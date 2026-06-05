import random

from entities.Entity import Entity
import copy
import math

class Bomb(Entity):
    '''
    Inimigo do tipo bomba.
    Após ser criado, surge fora da tela em uma posição aleatória
    e passa a perseguir continuamente o jogador.
    Quando sua vida chega a zero, a entidade é marcada para remoção.
    '''

    def __init__(self, partes, cores, centro=(0,0), partes_criticas=[]):

        # Cria cópias para evitar que múltiplas bombas compartilhem as mesmas estruturas.
        super().__init__(
            copy.deepcopy(partes),
            copy.deepcopy(cores),
            centro,
            partes_criticas
        )

        self.vida = 1

        self.velocidade = 230

        # Controle de temporizador para futuras explosões
        self.bomb_timer = 0
        self.bomb_cooldown = 8

        # Escolha de uma posição inicial fora da tela
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

        # Move a entidade para sua posição inicial
        self.mover(x, y)

    def seguir_player(self, player, dt):
        '''
        Calcula o vetor direção até o jogador,
        normaliza esse vetor e movimenta a entidade
        mantendo velocidade constante
        '''

        # Vetor da bomba até o jogador
        dx = player.cx - self.cx
        dy = player.cy - self.cy

        # Distância entre os dois objetos
        distancia = math.hypot(dx, dy)

        if distancia == 0:
            return

        # Normalizando
        dx /= distancia
        dy /= distancia

        self.mover( # Movimento na direção do jogador
            dx * self.velocidade * dt,
            dy * self.velocidade * dt
        )


    def update(self, dt, player):
        '''
        Verifica se a entidade ainda está viva e
        executa sua lógica de movimentação.
        '''

        # Marca a entidade para remoção quando sua vida acaba
        if self.vida <= 0: self.alive = False

        # Persegue continuamante !!
        self.seguir_player(player, dt)