import logging
import zipfile
from pathlib import Path

import pyzipper


class Cracker:
    def __init__(self, path):
        self.path = Path(path)
        self.logger = logging.getLogger("Ziply")
        self.logger.setLevel(logging.ERROR)
        if not self.logger.handlers:
            handler = logging.FileHandler(
                Path(__file__).resolve().parent / "app.log",
                encoding="utf-8"
            )
            handler.setFormatter(logging.Formatter(
                "%(asctime)s %(levelname)s: %(message)s"
            ))
            self.logger.addHandler(handler)

        base_dir = Path(__file__).resolve().parent
        self.extracted_path = base_dir / "Extracted"
        self.password_file = base_dir / "passwd.txt"
        self.extracted_path.mkdir(parents=True, exist_ok=True)

    def unzip(self):
        if not self.path.is_file():
            self.logger.error("ZIP file was not found.")
            return False

        if not zipfile.is_zipfile(self.path):
            self.logger.error("Input is not a valid ZIP file.")
            return False

        try:
            with pyzipper.AESZipFile(self.path, "r") as archive:
                archive.extractall(path=self.extracted_path)
            return True
        except (RuntimeError, pyzipper.zipfile.BadZipFile) as error:
            message = str(error).lower()
            if "password" not in message and "encrypt" not in message:
                self.logger.error("Could not extract ZIP without a password: %s", error)
                return False
        except Exception:
            self.logger.exception("Unexpected error during initial extraction.")
            return False

        if not self.password_file.is_file():
            self.logger.error("passwd.txt was not found.")
            return False

        try:
            with self.password_file.open("r", encoding="utf-8", errors="replace") as handle:
                passwords = [line.strip() for line in handle if line.strip()]
        except OSError:
            self.logger.exception("Could not read passwd.txt.")
            return False

        for password in passwords:
            try:
                with pyzipper.AESZipFile(self.path, "r") as archive:
                    archive.extractall(
                        path=self.extracted_path,
                        pwd=password.encode("utf-8")
                    )
                return True
            except (RuntimeError, ValueError) as error:
                self.logger.debug("A candidate password did not work: %s", error)
            except Exception:
                self.logger.exception("Unexpected error while trying a candidate password.")
                return False

        self.logger.error("No password in passwd.txt successfully extracted the ZIP.")
        return False
