#!/usr/bin/python3

import pygame


# OBJETO PACMAN CON SUS IMAGENES DE SPRITE
class pacman(pygame.sprite.Sprite):
    def __init__(self, position):
        #CARGA LA IMAGEN
        self.sheet = pygame.image.load('sprite_pacman.png')


        # IMAGEN DE INICIO, SOLO EL PEDAZO DE IMAGEN QUE QUEREMOS
        self.sheet.set_clip(pygame.Rect(850, 0, 35, 30))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        #POSICION INICIAL
        self.rect.topleft = position

        #SIEMPRE INICIA EN EL FRAME INICAL
        self.frame = 0

        #LOS DIREFENTES FLAMES, PARA GENERAR LA RECORRIDO
        self.left_states = { 0: (850, 350, 38, 40), 1: (850, 0, 38, 40) }
        self.right_states = { 0: (850,52, 38, 40), 1: (850, 0, 38, 40) }
        self.up_states = { 0: (850, 510, 38, 40), 1:(850, 0, 38, 40)}
        self.down_states = { 0: (850, 190, 38, 40), 1: (850, 0, 38, 40)}


#FUNCION PARA RECORRER EL FLAME, RECORRIEDO DE IMAGENES
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect


# GENERA EL MOVIMIENTO EN (X,Y) EL MOVIMIENTO ES EN 5 EN 5
    def update(self, direction):
        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= 2
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += 2
        if direction == 'up':
            self.clip(self.up_states)
            self.rect.y -= 2
        if direction == 'down':
            self.clip(self.down_states)
            self.rect.y += 2

        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        if direction == 'stand_down':
            self.clip(self.down_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())



#FUNCION PARA LEER EL TECLADO, LAS FECHAS
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_UP:
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.update('down')

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                self.update('stand_left')
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            if event.key == pygame.K_UP:
                self.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.update('stand_down')
