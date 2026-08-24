"""
Problem #31: Text-to-Speech from a File
Date: 2026-08-25

This script reads a text file and speaks its contents aloud using the pyttsx3 library.
It supports keyboard interrupt (Ctrl+C) to stop speaking immediately.
"""

import pyttsx3
import os

def speak_file(file_path):
    """
    Reads a text file line by line and speaks each non-empty line.
    """
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    engine = pyttsx3.init()

    voices = engine.getProperty("voices")
    if len(voices) > 33:
        engine.setProperty("voice", voices[33].id)
    engine.setProperty('rate', 140)  

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        for line in lines:
            line = line.strip()
            if line:  
                engine.say(line)
                engine.runAndWait()
    except KeyboardInterrupt:
        print("\nspeech interrupted by user.")
        engine.stop()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        engine.stop()  

if __name__ == "__main__":
   
    file_path = "~/file.txt"  # Change to your file path
    speak_file(file_path)
