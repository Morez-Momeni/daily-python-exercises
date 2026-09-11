import pygame

pygame.mixer.init()

pygame.mixer.music.load("music/song.mp3")

pygame.mixer.music.play()

input("Press Enter to stop...")