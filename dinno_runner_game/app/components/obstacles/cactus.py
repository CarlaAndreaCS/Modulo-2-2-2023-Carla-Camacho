import random
from app.components.obstacles.obstacles import Obstacle



class LargeCactus(Obstacle): #Cactus va a heredar todo de la clase obstacle
    def __init__(self, image_list):
        self.obstacle_type = random.randint(0, 2) #Llamando imagenes al azar entre 0 y 2
        super().__init__(image_list, self.obstacle_type) #Llamamos metodo construtor de Obstacle
        #self.image_list = image_list
        #self.obstacle_type = obstacle_type
        #self.rect = image_list[obstacle_type].get_rect()
        #self.rect.x = SCREEN_WIDTH 
        self.rect.y = 340  #Atributo de large cactus 

class SmallCactus(Obstacle):
    def __init__(self, image_list):
        self.obstacle_type = random.randint(0, 2)
        super().__init__(image_list, self.obstacle_type)
        self.rect.y = 355 
