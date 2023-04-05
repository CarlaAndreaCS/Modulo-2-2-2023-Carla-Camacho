import pygame
import random
from app.utils.constants import ICON2, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, BG2, SOL, SMALL_CACTUS, LARGE_CACTUS, BIRD
from app.components.obstacles.cactus import SmallCactus, LargeCactus
from app.components.obstacles.bird import Bird
from app.components.cloud import Cloud
from app.components.cloud_2 import Cloud_2
from app.components.mountain import Mountain
from app.components.dinosaur import Dinosaur
from app.components.textscreen import TextScreen

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON2)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        
        self.cloud = Cloud() 
        self.cloud_2 = Cloud_2() 
        self.mountain = Mountain()

        self.Dinosaurio = Dinosaur()

        self.obstacles = [] #AÑADIDO

        self.obstacles_not_done_number = 0
        self.obstacles_done_number = 0

        
        self.text_screen = TextScreen() #AÑADIDO

        pygame.mixer.init() 
        sonido_fondo = pygame.mixer.Sound('Slime.wav') 
        pygame.mixer.Sound.play(sonido_fondo, -1) 

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update(self.game_speed)
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

        if len(self.obstacles) == 0:   #AÑADIDO
           if random.randint(0, 2) == 0:
               self.obstacles.append(SmallCactus(SMALL_CACTUS))
           elif random.randint(0, 2) == 1:
               self.obstacles.append(LargeCactus(LARGE_CACTUS))
           elif random.randint(0, 2) == 2:
               self.obstacles.append(Bird(BIRD))
        

    def update(self, game_speed):

        self.cloud.update(self.game_speed) 
        self.cloud_2.update(self.game_speed)
        self.mountain.update(self.game_speed) 
        user_input = pygame.key.get_pressed()
        self.Dinosaurio.update(user_input) 
        
        for obstacle in self.obstacles: #AÑADIDO
            obstacle.update(game_speed, self.obstacles) 
            #if self.Dinosaurio.dino_rect.colliderect(obstacle.rect): #Cuando colisiona
                #pygame.time.delay(100) #El juego se pausa
                #self.cactus_done_number = self.cactus_done_number + 1



       

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((135, 206,235)) #CAMBIO COLOR SKY BLUE #135, 206, 235
        self.draw_background()
        self.cloud.draw(self.screen) 
        self.cloud_2.draw(self.screen) 
        self.mountain.draw(self.screen)
        self.Dinosaurio.draw(self.screen) 

        for obstacle in self.obstacles: #AÑADIDO
            obstacle.draw(self.screen)

        self.show_text()


        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG2.get_width() 
        self.screen.blit(BG2, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG2, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG2, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

        self.screen.blit(SOL, (SCREEN_WIDTH -100, SCREEN_HEIGHT//2 -300))
        
    def show_text(self):
        
        #Nombre
        text, text_rect = self.text_screen.name() 
        self.screen.blit(text, text_rect) 
        
        #No colision con obstaculos

        for obstacles in self.obstacles: #AÑADIDO
         user_input = pygame.key.get_pressed()
         if user_input[pygame.K_DOWN] and self.Dinosaurio.dino_rect.colliderect(obstacles.rect) == False or user_input[pygame.K_UP] and self.Dinosaurio.dino_rect.colliderect(obstacles.rect) == False:
                self.obstacles_done_number = self.obstacles_done_number + 1
        text, text_rect = self.text_screen.obstacles_done(self.obstacles_done_number) 
        self.screen.blit(text, text_rect) 

        #colision con obstaculos
        
        for obstacles in self.obstacles: #AÑADIDO
         if self.Dinosaurio.dino_rect.colliderect(obstacles.rect): #Cuando colisiona
                self.obstacles_not_done_number = self.obstacles_not_done_number + 1

        text, text_rect = self.text_screen.obstacles_not_done(self.obstacles_not_done_number) 
        self.screen.blit(text, text_rect)