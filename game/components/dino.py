import random

import pygame

from game.utils.constants import DUCKING, JUMPING, RUNNING


class Dinosaur:
    COORD_X = 80
    COORD_Y = 320
    JUMP_VEL = 8

    def __init__(self, name):
        self.duck_img = DUCKING[0]
        self.run_img = RUNNING[0]
        self.jump_img = JUMPING
        self.image = self.run_img
        
        self.dino_rect = self.image.get_rect() #empezamos a usar get.rect()
        self.dino_rect.x = self.COORD_X
        self.dino_rect.y = self.COORD_Y
        self.name = name
        self.font = pygame.font.SysFont('segoe print', 18)
        self.status= "running"
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL


    #todo dinosaur sabe como dibujarse en un screen (de pygame)
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x,self.dino_rect.y)) #dibuja la imagen en una posicion 
        screen.blit(self.text, (80, 500))

    #todo dinosaur sabe como correr (run)
    def run(self):
        self.dino_rect.y = self.COORD_Y
        #generamos el efecto de que el dinosaur corre intercalando imagenes
        selected_image_index = random.randint(0, 1)
        #seleccionar imagen en posicion "selected_image_index"
        self.image = RUNNING[selected_image_index]

    def update(self):
        #actualizamos el estado del dinosaurio
        player = pygame.key.get_pressed()
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

        if player[pygame.K_UP] and not self.dino_duck or player[pygame.K_x] and not self.dino_duck:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
        elif player[pygame.K_RIGHT] or player[pygame.K_z]:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False
        elif player[pygame.K_DOWN] and not self.dino_jump or player[pygame.K_a] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False

        if self.dino_run == True and self.dino_duck == False and self.dino_jump == False: 
            self.status = "running"
        elif self.dino_run == False and self.dino_duck == False and self.dino_jump == True: 
            self.status = "Jumping"
        elif self.dino_run == False and self.dino_duck == True and self.dino_jump == False: 
            self.status = "ducking"
        self.text = self.font.render(f"The player {self.name} is {self.status}", True, (0, 0, 0))

    def duck(self):
        self.image == self.duck_img
        self.image = DUCKING[0]

        self.dino_rect.x = self.COORD_X
        self.dino_rect.y = 330


    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:  
            self.dino_rect.y -= self.jump_vel * 4 #Salto
            self.jump_vel -= 0.8 #subiendo y cuando es negativo baja
        if self.jump_vel < -self.JUMP_VEL: #cuando llega a JUMP_VEL negativo retornara 
            self.dino_rect.y = self.COORD_Y  #a su posicion en x
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL
            self.dino_run = True