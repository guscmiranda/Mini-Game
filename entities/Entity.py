import pygame
from core.transformacoes import (
    translacao,
    rotacao_central,
    escalonamento_central
)

class Entity:

    def __init__(self, partes, cores, centro=(0, 0)):
        """
        partes = dicionário de partes da entidade
        cores = dicionário de cores das partes
        centro = ponto central da entidade
        """

        self.partes = partes
        self.cores = cores
        self.cx, self.cy = centro
        self.angulo = 0

    def mover(self, dx, dy):

        for nome, parte in self.partes.items():
            objeto = parte[0]
            tipo = parte[1]

            if tipo == "polygon":
                self.partes[nome][0] = translacao(objeto, dx, dy)

            elif tipo == "circle":

                centro = objeto["centro"]

                novo_centro = translacao([centro], dx, dy)[0]

                self.partes[nome][0]["centro"] = novo_centro

        self.cx += dx
        self.cy += dy

    def rotacionar(self, angulo):
        self.angulo += angulo
        for nome, parte in self.partes.items():

            objeto = parte[0]
            tipo = parte[1]

            if tipo == "polygon":
                self.partes[nome][0] = rotacao_central(
                    objeto,
                    angulo,
                    self.cx,
                    self.cy
                )

            elif tipo == "circle":

                centro = objeto["centro"]

                novo_centro = rotacao_central(
                    [centro],
                    angulo,
                    self.cx,
                    self.cy
                )[0]

                self.partes[nome][0]["centro"] = novo_centro

    def escalar(self, sx, sy):

        for nome, parte in self.partes.items():

            objeto = parte[0]
            tipo = parte[1]

            if tipo == "polygon":

                self.partes[nome][0] = escalonamento_central(
                    objeto,
                    sx,
                    sy,
                    self.cx,
                    self.cy
                )

            elif tipo == "circle":

                centro = objeto["centro"]

                novo_centro = escalonamento_central(
                    [centro],
                    sx,
                    sy,
                    self.cx,
                    self.cy
                )[0]

                self.partes[nome][0]["centro"] = novo_centro
                self.partes[nome][0]["raio"] *= (sx + sy) / 2

    def draw(self, screen):

        for nome, parte in self.partes.items():

            objeto = parte[0]
            tipo = parte[1]

            cor_interior = self.cores[nome]["interior"]
            cor_borda = self.cores[nome]["borda"]

            if tipo == "polygon":

                pygame.draw.polygon(screen, cor_interior, objeto)
                pygame.draw.polygon(screen, cor_borda, objeto, 3)

            elif tipo == "circle":

                centro = objeto["centro"]
                raio = objeto["raio"]

                pygame.draw.circle(
                    screen,
                    cor_interior,
                    (int(centro[0]), int(centro[1])),
                    raio
                )

                pygame.draw.circle(
                    screen,
                    cor_borda,
                    (int(centro[0]), int(centro[1])),
                    raio,
                    3
                )

    def update(self, dt):
        pass
