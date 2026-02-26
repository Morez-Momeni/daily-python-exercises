# Project 13: Cipher Tool (Caesar & Atbash)

## Project Overview
This is a command-line tool that implements two classic ciphers:
- **Caesar cipher** 
- **Atbash cipher** 

The tool features a modular design, with each cipher in its own module, and an interactive menu built with the `rich` library for a polished terminal experience.

**Current Version:** (2026-02-26) – now includes Atbash cipher.
---

## Features
- **Caesar cipher**
  - Encode/decode any text with adjustable shift.
  - Shift can be changed at runtime.
  - Handles uppercase and lowercase letters separately.
- **Atbash cipher**
  - Encode/decode using the reverse alphabet mapping.
  - Since Atbash is symmetric, encode and decode are identical.
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

    Input: "Hello" with shift 3 → Output: "Khoor"

    Input: "Khoor" with shift 3 → Output: "Hello"

- **Atbash**

    - Input: "Hello" → Output: "Svool"

    - Input: "Svool" → Output: "Hello"

---

##  Future Improvements
- Add Vigenère cipher

