import pygame
import random

from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, surface: pygame.Surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        # Update the asteroid's position or state here if needed
        self.position += self.velocity * dt

    def split(self) -> None:
        # Implementation for splitting the asteroid
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            old_radius = self.radius
            asteroid1_velocity = self.velocity.rotate(angle)
            asteroid2_velocity = self.velocity.rotate(-angle)
            asteroid1 = Asteroid(self.position.x, self.position.y, old_radius - ASTEROID_MIN_RADIUS)
            asteroid2 = Asteroid(self.position.x, self.position.y, old_radius - ASTEROID_MIN_RADIUS)
            asteroid1.velocity = asteroid1_velocity * 1.2
            asteroid2.velocity = asteroid2_velocity * 1.2
