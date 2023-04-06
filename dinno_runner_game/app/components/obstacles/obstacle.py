from app.utils.constants import SCREEN_WIDTH
from pygame.sprite import Sprite

class Obstacle(Sprite): #Clase general

    def __init__(self, image_list, obstacle_type): #Generalizando para todos los obstaculos existentes
        self.image_list = image_list
        self.obstacle_type = obstacle_type
        self.rect = image_list[obstacle_type].get_rect()
        self.rect.x = SCREEN_WIDTH   #Y no se puede definir(porque no tienen la misma posicion). pero x si se puede, el lado derecho de la pantalla self.passed = False
        

    def update(self, game_speed, obstacles):
        self.rect.x = self.rect.x - game_speed  #Reducimos la posicion en x de acuerdo al game_speed, moviendo de derecha a izquierda
        if self.rect.x <= 0: #Si el obstaculo salio de la poisicion de x, elimina el obstaculo
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image_list[self.obstacle_type], (self.rect))

