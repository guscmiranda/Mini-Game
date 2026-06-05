from math import cos
from math import sin
import math

def translacao(pontos, dx, dy):
    ''' Função para movimentar os pontos de lugar '''
    novos = []
    for x, y in pontos: novos.append((x + dx, y + dy)) # Soma dx e dy para movimentar
    return novos

def rotacao_central(pontos, theta, dx, dy):
    ''' Multiplicando as matrizes de translação para o centro
        com a de rotação e com a de translação para a posição incial
        obtemos as expressões para o x_new e para o y_new
    '''
    theta = math.radians(theta)

    novos = []

    for x, y in pontos:
        x_new = (
                x * math.cos(theta)
                - y * math.sin(theta)
                + dx * (1 - math.cos(theta))
                + dy * math.sin(theta)
        )
        y_new = (
                x * math.sin(theta)
                + y * math.cos(theta)
                + dy * (1 - math.cos(theta))
                - dx * math.sin(theta)
        )
        novos.append((x_new,y_new))

    return novos


def escalonamento_central(pontos, sx, sy, cx, cy):
    ''' Função para redimensionar os pontos'''
    novos = []

    for x, y in pontos:
        # Subtrai o centro, aplica a escala e soma o centro de volta
        x_new = (x - cx) * sx + cx
        y_new = (y - cy) * sy + cy
        novos.append((x_new, y_new))

    return novos
