import pygame
import random
from app.utils.constants import ICON2, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, BG2, SOL, SMALL_CACTUS, LARGE_CACTUS, BIRD, BGMENU4
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
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        
        self.cloud = Cloud() 
        self.cloud_2 = Cloud_2() 
        self.mountain = Mountain()

        self.Dinosaurio = Dinosaur("Pedro")

        self.obstacles = [] #AÑADIDO

        self.game_running = True

        self.cactus_not_done_number = 0
        self.cactus_done_number = 0
        self.colliderected_count_cactus = 0
        self.not_colliderected_count_cactus = 0
        self.total_cactus = 0

        self.birds_not_done_number = 0
        self.birds_done_number = 0
        self.colliderected_count_birds = 0
        self.not_colliderected_count_birds = 0
        self.total_birds = 0


        self.points = 0

        
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
            if self.points <= - 100:
                self.playing = False
                break  
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
        

    def update(self, game_speed):

        self.cloud.update(self.game_speed) 
        self.cloud_2.update(self.game_speed)
        self.mountain.update(self.game_speed) 
        user_input = pygame.key.get_pressed()
        self.Dinosaurio.update(user_input) 
        
        
        if len(self.obstacles) == 0:
           if random.randint(0, 2) == 0:
               self.obstacles.append(SmallCactus(SMALL_CACTUS))
               self.total_cactus += 1

               if self.colliderected_count_cactus > 0:
                   self.colliderected_count_cactus = 0
                   self.cactus_not_done_number += 1
                   self.points = self.points - 50 

               if self.not_colliderected_count_cactus> 0:
                   self.not_colliderected_count_cactus = 0
                   self.cactus_done_number += 1
                   self.points = self.points + 100
               
           elif random.randint(0, 2) == 1:
               self.obstacles.append(LargeCactus(LARGE_CACTUS))
               self.total_cactus += 1

               if self.colliderected_count_cactus > 0:
                   self.colliderected_count_cactus = 0
                   self.cactus_not_done_number += 1
                   self.points = self.points - 50

               if self.not_colliderected_count_cactus > 0:
                   self.not_colliderected_count_cactus = 0
                   self.cactus_done_number += 1
                   self.points = self.points + 100

           elif random.randint(0, 2) == 2:
               self.obstacles.append(Bird(BIRD))
               self.total_birds += 1

               if self.colliderected_count_birds > 0:
                   self.colliderected_count_birds = 0
                   self.birds_not_done_number += 1
                   self.points = self.points - 25  
                   
                
               if self.not_colliderected_count_birds > 0:
                   self.not_colliderected_count_birds = 0
                   self.birds_done_number += 1
                   self.points = self.points + 75   


        user_input = pygame.key.get_pressed()
        
        for obstacle in self.obstacles: #AÑADIDO
            obstacle.update(game_speed, self.obstacles)
            if  pygame.Rect.colliderect(self.Dinosaurio.dino_rect, obstacle.rect) and type(obstacle) is LargeCactus: #Cuando colisiona
                self.colliderected_count_cactus += 1
                

            elif  pygame.Rect.colliderect(self.Dinosaurio.dino_rect, obstacle.rect) and type(obstacle) is SmallCactus: #Cuando colisiona
                self.colliderected_count_cactus += 1
                 

            elif user_input[pygame.K_UP] and self.Dinosaurio.dino_rect.colliderect(obstacle.rect) == False:
                   self.not_colliderected_count_cactus += 1
                   

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if pygame.Rect.colliderect(self.Dinosaurio.dino_rect, obstacle.rect) and type(obstacle) is Bird:
                     self.colliderected_count_birds += 1

            elif user_input[pygame.K_DOWN] and self.Dinosaurio.dino_rect.colliderect(obstacle.rect) == False:
                  self.not_colliderected_count_birds += 1
                 

    def show_text(self):
        
        text, text_rect = self.text_screen.name(self)
        self.screen.blit(text, text_rect)
        
        text, text_rect = self.text_screen.cactus_done(self.cactus_done_number) 
        self.screen.blit(text, text_rect) 
        
        text, text_rect = self.text_screen.cactus_not_done(self.cactus_not_done_number) 
        self.screen.blit(text, text_rect)

        text, text_rect = self.text_screen.birds_not_done(self.birds_not_done_number) 
        self.screen.blit(text, text_rect)

        text, text_rect = self.text_screen.birds_done(self.birds_done_number) 
        self.screen.blit(text, text_rect)

        text, text_rect = self.text_screen.score(self.points)
        self.screen.blit(text, text_rect)

       

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((135, 206,235)) 
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
        

    def show_menu(self):
        
        self.game_running = True
        self.screen.blit(BGMENU4, (0,0))
        self.print_menu_elements()
        pygame.display.update()

    def print_menu_elements(self):
        text, text_rect = self.text_screen.menu_message("¿DO YOU WANT TO WAKE UP THE DINO?" )
        self.screen.blit(text, text_rect)

        text, text_rect = self.text_screen.menu_message_two("PRESS ANY KEY" )
        self.screen.blit(text, text_rect)
        self.handle_key_events()

    def handle_key_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN: #Detecta si alguna tecla ha sido presionada
                self.run()

