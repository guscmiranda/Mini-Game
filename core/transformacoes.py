from math import cos
from math import sin
import math

def translacao(pontos, dx, dy):
    novos = []
    for x, y in pontos: novos.append((x + dx, y + dy))
    return novos

def escalonamento(pontos, sx, sy):
    novos = []
    for x, y in pontos:
        novos.append((x * sx, y * sy))
    return novos

def rotacao_00 (pontos, theta):
    novos = []

    for x,y in pontos:
        x_new = x * cos(theta) - y * sin(theta)
        y_new = x * sin(theta) - y * cos(theta)
        #xs_novos.append(x_new)
        #ys_novos.append(y_new)
        novos.append((x_new, y_new))

    return novos

def rotacao_central(pontos, theta, dx, dy):

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
    novos = []

    for x, y in pontos:
        # Subtrai o centro, aplica a escala e soma o centro de volta
        x_new = (x - cx) * sx + cx
        y_new = (y - cy) * sy + cy
        novos.append((x_new, y_new))

    return novos
