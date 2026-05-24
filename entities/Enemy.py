from entities.Entity import Entity
import pygame

class Spaceship(Entity):
    def __init__(self, partes, cores,  centro=(0, 0)):
        super().__init__(partes, cores, centro=(0, 0)) # em criação esse trem

        self.velocidade = 300
        self.vidas = 3 # TODO: a decidir

        self.cooldown_tiro = 0.2
        self.time_sinse_last_shot = 0

        self.mover(600, 600)

    def movement(self, dt):
        velocidade = self.velocidade * dt
        if keys[pygame.K_w]:
            self.mover(0, -velocidade)
        if keys[pygame.K_a]:
            self.mover(-velocidade, 0)
        if keys[pygame.K_s]:
            self.mover(0, velocidade)
        if keys[pygame.K_d]:
            self.mover(velocidade, 0)
        if keys[pygame.K_q]:
            self.rotacionar(-2)
        if keys[pygame.K_e]:
            self.rotacionar(2)

    def update(self, dt):
        self.handle_input(dt)
        #self.aplicar_transformacoes() # TODO: aparentemente vamos tratar como 3 funções diferentes então tem q atualizar isso


