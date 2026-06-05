from entities.Entity import Entity
from entities.Projectile import Projectile
from models.spaceship_ray import *
from models.player_lives import *
import pygame
import math

class Spaceship(Entity):
    '''
   A nave controlada pelo jogador, mantém informações de vida, cooldowns
   e estados necessários para o controle do jogador.
   '''

    def __init__(self, partes, cores,  centro=(0, 0), partes_criticas=[]):
        super().__init__(partes, cores, centro, partes_criticas)

        self.velocidade = 300
        self.vidas = 5

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
        '''
       Cria e retorna um novo projétil.

       O projétil nasce alguns pixels à frente da nave,
       seguindo sua direção atual.
       '''

        rad = math.radians(self.angulo)

        # Distância entre o centro da nave e o ponto onde o projétil será criado.
        offset = 100

        x = self.cx + math.sin(rad) * offset
        y = self.cy - math.cos(rad) * offset

        # Cria os tiros
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
        '''
        Processa todas as entradas do teclado.

        Controla: Movimento, Rotação, Transformação de tamanho
        '''

        velocidade = self.velocidade * dt
        keys = pygame.key.get_pressed()
        # Mover para cima
        if keys[pygame.K_w]:
            self.mover(0, -velocidade)
        # Mover para esquerda
        if keys[pygame.K_a]:
            self.mover(-velocidade, 0)
        # Mover para baixo
        if keys[pygame.K_s]:
            self.mover(0, velocidade)
        # Mover para direita
        if keys[pygame.K_d]:
            self.mover(velocidade, 0)
        # Girar para esquerda
        if keys[pygame.K_j]:
            self.rotacionar(-200*dt)
        # Girar para direita
        if keys[pygame.K_k]:
            self.rotacionar(200*dt)
        # Diminuir ou aumentar a nave
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
        '''
       Atualiza o estado da nave a cada frame.

       Responsável por: Verificar se a nave morreu, processar entradas do jogador,
       atualizar temporizadores internos
       '''

        # Se acabarem as vidas ele morre
        if self.vidas <= 0: self.alive = False

        self.handle_input(dt)
        # Incrementa os tempos
        self.time_since_last_shot += dt
        self.time_since_last_mini += dt
        self.time_since_last_damage += dt


