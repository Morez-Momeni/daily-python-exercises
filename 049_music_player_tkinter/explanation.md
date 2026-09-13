# Problem 49: Music Player with Tkinter GUI

## Problem
Build a graphical music player using Tkinter with the following features:
- An entry field to type the name of a song.
- A button to display a list of available tracks in a table.
- Buttons to play, pause, and unpause music.
- The audio logic should be separated into a `logic` module.

## My Solution

I separated the application into two layers:

1. **UI layer** (`solution.py`) – built with Tkinter, handles layout, buttons, and user interaction.
2. **Logic layer** (`logic/logic.py`) – contains the actual music functions (`play_music`, `pause_music`, `unpause_music`, `list_music`), which likely use `pygame.mixer` or a similar library.
