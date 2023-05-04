import random
from game.components.obstacle import Obstacle
from game.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self, image):
        self.image = BIRD[0]
        self.rect = self.image.get_rect()
        self.type = 0
        super().__init__(image, self.type)
        
        self.rect.y = random.randint(225, 300)

    def update(self, game_speed, obstacles):
        super().update(game_speed, obstacles)
        self.fly()

    def fly(self):
        selected_image_index = random.randint(0, 1)
        self.image = BIRD[selected_image_index]

    def draw(self, screen):
        #self.rect.y = random.randint(225, 300)
        screen.blit(self.image,(self.rect.x,self.rect.y))