from app.utils.constants import CLOUDCOLOR1, SCREEN_WIDTH, SCREEN_HEIGHT
import random

class Cloud:
    def __init__(self): #Implementamos las coordenadas y la imagen a utilizar
        self.image = CLOUDCOLOR1
        self.image_width = self.image.get_width()
        self.x_pos_cloud = SCREEN_WIDTH + random.randint(800, 1000)
        self.y_pos_cloud = random.randint(50, 100)

    def update(self, game_speed): #velocidad de movimiento de cloud = game_speed
        self.x_pos_cloud -= game_speed #Aqui hacemos mover el cloud de derecha a izquierda en la pantalla #X se va reduciendo de acuerdo a la velocidad del juego
        if self.x_pos_cloud < -self.image_width:
            self.x_pos_cloud = SCREEN_WIDTH + random.randint(2500, 3500)
            self.y_pos_cloud = random.randint(50, 100) #Posicones aleatorias de y

    def draw(self, screen):
        screen.blit(self.image,(self.x_pos_cloud,self.y_pos_cloud))

