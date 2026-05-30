from entities.Entity import Entity
from entities.Projectile import Projectile
from models.spaceship_ray import *
from models.player_lives import *
import pygame
import math

class Spaceship(Entity):
    def __init__(self, partes, cores,  centro=(0, 0), partes_criticas=[]):
        super().__init__(partes, cores, centro, partes_criticas)

        self.velocidade = 300
        self.vidas = 3

        self.cooldown_tiro = 0.35
        self.time_since_last_shot = 0

        self.cooldown_damage = 0.5
        self.time_since_last_damage = 0

        self.heart_partes = heart_partes
        self.heart_cores = heart_cores

        self.isBig = True
        self.time_since_last_mini = 0
        self.cd_mini = 2
        self.f_pressed = False

        self.mover(600, 600)

    def shoot(self, partes_criticas):

        rad = math.radians(self.angulo)

        offset = 100

        x = self.cx + math.sin(rad) * offset
        y = self.cy - math.cos(rad) * offset

        tiro = Projectile(
            tiro_partes,
            tiro_cores,
            x,
            y,
            self.angulo,
            partes_criticas
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

        if keys[pygame.K_f] and not self.f_pressed:
            if self.isBig and self.time_since_last_mini > self.cd_mini:
                self.escalar(0.5, 0.5)
                self.isBig = False
                self.time_since_last_mini = 0
            elif not self.isBig:
                self.escalar(2, 2)
                self.isBig = True

            self.f_pressed = True

        if not keys[pygame.K_f]:
            self.f_pressed = False

    def update(self, dt):

        if self.vidas <= 0: self.alive = False

        self.handle_input(dt)
        self.time_since_last_shot += dt
        self.time_since_last_mini += dt
        self.time_since_last_damage += dt


