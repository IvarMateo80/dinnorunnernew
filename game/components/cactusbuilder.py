#el cactusbuilder es el responsable de darme cactus de distintas formas ,  etc
import random
from game.components.cactus import Cactus
from game.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class CactusBuilder:
    def __init__(self):
        self.cactuses = []
        pass

    def update(self):
        #self.cactuses.append()
        randon_number = random.randint(0, 1)
        cactus_images = SMALL_CACTUS if randon_number == 0 else LARGE_CACTUS

        for img_cactus in cactus_images:
            cactus = Cactus(img_cactus)
            self.cactuses.append(cactus)
        pass
        # self.cactuses.pop() #pop remueve el elemento de la cola


    def draw(self, screen):
        y = 300
        x = 300
        for cactus in self.cactuses:
            y += 20
            cactus.draw(screen, x ,y)

        #esto limpia la lista de cactuses
        self.cactuses = []
        pass