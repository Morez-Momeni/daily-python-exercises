# Problem 31: Text-to-Speech from a File

## Problem
Write a script that reads the contents of a text file and speaks each line aloud using text‑to‑speech. The program should handle interruptions gracefully (e.g., Ctrl+C to stop speaking) and support custom voice and speech rate settings.

## My Solution

I used the `pyttsx3` library, which is a cross‑platform text‑to‑speech engine for Python. The script:
1. Checks if the file exists.
2. Initialises the TTS engine.
3. Optionally sets a preferred voice and speaking rate.
4. Reads the file line by line and speaks each non‑empty line.
5. Catches `KeyboardInterrupt` to stop speaking cleanly.

