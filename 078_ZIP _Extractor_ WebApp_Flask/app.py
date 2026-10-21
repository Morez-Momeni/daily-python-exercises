from pathlib import Path
from uuid import uuid4
import shutil

from flask import Flask, jsonify, render_template, request
from werkzeug.utils import secure_filename

from cracker import Cracker

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
EXTRACT_DIR = BASE_DIR / "Extracted"

app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
EXTRACT_DIR.mkdir(parents=True, exist_ok=True)


@app.errorhandler(413)
def file_too_large(_error):
    return jsonify({
        "ok": False,
        "message": "حجم فایل بیشتر از حد مجاز (۵۰ مگابایت) است."
    }), 413


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/extract", methods=["POST"])
def extract():
    uploaded_file = request.files.get("file")

    if uploaded_file is None or not uploaded_file.filename:
        return jsonify({
            "ok": False,
            "message": "فایلی انتخاب نشده است."
        }), 400

    original_name = secure_filename(uploaded_file.filename)
    if not original_name or Path(original_name).suffix.lower() != ".zip":
        return jsonify({
            "ok": False,
            "message": "فقط فایل ZIP قابل قبول است."
        }), 400

    upload_path = UPLOAD_DIR / f"{uuid4().hex}.zip"
    uploaded_file.save(upload_path)

    try:
        
        for item in EXTRACT_DIR.iterdir():
            if item.is_symlink() or item.is_file():
                item.unlink()
            elif item.is_dir():
                shutil.rmtree(item)

        cracker = Cracker(str(upload_path))
        result = cracker.unzip()

        if result is not True:
            return jsonify({
                "ok": False,
                "message": (
                    "استخراج انجام نشد. ممکن است فایل خراب باشد، "
                    "یا رمز مناسب در passwd.txt وجود نداشته باشد."
                )
            }), 422

        extracted_files = []
        for item in EXTRACT_DIR.rglob("*"):
            
            if item.is_file() and not item.is_symlink():
                extracted_files.append({
                    "name": item.relative_to(EXTRACT_DIR).as_posix(),
                    "size": item.stat().st_size
                })

        return jsonify({
            "ok": True,
            "message": "استخراج با موفقیت انجام شد.",
            "files": extracted_files
        })

    except Exception:
        app.logger.exception("ZIP extraction failed")
        return jsonify({
            "ok": False,
            "message": "هنگام استخراج خطایی رخ داد. جزئیات در ترمینال سرور ثبت شد."
        }), 500

    finally:
        upload_path.unlink(missing_ok=True)


if __name__ == "__main__":
   
    app.run(debug=True)
