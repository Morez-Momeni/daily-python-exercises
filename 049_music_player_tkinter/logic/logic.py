import os
import pygame

DIR_MUSIC = os.path.join("musics")
pygame.mixer.init()


def play_music(music):
    
    try:
        music_path = os.path.join(DIR_MUSIC,music)
        if not os.path.isfile(music_path):
            print("Music not found:", music)
            return
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play()

    except pygame.error as e:
        print("Play Music Failed", e)
        return


def pause_music():
    try:    
        pygame.mixer.music.pause()
    except pygame.error as e:
        print("Pause Music Failed", e)
        return

def unpause_music():
    try:    

        pygame.mixer.music.unpause()
    except pygame.error as e:
        print("Un-Pause Music Failed", e)
        return


def list_music():
    musics = []
    for idx,music in enumerate(os.listdir(DIR_MUSIC),start=1):
        if music.endswith(".mp3"):
            musics.append((idx,music))
    if not musics:
        return f"Empty, please add music"
    return musics
    

if __name__ == "__main__":
    print("This moudle for control music player logic".title())