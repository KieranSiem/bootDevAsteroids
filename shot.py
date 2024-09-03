import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, ammo_type):
        super().__init__(x, y, self.get_shot_radius(ammo_type))
    
    def get_shot_radius(self, ammo_type):
        match ammo_type:
            case "normal":
                return NORMAL_SHOT_RADIUS
            case "big":
                return BIG_SHOT_RADIUS
            case "bigger":
                return BIGGER_SHOT_RADIUS
            case "cheating":
                return CHEATING_SHOT_RADIUS
            
        return NORMAL_SHOT_RADIUS

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
