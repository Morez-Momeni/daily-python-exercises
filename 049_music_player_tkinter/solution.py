"""
Problem #49: Music Player with Tkinter GUI
Date: 2026-09-13

A graphical music player built with Tkinter.
The UI provides:
- An entry to type a song name.
- A "Show Musics" button that lists available tracks in a table.
- Play / Pause / Un-Pause buttons.
The actual music logic (play, pause, unpause, list) is imported from a separate `logic` package.
"""

import tkinter as tk
from logic.logic import play_music, pause_music, unpause_music, list_music


window = tk.Tk()

window.title("Music-Player")
window.geometry("400x300")


# Music Table


music_table_frame = tk.Frame(window)
music_table_frame.pack(pady=10)


def play():

    music_name = entry_music_name.get()
    play_music(music_name)


def show_music():

    musics = list_music()

    for r, music in enumerate(musics):
        for c, value in enumerate(music):

            text_widget = tk.Label(
                music_table_frame,
                text=value,
                width=15,
                borderwidth=1,
                relief="solid"
            )

            text_widget.grid(
                row=r,
                column=c,
                padx=2,
                pady=2
            )



# Music Name

music_name_label = tk.Label(
    window,
    text="Enter music name"
)

music_name_label.pack(pady=(5, 3))


entry_music_name = tk.Entry(
    window,
    width=30
)

entry_music_name.pack(pady=3)


# Buttons

show_music_button = tk.Button(
    window,
    text="Show Musics",
    command=show_music,
    width=15
)

show_music_button.pack(pady=8)


controls_frame = tk.Frame(window)
controls_frame.pack(pady=10)


play_music_button = tk.Button(
    controls_frame,
    text="Play",
    command=play,
    width=10
)

play_music_button.grid(
    row=0,
    column=0,
    padx=4
)


pause_music_button = tk.Button(
    controls_frame,
    text="Pause",
    command=pause_music,
    width=10
)

pause_music_button.grid(
    row=0,
    column=1,
    padx=4
)


unpause_music_button = tk.Button(
    controls_frame,
    text="Un-Pause",
    command=unpause_music,
    width=10
)

unpause_music_button.grid(
    row=0,
    column=2,
    padx=4
)


window.mainloop()