from entities.Entity import Entity
import copy
import math

class Projectile(Entity):

    def __init__(self, partes, cores, x, y, angulo, partes_criticas=[]):
        '''
        O projétil se desloca em linha reta seguindo o ângulo
        informado no momento da criação e é removido quando sai
        da área visível do jogo.
        '''

        # Cria cópias independentes para evitar compartilhamento entre diferentes projéteis e causar problemas
        super().__init__(copy.deepcopy(partes), copy.deepcopy(cores), (x,y), partes_criticas)

        self.velocidade = 500
        self.angulo = angulo # Angulo entre a sua inicialização e o jogador no momento em que foi criado
        self.mover(x, y) # Inicializa sua posição inicial no Robô

    def update(self, dt):

        # Converte o ângulo de graus para radianos (pelas funções trigonométricas)
        rad = math.radians(self.angulo)

        # Calcula o deslocamento horizontal e vertical com base no ângulo de disparo
        dx = math.sin(rad) * self.velocidade * dt
        dy = -math.cos(rad) * self.velocidade * dt

        self.mover(dx, dy)

        # Remove se sair da tela
        if self.cy < -20:
            self.alive = False