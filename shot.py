import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH

class Shot(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)
    
    def draw(self, surface: pygame.Surface):
        pygame.draw.circle(surface, "red", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float):
        # Update the shot's position or state here if needed
        self.position += self.velocity * dt