#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys

# -----------
# Constantes
# -----------

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------


# ------------------------------
# Funcion principal del juego
# ------------------------------


def main():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Juego de Manolo")

    # cargamos el fondo y una imagen (se crea objetos "Surface")
    fondo = pygame.image.load("fondo.jpg").convert()
    tux = pygame.image.load("bola.png").convert_alpha()
    bicho = pygame.image.load("bicho.png").convert_alpha()

    bicho_pos_x = 10
    bicho_pos_y = 330

    tux_pos_x = 550
    tux_pos_y = 300

    # Indicamos la posicion de las "Surface" sobre la ventana
    screen.blit(bicho, (bicho_pos_x, bicho_pos_y))
    screen.blit(tux, (tux_pos_x, tux_pos_y))
    screen.blit(fondo, (0, 0))
    # se muestran lo cambios en pantalla
    pygame.display.flip()

    # el bucle principal del juego
    reloj = pygame.time.Clock()
    while True:
        # le restamos 1 a la coordenada x de tux y comprobamos
        # que no alcance el borde de la pantalla
        tux_pos_x = tux_pos_x - 0.5
        if tux_pos_x < 1:
            tux_pos_x = 550
        presionada = pygame.key.get_pressed()
        if presionada[K_SPACE]:
	    bicho_pos_y = 5
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
                sys.exit(0)
    return 0    


if __name__ == "__main__":
    main()
