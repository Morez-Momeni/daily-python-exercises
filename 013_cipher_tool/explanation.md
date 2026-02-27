# Project 13: Cipher Tool (Caesar & Atbash)

## Project Overview
This is a command-line tool that implements three classic ciphers:
- **Caesar cipher** 
- **Atbash cipher** 
- **Vigenère cipher**

The tool features a modular design, with each cipher in its own module, and an interactive menu built with the `rich` library for a polished terminal experience.

**Current Version:** (2026-02-27) – now includes Vigenère cipher.
---

## Features
- **Caesar cipher**
  - Encode/decode any text with adjustable shift.
  - Shift can be changed at runtime.
  - Handles uppercase and lowercase letters separately.
- **Atbash cipher**
  - Encode/decode using the reverse alphabet mapping.
  - Since Atbash is symmetric, encode and decode are identical.
- **Vigenère cipher**
  - Uses a keyword that repeats cyclically.
  - Key can be changed interactively
- **Interactive menu** with submenus for each cipher.
- **Modular design** – each cipher is in its own Python file.


---

## Cipher Implementations

### Caesar (`caesar.py`)
- Class `Caesar` with `__shift` (private).
- Uses `string.ascii_lowercase` and `string.ascii_uppercase`.
- Encode: `(position + shift) % 26`
- Decode: `(position - shift) % 26`

### Atbash (`atbash.py`)
- Class `Atbash` with four private strings representing the first and second halves of the alphabet (both uppercase and lowercase).
- For each character, it checks which half it belongs to and maps it to the corresponding character in the opposite half.
- Since Atbash is self‑inverse, `decode()` simply calls `encode()`.

### Vigenère (`vigenere.py`)
- Class `Vigenere` with a private `__key`.
- Builds a repeated‑key string of the same length as the message.
- For each character:
  - Determines the numeric position (0–25) of the message letter and the key letter (using `ord` and subtracting base `'A'` or `'a'`).
  - **Encode:** `(msg_pos + key_pos) % 26`
  - **Decode:** `(msg_pos - key_pos) % 26`
  - Converts back to a letter using the appropriate alphabet string.
- Non‑letters are left unchanged.

---
## How to Run
1. Ensure all files are in the correct folder structure.
2. Install the `rich` library if not already installed:

   ```bash

   pip install rich

   ```
3. Run the main script:

    ```python

    python solution.py

    ```
---
## Example Usage
- **Caesar**

    - Input: "Hello" with shift 3 → Output: "Khoor"

    - Input: "Khoor" with shift 3 → Output: "Hello"

- **Atbash**

    - Input: "Hello" → Output: "Svool"

    - Input: "Svool" → Output: "Hello"

- Vigenère (key "key")
    
    - "Hello" → "Rijvs" → "Hello"

    - "hello" → "rijvs" → "hello"
---


