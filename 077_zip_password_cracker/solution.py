"""
Problem #77: ZIP Password Cracker (Dictionary Attack)
Date: 2026-10-20

Attempts to open an AES-encrypted ZIP file by trying each password from a
wordlist (passwd.txt). Logs every wrong password to app.log.
"""

import os
import pyzipper
import logging


class Cracker:
    def __init__(self, path) -> None:
        self.path = path
        self.logger = logging.getLogger("SimpleLogger")
        self.logger.setLevel(logging.ERROR)
        file_handler = logging.FileHandler("app.log")
        self.logger.addHandler(file_handler)

    def unzip(self):
        if not os.path.isfile(self.path):
            self.logger.error(f"File:{self.path} Not Found")
            return False

        with open('passwd.txt', 'r') as f:
            passwords = f.readlines()
            table = str.maketrans('\n', ' ')
            for password in passwords:
                password = password.translate(table).strip().encode()

                try:
                    with pyzipper.AESZipFile(self.path, 'r') as zf:
                        zf.extractall(pwd=password)
                        return True

                except RuntimeError as e:
                    self.logger.error(f"Password: {password} is Wrong ,Error:{e}")


x = Cracker('iris.zip')
print(x.unzip())