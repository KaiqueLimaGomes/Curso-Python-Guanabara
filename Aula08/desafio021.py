#Desafio021
#Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.
import time
import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("alarmeDesafio021.mp3")
pygame.mixer.music.play()
input('Tocando musica... Precione ENTER para PARAR') #Só funcionou assim!
pygame.mixer.music.stop()
pygame.quit()
