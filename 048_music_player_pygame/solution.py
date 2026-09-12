"""
Problem #48: Advanced Music Player with Pygame
Date: 2026-09-12

A command-line music player that:
- Scans a folder for audio files (MP3, WAV, OGG).
- Displays a numbered list of available tracks.
- Allows the user to play, stop, or quit interactively.
"""

import os
import pygame


MUSIC_FOLDER = "music"


def get_music_files():
    music_files = []

    for file in os.listdir(MUSIC_FOLDER):
        if file.lower().endswith((".mp3", ".wav", ".ogg")):
            music_files.append(file)

    return music_files


def show_music_list(music_files):
    print("\nMusic List")
    print("-" * 30)

    for index, music in enumerate(music_files, start=1):
        print(f"{index}. {music}")

    print("-" * 30)


def play_music(music_file):
    music_path = os.path.join(MUSIC_FOLDER, music_file)

    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play()

    print(f"\nPlaying: {music_file}")


def stop_music():
    pygame.mixer.music.stop()
    print("\nMusic stopped.")


def main():
    pygame.mixer.init()

    if not os.path.isdir(MUSIC_FOLDER):
        print(f"Folder '{MUSIC_FOLDER}' not found!")
        return

    music_files = get_music_files()

    if not music_files:
        print("No music files found!")
        return

    while True:
        show_music_list(music_files)

        print("Commands:")
        print("P - Play")
        print("S - Stop")
        print("Q - Quit")

        command = input("\nEnter command: ").strip().lower()

        if command == "p":
            try:
                choice = int(input("Choose song number: "))

                if choice < 1 or choice > len(music_files):
                    print("Invalid song number!")
                    continue

                selected_music = music_files[choice - 1]
                play_music(selected_music)

            except ValueError:
                print("Please enter a valid number!")

        elif command == "s":
            stop_music()

        elif command == "q":
            stop_music()
            print("Goodbye!")
            break

        else:
            print("Unknown command!")


if __name__ == "__main__":
    main()