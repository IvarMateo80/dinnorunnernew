import pygame
#from game.components.cactusbuilder import CactusBuilder
from game.components.dino import Dinosaur
from game.components.obscontroller import Builder
#from game.components.cactus import Cactus

from game.utils.constants import BG, CLOUD, DINO, GAMEOVER_RESTART, GROUND, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.dinosaur = Dinosaur("Mario")
        self.builder = Builder()
        self.game_speed = 20
        self.x_pos_g = 0
        self.y_pos_g = 390
        self.x_pos_cloud = SCREEN_WIDTH
        self.running = True
        self.font = pygame.font.SysFont('segoe print', 18)
        self.points = 100

    def run(self):
        # This is Game Loop: events - update - draw
        print("starting the game loop")
        self.playing = True
        #self.game_speed = 20
        while self.playing:
            self.capture_events()
            self.update()
            self.draw()

    def capture_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                print("received event.type", event.type, "that indicates `quit` game")
            
    
    #actualiza estado de los objetos del juego
    def update(self):
        self.dinosaur.update()
        self.builder.update(self)

    #actualizando el display del juego
    def draw(self):
        #print("entering draw")
        self.clock.tick(FPS)
        self.screen.fill((112, 202, 238)) #255, 255, 255
        self.draw_ground()
        self.draw_clouds()
        #draw dinosaur
        self.dinosaur.draw(self.screen)

        #le pedimos al obscontroller que nos dibuje cactus y pajaros
        self.builder.draw(self.screen)
        
        #dibujamos los cambios en pantalla
        pygame.display.update()
        pygame.display.flip()
        #print("exiting draw")

    def execute (self):
        while self.running: 
            if not self.playing:
                self.show_menu()
    
    def show_menu(self):
        self.running = True
        self.screen.fill((112, 202, 238))
        self.print_menu_elements()
        pygame.display.update()
        self.press_key_events_on_menu()

    def draw_clouds(self):
        positions = [(self.x_pos_cloud, 50), (self.x_pos_cloud - 300, 140), (self.x_pos_cloud + 100, 160), 
                     (self.x_pos_cloud + 450, 180), (self.x_pos_cloud + 900, 200), (self.x_pos_cloud + 320, 210), 
                     (self.x_pos_cloud + 800, 260)]
        for position in positions:
            self.screen.blit(CLOUD, position)
        self.x_pos_cloud -= 1
        if self.x_pos_cloud < -1000:
            self.x_pos_cloud = SCREEN_WIDTH

    def draw_ground(self):
        image_width = GROUND.get_width()
        self.screen.blit(GROUND, (self.x_pos_g, self.y_pos_g))
        self.screen.blit(GROUND, (image_width + self.x_pos_g, self.y_pos_g))
        
        #controlar que la imagen no se salga del borda derecho/izquierdo
        if self.x_pos_g <= -image_width:
            self.screen.blit(GROUND, (image_width + self.x_pos_g, self.y_pos_g))
            self.x_pos_g = 0
        self.x_pos_g -= self.game_speed

    def print_menu_elements(self):
        if self.points == 100:
            self.text = self.font.render(f"PRESS SPACE TO START", True, (0, 0, 0))
            self.screen.blit(self.text, (420, 300))
            self.screen.blit(DINO[1], (515, 200))

        elif self.points <= 0:
            self.text2 = self.font.render(f"Your points are 0, quit the game", True, (0, 0, 0))
            self.screen.blit(self.text2, (390, 300))
            self.text3 = self.font.render(f"or", True, (0, 0, 0))
            self.screen.blit(self.text3, (530, 330))
            self.text4 = self.font.render(f"PRESS SPACE TO RESTART", True, (0, 0, 0))
            self.screen.blit(self.text4, (400, 360))
            self.screen.blit(GAMEOVER_RESTART[0], (355, 150))
            self.screen.blit(GAMEOVER_RESTART[1], (500, 200))
            self.screen.blit(DINO[0], (515, 420))

    
    def press_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.points = 100
                    self.run()

