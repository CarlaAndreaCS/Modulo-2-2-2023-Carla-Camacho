from app.utils.constants import CLOUDCOLOR2, SCREEN_WIDTH, SCREEN_HEIGHT
import random

class Cloud_2:
    def __init__(self): #Implementamos las coordenadas y la imagen a utilizar
        self.image = CLOUDCOLOR2
        self.image_width = self.image.get_width()
        self.x_pos_cloud = SCREEN_WIDTH + random.randint(500, 800)
        self.y_pos_cloud = random.randint(50, 100)

    def update(self, game_speed): #velocidad de movimiento de cloud2
        self.x_pos_cloud -= game_speed #Aqui hacemos mover el cloud de derecha a izquierda en la pantalla
        if self.x_pos_cloud < -self.image_width:
           self.x_pos_cloud = SCREEN_WIDTH + random.randint(1500, 2000) #Apariciones aleatorias entre las posicones definidas
           self.y_pos_cloud = random.randint(50, 100)

    def draw(self, screen):
        screen.blit(self.image,(self.x_pos_cloud,self.y_pos_cloud))

