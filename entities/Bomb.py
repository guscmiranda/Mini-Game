import random

from entities.Entity import Entity
import copy
import math

class Bomb(Entity):

    def __init__(self, partes, cores, centro=(0,0), partes_criticas=[], rand_init=False):

        super().__init__(
            copy.deepcopy(partes),
            copy.deepcopy(cores),
            centro,
            partes_criticas
        )

        self.vida = 1

        self.velocidade = 170

        self.bomb_timer = 0
        self.bomb_cooldown = 8

        # estados
        self.entering = True

        # direção vertical
        self.vertical_direction = 1

        if rand_init:
            side = random.choice(['top', 'bottom', 'left', 'right'])

            if side == 'top':
                x = random.randint(0, 1280)
                y = random.randint(-100, -20)
                x = random.randint(0, 1280)
                y = random.randint(740, 820)
            elif side == 'left':
                x = random.randint(-100, -20)
                y = random.randint(0, 720)
            else:  # right
                x = random.randint(1300, 1380)
                y = random.randint(0, 720)
        else:
            x, y = 1600, 360

        self.mover(x, y)

    def entrada(self, dt):

        alvo_x = 1200

        if self.cx > alvo_x:

            self.mover(
                -(self.velocidade-40) * dt,
                0
            )

        else:
            self.entering = False

    def seguir_player(self, player, dt):

        dx = player.cx - self.cx
        dy = player.cy - self.cy

        distancia = math.hypot(dx, dy)

        if distancia == 0:
            return

        dx /= distancia
        dy /= distancia

        self.mover(
            dx * self.velocidade * dt,
            dy * self.velocidade * dt
        )


    def update(self, dt, player):
        if self.vida <= 0: self.alive = False

        # if self.entering:
        #     self.entrada(dt)
        #
        # else:
        self.seguir_player(player, dt)