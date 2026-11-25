import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED

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

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        # if keys[pygame.K_w]:
        #     # ?
        # if keys[pygame.K_s]:
        #     # ?