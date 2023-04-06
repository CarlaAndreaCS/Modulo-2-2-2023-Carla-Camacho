import pygame
from app.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

COLORS = {
    "soft": (255,255,153),
    "softorange": (255,102,0),
    "black": (0,0,0)
}

class TextScreen: 
     
      FONT_STYLE = "C:\Windows\Fonts\JOKERMAN.ttf"

     #def __init__(self, text):
     
      def name(self, game):
          font = pygame.font.Font(self.FONT_STYLE, 20)
          text = font.render("Dinosaur Name: " + game.Dinosaurio.name, True, COLORS["soft"] )
          text_rect = text.get_rect()
          text_rect.center = (165, 40) #Posiciones en X y Y
          return text, text_rect

      def cactus_not_done(self, cactus_not_done): 
          font = pygame.font.Font(self.FONT_STYLE, 20)
          text = font.render("Cactus no logrados: " + str(cactus_not_done) , True, COLORS["soft"])
          text_rect = text.get_rect()
          text_rect.center = (155, 70)
          return text, text_rect
     
      def cactus_done(self, cactus_done): 
          font = pygame.font.Font(self.FONT_STYLE, 20)
          text = font.render("Cactus logrados: " + str(cactus_done), True, COLORS["soft"])
          text_rect = text.get_rect()
          text_rect.center = (140, 100)
          return text, text_rect
      
      def birds_not_done(self, birds_not_done): 
          font = pygame.font.Font(self.FONT_STYLE, 20)
          text = font.render("Aves no logradas: " + str(birds_not_done) , True, COLORS["soft"])
          text_rect = text.get_rect()
          text_rect.center = (500, 40)
          return text, text_rect
     
      def birds_done(self, birds_done): 
          font = pygame.font.Font(self.FONT_STYLE, 20)
          text = font.render("Aves logradas: " + str(birds_done), True, COLORS["soft"])
          text_rect = text.get_rect()
          text_rect.center = (500, 70)
          return text, text_rect
      
      def menu_message(self, message):
           font = pygame.font.Font(self.FONT_STYLE, 30)
           text = font.render(message, True, COLORS["softorange"])
           text_rect = text.get_rect()
           text_rect.center = (550, 100)
           return text, text_rect
      
      def menu_message_two(self, message):
           font = pygame.font.Font(self.FONT_STYLE, 30)
           text = font.render(message, True, COLORS["softorange"])
           text_rect = text.get_rect()
           text_rect.center = (550, 200)
           return text, text_rect
      
      def score(self, points):
          font = pygame.font.Font(self.FONT_STYLE, 20)
          text = font.render("Points: " + str(points), True, COLORS["soft"])
          text_rect = text.get_rect()
          text_rect.center = (800, 50)
          return text, text_rect
     
