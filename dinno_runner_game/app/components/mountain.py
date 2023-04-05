from app.utils.constants import MOUNTAIN, SCREEN_WIDTH, SCREEN_HEIGHT
import random

class Mountain:
    def __init__(self): #Implementamos las coordenadas y la imagen a utilizar
        self.image = MOUNTAIN
        self.image_width = self.image.get_width()
        self.x_pos_mountain = SCREEN_WIDTH -1100 
        self.y_pos_mountain = SCREEN_HEIGHT -370

    def update(self, game_speed): #velocidad de movimiento de la montaña
        self.x_pos_mountain -= game_speed #Aqui hacemos mover la montaña de derecha a izquierda en la pantallla #la posicion en x se reduce de acuerdo a la velocidad del juego
        if self.x_pos_mountain < -self.image_width:
           self.x_pos_mountain = SCREEN_WIDTH + random.randint(1000, 3000) #Posiciones aleatorias para que bayan apareciendo
           self.y_pos_mountain = SCREEN_HEIGHT -370

    def draw(self, screen):
        screen.blit(self.image,(self.x_pos_mountain, self.y_pos_mountain))
        
       