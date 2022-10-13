import pygame

pygame.init()  # iniciando

pygame.mixer.music.load('ex21.mp3')  # carregando arquivo
pygame.mixer.music.play()  # tocando
pygame.event.wait()  # esperar o evento terminar para parar a musica
