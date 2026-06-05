from entities.Entity import Entity


class ParedeLaser(Entity):
    '''
    A parede surge fora da tela e realiza uma
    varredura horizontal da direita para a esquerda. Quando sai
    completamente da área visível do jogo, é apagada.
    '''

    def __init__(self, partes, cores, centro, partes_criticas):
        super().__init__(partes, cores, centro, partes_criticas)
        self.velocidade = 350  # Velocidade da varredura

        # Posiciona a entidade no ponto inicial
        x, y = centro
        self.mover(x, y)

    def update(self, dt):
        # Move para a esquerda sempre
        self.mover(-self.velocidade * dt, 0)

        # Quando a parede já passou completamente pela tela marca a entidade para remoção
        if self.cx < -200:
            self.alive = False