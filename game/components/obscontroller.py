import random

import pygame
from game.components.birds import Bird
from game.components.cactus import Cactus
from game.utils.constants import BIRD, LARGE_CACTUS, SMALL_CACTUS


class Builder:
    def __init__(self):
        self.obstacles = []
        self.bird_counter = 0
        self.cactus_counter = 0
        self.font = pygame.font.SysFont('segoe print', 18)

    
    def update(self, game):
        if len(self.obstacles) == 0:
            self.type = random.randint(0,2)
            if self.type == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif self.type == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            elif self.type == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.dinosaur.dino_rect.colliderect(obstacle.rect):
                if type(obstacle) is Cactus:
                    self.cactus_counter += 1
                    game.points -= 5
                    self.obstacles = []
                elif type(obstacle) is Bird:
                    self.bird_counter += 1
                    game.points -= 2.5
                    self.obstacles = []
                if game.points <= 0:
                    game.playing = False
                    self.bird_counter = 0
                    self.cactus_counter = 0

        
        self.text = self.font.render(f"Mario collided with a cactus {self.cactus_counter} times", True, (0, 0, 0))
        self.text2 = self.font.render(f"Mario collided with a bird {self.bird_counter} times", True, (0, 0, 0))
        self.text3 = self.font.render(f"Total Points: {game.points}", True, (0, 0, 0))
            
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        
        screen.blit(self.text, (15, 20))
        screen.blit(self.text2, (15, 60))
        screen.blit(self.text3, (900, 50))

