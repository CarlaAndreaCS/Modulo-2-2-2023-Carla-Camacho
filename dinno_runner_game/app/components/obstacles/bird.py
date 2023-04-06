import random
from app.components.obstacles.obstacle import Obstacle
from app.utils.constants import BIRD


class Bird(Obstacle):
    BIRD_HEIGHTS = [280, 250, 270, 100, 50]

    def __init__(self, image_list):
        self.obstacle_type = 0
        super().__init__(image_list, self.obstacle_type)
        self.rect.y = random.choice(self.BIRD_HEIGHTS)
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 10:
            self.index = 0
        
        self.index = self.index + 1

        if self.index < 5:
            self.image_list = BIRD[0] 
        else: 
            self.image_list = BIRD[1]

        SCREEN.blit(self.image_list, self.rect)
        
        