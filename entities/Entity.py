import pygame
from core.transformacoes import (
    translacao,
    rotacao_central,
    escalonamento_central
)
import math
import copy

def gerar_circulo_envolvente(pontos):
    min_x = min(p[0] for p in pontos)
    max_x = max(p[0] for p in pontos)
    min_y = min(p[1] for p in pontos)
    max_y = max(p[1] for p in pontos)

    cx = (min_x + max_x) / 2
    cy = (min_y + max_y) / 2

    raio = 0
    for x, y in pontos:
        dist = math.hypot(x-cx, y-cy)
        if dist > raio:
            raio = dist

    return {"centro": (cx, cy), "raio": raio}


class Entity:

    def __init__(self, partes, cores, centro=(0, 0), partes_criticas=[]):
        """
        partes = dicionário de partes da entidade
        cores = dicionário de cores das partes
        centro = ponto central da entidade
        """

        self.partes = copy.deepcopy(partes)
        self.cores = copy.deepcopy(cores)
        self.cx, self.cy = centro
        self.angulo = 0

        self.hitboxes = []
        for nome in partes_criticas:
            if nome in self.partes:
                objeto = self.partes[nome][0]
                tipo = self.partes[nome][1]

                if tipo == "polygon":
                    self.hitboxes.append(gerar_circulo_envolvente(objeto))
                elif tipo == "circle":
                    # Se já for um círculo, só copia o centro e o raio
                    self.hitboxes.append({"centro": objeto["centro"], "raio": objeto["raio"]})

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

        for hb in self.hitboxes:
            hb["centro"] = translacao([hb["centro"]], dx, dy)[0]

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

        for hb in self.hitboxes:
            hb["centro"] = escalonamento_central([hb["centro"]], sx, sy, self.cx, self.cy)[0]
            hb["raio"] *= (sx + sy) / 2

    def draw(self, screen, ver_hitboxes=False):
        if not self.alive: return

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

        if ver_hitboxes:
            for hb in self.hitboxes:
                pygame.draw.circle(
                    screen,
                    (0, 255, 0),  # Verde limão
                    (int(hb["centro"][0]), int(hb["centro"][1])),
                    int(hb["raio"]),
                    1
                )

    def update(self, dt):
        pass
