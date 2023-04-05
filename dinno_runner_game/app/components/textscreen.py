import pygame

COLORS = {
    "soft": (255,255,153)
}

class TextScreen: 
     
      FONT_STYLE = "C:\Windows\Fonts\JOKERMAN.ttf"

     #def __init__(self, text):
     
      def name(self):
          font = pygame.font.Font(self.FONT_STYLE, 20)
          text = font.render("Dinosaur Name: Carla", True, COLORS["soft"] )
          text_rect = text.get_rect()
          text_rect.center = (125, 40) #Posiciones en X y Y
          return text, text_rect

      def obstacles_not_done(self, obstacles_not_done): 
          font = pygame.font.Font(self.FONT_STYLE, 20)
          text = font.render("Obstaculos no logrados: " + str(obstacles_not_done) , True, COLORS["soft"])
          text_rect = text.get_rect()
          text_rect.center = (145, 70)
          return text, text_rect
     
      def obstacles_done(self, obstacles_done): 
          font = pygame.font.Font(self.FONT_STYLE, 20)
          text = font.render("Obstaculos logrados: " + str(obstacles_done), True, COLORS["soft"])
          text_rect = text.get_rect()
          text_rect.center = (140, 100)
          return text, text_rect
     
