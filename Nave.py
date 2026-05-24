import pygame
# from main import WIDTH, HEIGHT
from core.transformacoes import *
pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# nave = {
#     'corpo': []
#     ''
# }

# Corpo triangular
corpo = [
    (0, -100),
    (-60, 60),
    (60, 60)
]

# Asa esquerda
asa_esq = [
    (-60, 60),
    (-110, 120),
    (-40, 120)
]

# Asa direita
asa_dir = [
    (60, 60),
    (40, 120),
    (110, 120)
]

# Motor
motor = [
    (-15, 60),
    (15, 60),
    (25, 95),
    (-25, 95)
]

# Janela
janela = [(0, -10)]
janela_raio = 20


# mover nave para centro da tela
def mover_objeto(objeto, dx, dy):
    return [(x + dx, y + dy) for x, y in objeto]


corpo = mover_objeto(corpo, WIDTH//2, HEIGHT//2)
asa_esq = mover_objeto(asa_esq, WIDTH//2, HEIGHT//2)
asa_dir = mover_objeto(asa_dir, WIDTH//2, HEIGHT//2)
motor = mover_objeto(motor, WIDTH//2, HEIGHT//2)
janela = mover_objeto(janela, WIDTH//2, HEIGHT//2)

running = True

while running:

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # TRANSLAÇÃO
    if keys[pygame.K_w]:
        corpo = translacao(corpo, 0, -5)
        asa_esq = translacao(asa_esq, 0, -5)
        asa_dir = translacao(asa_dir, 0, -5)
        motor = translacao(motor, 0, -5)
        janela = translacao(janela, 0, -5)

    if keys[pygame.K_s]:
        corpo = translacao(corpo, 0, 5)
        asa_esq = translacao(asa_esq, 0, 5)
        asa_dir = translacao(asa_dir, 0, 5)
        motor = translacao(motor, 0, 5)
        janela = translacao(janela, 0, 5)

    if keys[pygame.K_a]:
        corpo = translacao(corpo, -5, 0)
        asa_esq = translacao(asa_esq, -5, 0)
        asa_dir = translacao(asa_dir, -5, 0)
        motor = translacao(motor, -5, 0)
        janela = translacao(janela, -5, 0)

    if keys[pygame.K_d]:
        corpo = translacao(corpo, 5, 0)
        asa_esq = translacao(asa_esq, 5, 0)
        asa_dir = translacao(asa_dir, 5, 0)
        motor = translacao(motor, 5, 0)
        janela = translacao(janela, 5, 0)

    # ROTAÇÃO
    if keys[pygame.K_q]:
        cx, cy = janela[0]
        corpo = rotacao_central(corpo, -2, cx, cy)
        asa_esq = rotacao_central(asa_esq, -2, cx, cy)
        asa_dir = rotacao_central(asa_dir, -2, cx, cy)
        motor = rotacao_central(motor, -2, cx, cy)
        janela = rotacao_central(janela, -2, cx, cy)

    if keys[pygame.K_e]:
        cx, cy = janela[0]
        corpo = rotacao_central(corpo, 2, cx, cy)
        asa_esq = rotacao_central(asa_esq, 2, cx, cy)
        asa_dir = rotacao_central(asa_dir, 2, cx, cy)
        motor = rotacao_central(motor, 2, cx, cy)
        janela = rotacao_central(janela, 2, cx, cy)

    if keys[pygame.K_f]:
        cx, cy = janela[0]
        v = 0.6
        corpo = escalonamento_central(corpo, v, v, cx, cy)
        asa_esq = escalonamento_central(asa_esq, v, v, cx, cy)
        asa_dir = escalonamento_central(asa_dir, v, v, cx, cy)
        motor = escalonamento_central(motor, v, v, cx, cy)
        janela_raio *= 0.6 #escalonamento_central(janela, v, v, cx, cy)

    if keys[pygame.K_g]:
        cx, cy = janela[0]
        v = 1.6
        corpo = escalonamento_central(corpo, v, v, cx, cy)
        asa_esq = escalonamento_central(asa_esq, v, v, cx, cy)
        asa_dir = escalonamento_central(asa_dir, v, v, cx, cy)
        motor = escalonamento_central(motor, v, v, cx, cy)
        janela_raio *= 1.6 #escalonamento_central(janela, v, v, cx, cy)

    screen.fill("black")

    pygame.draw.polygon(screen, (120, 120, 120), corpo) # Se precisar deixar mais suave [(int(x), int(y)) for x,y in corpo]
    pygame.draw.polygon(screen, (180, 0, 20), asa_esq)
    pygame.draw.polygon(screen, (180, 0, 20), asa_dir)
    pygame.draw.polygon(screen, (180, 0, 20), motor)

    pygame.draw.polygon(screen, (120, 0, 0), corpo, 4)

    pygame.draw.circle(screen, (150, 240, 255),
                       (int(janela[0][0]), int(janela[0][1])),
                       janela_raio)

    pygame.draw.circle(screen, (120, 0, 0),
                       (int(janela[0][0]), int(janela[0][1])),
                       janela_raio, 4)

    pygame.display.flip()

pygame.quit()