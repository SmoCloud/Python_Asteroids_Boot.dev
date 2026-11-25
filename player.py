import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH

class Player(CircleShape):

    def __init__(self, x: float, y: float, radius: float = PLAYER_RADIUS):
        super().__init__(x, y, radius)

        self.rotation: int = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward: float = pygame.Vector2(0, 1).rotate(self.rotation)
        right: float = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a: float = self.position + forward * self.radius
        b: float = self.position - forward * self.radius - right
        c: float = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, surface: pygame.Surface):
        pygame.draw.polygon(surface, "white", self.triangle(), LINE_WIDTH)