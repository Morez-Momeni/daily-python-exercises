"""
Problem #63: Secure Token Generator (Bottle Web App)
Date: 2026-09-28

A minimal web application built with the Bottle micro-framework.
On each visit to the root URL, it generates a cryptographically secure
URL-safe token using Python's `secrets` module and renders it in a styled HTML page.
"""

from bottle import route, run, template
import secrets

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Secure Code Generator</title>

    <style>

        {% raw %}
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;

            background:
                radial-gradient(circle at top left, #182848, transparent 40%),
                radial-gradient(circle at bottom right, #4b1248, transparent 40%),
                #080b12;

            font-family: Arial, Helvetica, sans-serif;
            color: white;
        }

        .container {
            width: 90%;
            max-width: 700px;
            padding: 45px;

            text-align: center;

            background: rgba(255, 255, 255, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 24px;

            backdrop-filter: blur(20px);

            box-shadow:
                0 25px 80px rgba(0, 0, 0, 0.5),
                inset 0 1px 1px rgba(255, 255, 255, 0.08);
        }

        .badge {
            display: inline-block;
            padding: 7px 14px;
            margin-bottom: 20px;

            border-radius: 50px;

            background: rgba(120, 90, 255, 0.15);
            border: 1px solid rgba(120, 90, 255, 0.3);

            color: #a99cff;
            font-size: 13px;
            letter-spacing: 1px;
        }

        h1 {
            font-size: 38px;
            margin-bottom: 12px;

            background: linear-gradient(
                90deg,
                #ffffff,
                #a99cff
            );

            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .description {
            color: #9ca3af;
            font-size: 15px;
            margin-bottom: 35px;
        }

        .code-box {
            padding: 22px 25px;

            border-radius: 15px;

            background: rgba(0, 0, 0, 0.35);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .code {
            color: #8bffb0;
            font-family: "Courier New", monospace;

            font-size: 17px;
            line-height: 1.6;

            word-break: break-all;
        }

        .label {
            display: block;
            margin-bottom: 10px;

            color: #6b7280;
            font-size: 12px;

            text-transform: uppercase;
            letter-spacing: 2px;
        }

        .footer {
            margin-top: 25px;

            color: #4b5563;
            font-size: 12px;
        }

        @media (max-width: 600px) {

            .container {
                padding: 30px 20px;
            }

            h1 {
                font-size: 28px;
            }

            .code {
                font-size: 14px;
            }

        }
        {% endraw %}

    </style>
</head>

<body>

    <div class="container">

        <span class="badge">
            SECURE TOKEN
        </span>

        <h1>
            Generated Code
        </h1>

        <p class="description">
            A secure URL-safe token has been generated for you.
        </p>

        <div class="code-box">

            <span class="label">
                Your Token
            </span>

            <div class="code">
                {{code}}
            </div>

        </div>

        <div class="footer">
            Generated securely using Python secrets
        </div>

    </div>

</body>
</html>
"""


@route('/')
def index():
    code = secrets.token_urlsafe(32)
    return template(HTML, code=code)


if __name__ == "__main__":
    run(host='localhost', port=8080, reloader=True, debug=True)