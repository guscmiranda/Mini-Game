import pygame

from GameStates import GameState
from entities.Spaceship import Spaceship
from entities.FinalBoss import FinalBoss
from models.spaceship_ray import *
from models.final_boss import  *
from models.spaceship import *
# from models.boss_teste import *
from models.parede_laser import *
from entities.ParedeLaser import ParedeLaser
from entities.Entity import Entity
from core.AudioManager import AudioManager
from core.BackgroundManager import BackgroundManager
from models.bomb import *
from entities.Bomb import Bomb

import random
import math

WIDTH = 1280

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, 720)) # Cria a janela
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()  # Para lidar com quais botões serão pressionados

        # Fontes
        self.fonte_titulo = pygame.font.SysFont('cooperblack', 100)
        self.fonte_subtitulo = pygame.font.SysFont('cooperblack', 40)

        self.state = GameState.IN_GAME
        self.running = True

        # Mídia e Audio
        self.audio = AudioManager()
        self.background = BackgroundManager("../assets/image/dark_montains.png", "../assets/image/dark_montains_cont.png")

        # Criando a nave e o boss
        self.player = Spaceship(spaceship_partes, spaceship_cores, centro=(0,0), partes_criticas=["corpo"])
        self.final_boss = FinalBoss(boss9_partes, boss9_cores, centro=(0,0), partes_criticas=["cabeca", "tronco"])
        self.final_boss.alive = False

        # listas de inimigos e projéteis
        self.enemies = []
        self.p_projectiles = []
        self.b_projectiles = []
        self.paredes = []
        self.bombs = []

        # Condições de vida das bombas
        self.bomb_timer = 0
        self.bomb_cooldown = 2

        # Variáveis para as fases
        self.fase_atual = 1
        self.tempo_fase = 0

        # Variáveis de Transição
        self.tempo_transicao = 0
        self.texto_transicao = ""

        self.audio.play_music("fase-1")

    def handle_events(self):
        ''' Captura eventos de reinicialização do jogo e de disparos da nave'''
        self.keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if self.state != GameState.IN_GAME:          
                if self.keys[pygame.K_r]:
                    # reiniciar o jogo
                    self.__init__()

            if self.keys[pygame.K_SPACE] and self.state == GameState.IN_GAME:

                if (
                    self.player.time_since_last_shot >
                    self.player.cooldown_tiro
                    and self.player.isBig # O player só pode atirar se estiver grande
                ):
                    projectile = self.player.shoot(["corpo"]) # cria um novo projétil
                    self.p_projectiles.append(projectile)
                    self.player.time_since_last_shot = 0 # reseta o tempo

    def draw_playing(self):
        ''' Desenha os elementos do jogo'''
        self.background.draw(self.screen)

        #--- Player
        self.player.draw(self.screen)

        #--- Tiros do player
        for projectile in self.p_projectiles:
            projectile.draw(self.screen)

        # Tiros do Boss
        for projectile in self.b_projectiles:
            projectile.draw(self.screen)

        #--- Final Boss
        if self.final_boss.alive:
            self.final_boss.draw(self.screen)

        #--- Paredes
        for parede in self.paredes:
            parede.draw(self.screen)

        #--- Bombas
        for bomb in self.bombs:
            bomb.draw(self.screen)

        #--- Vidas do jogador
        self.draw_hud()

    def draw_hud(self):
        ''' Desenha os corações do player '''
        x_inicial = 30
        y_inicial = 690
        espacamento = 50
        tamanho_pixel = 2

        for i in range(self.player.vidas):
            if i > 10: break

            x_offset = x_inicial + (i * espacamento)

            for nome_parte, (pontos, tipo) in self.player.heart_partes.items():
                cor = self.player.heart_cores[nome_parte]["interior"]

                if tipo == "polygon":
                    pontos_tela = [(p[0] * tamanho_pixel + x_offset,
                                    p[1] * tamanho_pixel + y_inicial) for p in pontos]
                    pygame.draw.polygon(self.screen, cor, pontos_tela)

                elif tipo == "circle":
                    centro = (pontos["centro"][0] * tamanho_pixel + x_offset,
                              pontos["centro"][1] * tamanho_pixel + y_inicial)
                    pygame.draw.circle(self.screen, cor, centro, pontos["raio"] * tamanho_pixel)

    def update_playing(self, dt):

        ''' Updates de movimento e de comportamento que ocorrem durante o jogo '''

        if not self.player.alive: self.state = GameState.GAME_OVER # player morre == Game Over
        if self.fase_atual == 3 and not self.final_boss.alive: self.state = GameState.GAME_WIN # boss morre == Game Win

        # --- Background
        self.background.update(dt)

        # --- Player
        self.player.update(dt)

        #--- Tiros do player
        for projectile in self.p_projectiles:
            projectile.update(dt)

        self.p_projectiles = [
            p for p in self.p_projectiles
            if p.alive
        ]

        # --- Controle de Tempo e Transições de Fase
        self.tempo_fase += dt

        # --- ifs para as transições
        if self.fase_atual == 1 and self.tempo_fase > 25:
            self.fase_atual = 2
            self.audio.play_music("fase-2")
            self.bomb_cooldown = 8
            self.state = GameState.TRANSITION
            self.tempo_transicao = 2.5
            self.texto_transicao = "BOSS DETECTADO!"

        if self.fase_atual == 2 and self.final_boss.vida <= 100:
            self.fase_atual = 3
            self.audio.play_music("fase-3")
            self.state = GameState.TRANSITION
            self.tempo_transicao = 1.2
            self.texto_transicao = "PAREDES LASER ATIVADAS!"

        # --- MECÂNICA DA FASE 1 (E SUPERIORES)
        if self.fase_atual >= 1:
            self.bomb_timer += dt

            if self.bomb_timer >= self.bomb_cooldown:
                bomb = Bomb(
                    bomba_partes,
                    bomba_cores,
                    (0,0),
                    ["corpo"]
                )
                self.bombs.append(bomb)
                self.bomb_timer = 0

            for bomb in self.bombs:
                bomb.update(dt, self.player)

            self.bombs = [
                bomb for bomb in self.bombs
                if bomb.alive
            ]
        # --- MECÂNICA DA FASE 2 (E SUPERIORES)
        if self.fase_atual >= 2 and self.final_boss.alive:

            # --- Final Boss
            self.final_boss.update(dt, self.player)
            if self.final_boss.time_since_last_shot > self.final_boss.cd_shoot:
                projectile = self.final_boss.shoot(["fogo_interno"], self.player)
                self.b_projectiles.append(projectile)

        # --- Tiros do Boss
        for projectile in self.b_projectiles:
            projectile.update(dt)

        self.b_projectiles = [
            b for b in self.b_projectiles
            if b.alive
        ]

        # --- MECÂNICA DA FASE 3
        if self.fase_atual == 3 and self.final_boss.alive:
             self.final_boss.time_since_last_parede += dt
             self.final_boss.cd_shoot = 1 #tiros mais devagar agora q tem parede
             if self.final_boss.time_since_last_parede > self.final_boss.cd_parede:
                 # Sorteia a altura do buraco (y) para não ser sempre no meio
                 # A tela tem 720, então o centro do buraco fica entre 150 e 570
                 gap_y = random.randint(150, 570)
                 # Cria a parede fora da tela (X = 1350)
                 nova_parede = ParedeLaser(
                     parede_partes,
                     parede_cores,
                     centro=(1350, gap_y),
                     partes_criticas=partes_criticas_parede
                 )
                 self.paredes.append(nova_parede)
                 self.final_boss.time_since_last_parede = 0

        # Atualiza e limpa paredes mortas
        for parede in self.paredes:
            parede.update(dt)

        self.paredes = [p for p in self.paredes if p.alive]

        # Verifica colisão
        self.tratar_colisao()

    def update_transition(self, dt):
        self.tempo_transicao -= dt

        if self.tempo_transicao <= 0:
            self.state = GameState.IN_GAME

        if self.fase_atual == 2:
            self.final_boss.alive = True

        if self.fase_atual == 3:
            self.final_boss.time_since_last_parede = 0

    def draw_transition(self):
        # self.draw_playing()

        pelicula = pygame.Surface((WIDTH, 720), pygame.SRCALPHA)
        pelicula.fill((0, 0, 0, 160))
        self.screen.blit(pelicula, (0, 0))

        tempo_atual = pygame.time.get_ticks()
        alpha_texto = int(102.5 * math.sin(tempo_atual * 0.005) + 152.5)
        texto = self.fonte_subtitulo.render(self.texto_transicao, True, (255, 215, 0))
        texto.set_alpha(alpha_texto)
        texto_sombra = self.fonte_subtitulo.render(self.texto_transicao, True, (80, 10, 10))
        texto_sombra.set_alpha(alpha_texto)

        rect = texto.get_rect(center=(WIDTH / 2, 720 / 2))
        rect_sombra = texto_sombra.get_rect(center=(WIDTH / 2 + 5, 720 / 2 + 5))
        self.screen.blit(texto_sombra, rect_sombra)
        self.screen.blit(texto, rect)

    def draw_game_end(self, text, main_color, second_color):

        # Renderiza os textos (Texto, Antialias, Cor)
        texto_go = self.fonte_titulo.render(text, True, main_color)
        texto_sombra = self.fonte_titulo.render(text, True, second_color)
        texto_restart = self.fonte_subtitulo.render("Pressione R para recomeçar", True, (255, 255, 255))

        # Pega as hitboxes do texto para centralizar na tela
        rect_go = texto_go.get_rect(center=(WIDTH / 2, 720 / 2 - 50))
        rect_sombra = texto_sombra.get_rect(center=(WIDTH / 2 + 5, 720 / 2 - 45))
        rect_restart = texto_restart.get_rect(center=(WIDTH / 2, 720 / 2 + 50))

        # Cola os textos na tela
        self.screen.blit(texto_sombra, rect_sombra)
        self.screen.blit(texto_go, rect_go)
        self.screen.blit(texto_restart, rect_restart)

    def verificar_colisao(self, hitbox1, hitbox2):

        dist_min = hitbox1["raio"] + hitbox2["raio"]
        real_dist = math.hypot(hitbox1["centro"][0] - hitbox2["centro"][0],
                              hitbox1["centro"][1] - hitbox2["centro"][1])

        return dist_min > real_dist

    def tratar_colisao(self):
        # ou verifica todos os pontos da borda ou usa o métododo raio

        player_hitbox = self.player.hitboxes[0]
        boss_hitbox = self.final_boss.hitboxes
        #player_projectiles = [p.hitboxes for p in self.p_projectiles]

        # player x boss
        for b_hitbox in boss_hitbox:
            if self.verificar_colisao(player_hitbox, b_hitbox):
                # player toma dano
                if self.player.time_since_last_damage > self.player.cooldown_damage:
                    self.player.vidas -= 1
                    self.player.time_since_last_damage = 0

        # boss x projetil player
        for p_proj in self.p_projectiles:
            p_proj_hitbox = p_proj.hitboxes[0]
            for b_hitbox  in boss_hitbox:
                if self.verificar_colisao(p_proj_hitbox, b_hitbox):
                    # boss toma dano
                    # distroi projetil
                    p_proj.alive = False
                    self.final_boss.vida -= 2


        # player x projetil boss
        for b_proj in self.b_projectiles:
            b_proj_hitbox = b_proj.hitboxes[0]
            if self.verificar_colisao(b_proj_hitbox, player_hitbox):
                # boss toma dano
                # distroi projetil
                b_proj.alive = False
                if self.player.time_since_last_damage > self.player.cooldown_damage:
                    self.player.vidas -= 1
                    self.player.time_since_last_damage = 0


        # player x paredes
        for parede in self.paredes:
            for p_hitbox in parede.hitboxes:
                if self.verificar_colisao(player_hitbox, p_hitbox):
                    if self.player.time_since_last_damage > self.player.cooldown_damage:
                        self.player.vidas -= 1
                        self.player.time_since_last_damage = 0

        # player x bombas
        for bomb in self.bombs:
            if self.verificar_colisao(player_hitbox, bomb.hitboxes[0]):
                if self.player.time_since_last_damage > self.player.cooldown_damage:
                    self.player.vidas -= 1
                    self.player.time_since_last_damage = 0
                    bomb.alive = False

        # tiro do player x bombas
        for p_proj in self.p_projectiles:
            p_proj_hitbox = p_proj.hitboxes[0]
            for bomb in self.bombs:
                if self.verificar_colisao(p_proj_hitbox, bomb.hitboxes[0]):
                    # boss toma dano
                    # destroi projetil
                    p_proj.alive = False
                    bomb.alive = False

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000 # Define tempo de cada frame
            self.handle_events()

            if self.state == GameState.IN_GAME:
                self.update_playing(dt)
                self.draw_playing()
            elif self.state == GameState.TRANSITION:
                self.update_transition(dt)
                self.draw_playing()
                self.draw_transition()
            elif self.state == GameState.GAME_OVER:
                self.draw_game_end("GAME OVER", (255, 50, 50), (80, 10, 10))
            elif self.state == GameState.GAME_WIN:
                self.draw_game_end("GAME WIN", (50, 50, 250), (0, 0, 128))

            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()