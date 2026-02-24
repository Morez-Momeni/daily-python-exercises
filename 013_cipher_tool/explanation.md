# Project 13: Cipher Tool – Caesar Cipher (CLI)

## Project Overview
This is a simple command‑line tool for encryption/decryption using the **Caesar cipher**. It is the first part of a larger cipher toolkit that will eventually include Atbash and Vigenère. The project demonstrates:
- Modular design (cipher logic in a separate module).
- Interactive menu with submenus using the `rich` library.
- Proper handling of uppercase/lowercase letters and non‑alphabetic characters.
- Adjustable shift value.

**Current Version:**  (Caesar only) – 2026‑02‑25

---

## Features
- **Caesar cipher** with a user‑defined shift (default 3).
- **Encode** any text – only letters are shifted; numbers, punctuation, and spaces remain unchanged.
- **Decode** any text – reverse the shift.
- **Change shift** at runtime.
- Clean, colourful terminal interface using `rich`.
- Modular structure – easy to add new ciphers later.



---

## Class Design (`Caesar` in `caesar.py`)

| Attribute / Method | Description |
|---------------------|-------------|
| `__shift`           | Current shift value (private). |
| `__letters_lower`   | String `'abcdefghijklmnopqrstuvwxyz'`. |
| `__letters_upper`   | String `'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`. |
| `encode(text)`      | Returns the encrypted version of `text`. |
| `decode(text)`      | Returns the decrypted version of `text`. |
| `change_shift(new)` | Updates the shift. |

**How it works:**
- For each character, check if it is uppercase, lowercase, or neither.
- If it's a letter, find its position in the corresponding alphabet string using `.find()`.
- Add (or subtract) the shift, take modulo 26 to wrap around, and look up the resulting letter.
- Non‑letters are appended unchanged.

---

##  Future Improvements
- Add Atbash cipher
- Add Vigenère cipher

