from pygame.sprite import Sprite
from pygame.image import load
from pygame.event import get
from pygame import K_UP, KEYDOWN, K_LEFT, K_RIGHT, K_SPACE
from pygame import display, init, transform
from time import sleep

walking_images = ["assets/mario-run-1.png", "assets/mario-run-2.png", "assets/mario-run-3.png"]


class Mario(Sprite):
    mario_speed = 4
    idle_image = transform.scale_by(load("assets/mario-idle.png"), 0.3)
    jump_image = transform.scale_by(load("assets/mario-jump.png"), 0.3)

    def __init__(self, initial_x, initial_y, pos=None):
        super().__init__()
        self.index = 0
        self.images = [transform.scale_by(load(image), 0.3) for image in walking_images]
        self.image = self.idle_image
        self.rect = self.image.get_rect()
        self.rect.x = initial_x
        self.rect.y = initial_y
        self.counter = 0

    def update_walk(self):
        # Update the actor's image
        self.counter += 1
        if self.counter >= 1:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]

    def update_jump(self):
        self.image = self.jump_image

    def set_idle_image(self):
        self.image = self.idle_image

    
