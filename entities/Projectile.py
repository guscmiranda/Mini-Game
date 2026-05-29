from entities.Entity import Entity
import copy
import math

class Projectile(Entity):

    def __init__(self, partes, cores, x, y, angulo, partes_criticas=[]):
        super().__init__(copy.deepcopy(partes), copy.deepcopy(cores), (x,y), partes_criticas)

        self.velocidade = 500
        # self.alive = True
        self.angulo = angulo
        self.mover(x, y)

    def update(self, dt):

        # self.mover(
        #     0,
        #     -self.velocidade * dt
        # )

        rad = math.radians(self.angulo)

        dx = math.sin(rad) * self.velocidade * dt
        dy = -math.cos(rad) * self.velocidade * dt

        self.mover(dx, dy)

        # remove se sair da tela
        if self.cy < -20:
            self.alive = False