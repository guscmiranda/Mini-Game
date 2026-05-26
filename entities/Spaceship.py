from entities.Entity import Entity
from entities.Projectile import Projectile
from models.spaceship_ray import *
import pygame
import math

class Spaceship(Entity):
    def __init__(self, partes, cores,  centro=(0, 0)):
        super().__init__(partes, cores, centro)

        self.velocidade = 300
        self.vidas = 3 # TODO: a decidir

        self.cooldown_tiro = 0.35
        self.time_since_last_shot = 0

        self.mover(600, 600)

    def shoot(self):

        rad = math.radians(self.angulo)

        offset = 100

        x = self.cx + math.sin(rad) * offset
        y = self.cy - math.cos(rad) * offset

        tiro = Projectile(
            tiro_partes,
            tiro_cores,
            x,
            y,
            self.angulo
        )
        return tiro


    def handle_input(self, dt):
        velocidade = self.velocidade * dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.mover(0, -velocidade)
        if keys[pygame.K_a]:
            self.mover(-velocidade, 0)
        if keys[pygame.K_s]:
            self.mover(0, velocidade)
        if keys[pygame.K_d]:
            self.mover(velocidade, 0)

        if keys[pygame.K_q]:
            self.rotacionar(-180*dt)
        if keys[pygame.K_e]:
            self.rotacionar(180*dt)

    def update(self, dt):
        self.handle_input(dt)
        self.time_since_last_shot += dt


