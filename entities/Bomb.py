import random

from entities.Entity import Entity
import copy
import math

class Bomb(Entity):

    def __init__(self, partes, cores, centro=(0,0), partes_criticas=[]):

        super().__init__(
            copy.deepcopy(partes),
            copy.deepcopy(cores),
            centro,
            partes_criticas
        )

        self.vida = 2

        self.velocidade = 100

        # estados
        self.entering = True

        # direção vertical
        self.vertical_direction = 1

        y = random.randint(1, 720)
        # começa fora da tela
        self.mover(1600, y)

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

        if self.entering:
            self.entrada(dt)

        else:
            self.seguir_player(player)