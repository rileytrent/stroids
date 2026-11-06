from typing import override
from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH
import pygame


class Shot(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius=SHOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        return pygame.draw.circle(
            screen, "white", self.position, self.radius, LINE_WIDTH
        )

    @override
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
