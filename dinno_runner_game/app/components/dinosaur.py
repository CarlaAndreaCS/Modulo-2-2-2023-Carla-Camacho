
import pygame
from app.utils.constants import RUNNINGANIMADO, JUMPINGANIMADO, DUCKINGANIMADO
from pygame.sprite import Sprite #Para usar el dinosaurio como Sprite tenemos que importar la clase Sprite

class Dinosaur(Sprite): #La clase dinosaurio hereda la clase Sprite de Pygame
    x_pos = 80  #Posiciones del dinosaurio
    y_pos = 310
    y_pos_DUCKING = 345 #Posicion del dinosaurio cuando se agacha, mas abajo 
    JUMP_VEL = 9 #Velocidad del dinosaurio desde que deja el camino 

    def __init__(self):
        
        self.run_img = RUNNINGANIMADO
        self.duck_img = DUCKINGANIMADO
        self.jump_img = JUMPINGANIMADO

        self.image = self.run_img[0] #Imagen inicial del Sprite
        self.dino_rect = self.image.get_rect() #Posicionamos el Sprite. 
        self.dino_rect.x = self.x_pos    #Se pasan las nuevas coordenadas en X y Y
        self.dino_rect.y = self.y_pos
        self.step = 0  #Realiza iteraciones, empieza en 0, cuando empieza el juego #Se usa para realizar el intercambio de imagenes
        self.jump_vel = self.JUMP_VEL

        
        self.dino_running = True   #Estados del dinosaurio iniciales
        self.dino_ducking = False
        self.dino_jumping = False

        self.sonidoJump = pygame.mixer.Sound("Jump.wav")
        self.sonidoDuck = pygame.mixer.Sound("Duck.wav")
 

    def update(self, user_input):
        
        if self.dino_running:
            self.run()
        elif self.dino_ducking:
            self.duck()
        elif self.dino_jumping:
            self.jump()

        if user_input[pygame.K_DOWN] and not self.dino_jumping:
            self.sonidoDuck.play()
            self.dino_running = False   
            self.dino_ducking = True
            self.dino_jumping = False

        elif user_input[pygame.K_UP] and not self.dino_jumping:
            self.sonidoJump.play()
            self.dino_running = False   
            self.dino_ducking = False
            self.dino_jumping = True

        elif not self.dino_jumping:
            self.dino_running = True   
            self.dino_ducking = False
            self.dino_jumping = False
       
       
        if self.step >= 10: 
            self.step = 0

    
    def run(self):
        self.dino_rect = self.image.get_rect() #Despues de cambiar la imagen en run, posicionamos al dinosaurio
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
        self.step = self.step + 1 #El indice va aumentando en 1 cada vez que se llama al metodo run, de 1 a 10
        
        if self.step < 5:
            self.image = RUNNINGANIMADO[0] 
        else: 
            self.image = RUNNINGANIMADO[1] #Cuando step_index sea menor a 5, reproduce la primer imagen de running, cuando sea mayor a 5 reproduce la siguiente imagen de running
       
    def duck(self):
        
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos_DUCKING
        self.step = self.step + 1

        if self.step < 5:     #Hacemos lo mismo que en running
           self.image = DUCKINGANIMADO[0] 
        else:
           self.image = DUCKINGANIMADO[1]

    def jump(self):
        self.image = self.jump_img
        if self.dino_jumping:
            self.dino_rect.y = self.dino_rect.y - self.jump_vel *5 #salto, la posicion en y va disminuyendo, conforme la velocidad del salto, definida abajo
            self.jump_vel = self.jump_vel - 1 #salto, cuando llega al punto maximo, baja. Disminuyendo la velocidad. Sirve para medir la velocidad con la que baja, se va volando
        if self.jump_vel <- self.JUMP_VEL: #Cuando llega a JUMP_VEL en negativo, este se detiene y llega a la posicion inicial en y
            self.dino_rect.y = self.y_pos
            self.dino_jumping = False     #Para que vuelva a correr, y no se quede en el estado de salto
            self.jump_vel = self.JUMP_VEL
        
    
    def draw(self, screen):
        screen.blit(self.image, self.dino_rect)

