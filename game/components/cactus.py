

#class cactus representa a un solo cactus
#quiero poder generar distintos objetos cactus diferentes
#la responsabilidad de generar objetos cactus diferentes NO ES DE LA CALSE CACTUS
#TIENE QUE SER RESPONSABLE OTRA CLASE
import random
from game.components.obstacle import Obstacle
from game.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class Cactus(Obstacle): 

    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        if image == SMALL_CACTUS:
            self.rect.y = 325
        else:
            self.rect.y = 300

    #def draw(self, screen, x, y):
        #cactus_rect = self.image.get_rect()
        #cactus_rect.y = y
        #cactus_rect.x = x
        #screen.blit(self.image, cactus_rect)

   
