from entities.Entity import Entity


class ParedeLaser(Entity):
    def __init__(self, partes, cores, centro, partes_criticas):
        super().__init__(partes, cores, centro, partes_criticas)
        self.velocidade = 350  # Velocidade da varredura

        x, y = centro
        self.mover(x, y)

    def update(self, dt):
        # Move para a esquerda
        self.mover(-self.velocidade * dt, 0)

        # Se saiu totalmente da tela, morre para liberar memória
        if self.cx < -200:
            self.alive = False