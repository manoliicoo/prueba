#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Juego de Manolo")

    fondo = pygame.image.load("fondo.jpg").convert()
    tux = pygame.image.load("bola.png").convert_alpha()
    bicho = pygame.image.load("bicho.png").convert_alpha()

    bicho_pos_x = 10
    bicho_pos_y = 330

    tux_pos_x = 550
    tux_pos_y = 300

    screen.blit(bicho, (bicho_pos_x, bicho_pos_y))
    screen.blit(tux, (tux_pos_x, tux_pos_y))
    screen.blit(fondo, (0, 0))
    pygame.display.flip()
    pygame.mixer.music.load("musica.mp3")
    pygame.mixer.music.play(1)
    reloj = pygame.time.Clock()
    while True:
        tux_pos_x = tux_pos_x - 0.5
        if tux_pos_x < 1:
            tux_pos_x = 550
        presionada = pygame.key.get_pressed()
        if presionada[K_UP]:
	    bicho_pos_y = bicho_pos_y -1
             
        if presionada[K_DOWN]:
	    bicho_pos_y = bicho_pos_y +1
       
        if presionada[K_LEFT]:
            bicho_pos_x = bicho_pos_x -1
  
        if presionada[K_RIGHT]:
            bicho_pos_x = bicho_pos_x +1

           # reloj.tick(1)
           # bicho_pos_y = 330
            pygame.display.update()
          #  bicho_pos_y = 330
        # Redibujamos todos los elementos de la pantalla
        screen.blit(fondo, (0, 0))
        screen.blit(tux, (tux_pos_x, tux_pos_y))
        screen.blit(bicho, (bicho_pos_x, bicho_pos_y))
        # se muestran lo cambios en pantalla
        pygame.display.flip()

        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
    return 0    


if __name__ == "__main__":
    main()
