# Problem 48: Advanced Music Player with Pygame

## Problem
Build a command‑line music player that:
- Scans a folder (`music/`) for audio files (MP3, WAV, OGG).
- Displays a numbered list of available tracks.
- Allows the user to play a selected track, stop playback, or quit the program.

## My Solution

I structured the program into small functions for clarity:
- `get_music_files()` – scans the folder and returns a list of audio files.
- `show_music_list(files)` – prints the numbered list of tracks.
- `play_music(file)` – loads and plays a selected file.
- `stop_music()` – stops the current playback.
- `main()` – ties everything together with a command loop.