import pygame

from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):

    def __init__(self, x: float, y: float, radius: float = PLAYER_RADIUS):
        super().__init__(x, y, radius)

        self.rotation: int = 0
        self.shoot_timer: float = 0.0

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
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.shoot_timer -= dt

    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self) -> None:
        if self.shoot_timer >= 0:
            return
        else:
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot: Shot = Shot(self.position.x, self.position.y)
        shot.velocity: pygame.Vector2 = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED