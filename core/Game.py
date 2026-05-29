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
import random
import math

WIDTH = 1280

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.state = GameState.IN_GAME
        self.running = True
        self.keys = pygame.key.get_pressed()

        self.fonte_titulo = pygame.font.SysFont('arial', 100, bold=True)
        self.fonte_subtitulo = pygame.font.SysFont('arial', 40)

        self.player = Spaceship(spaceship_partes, spaceship_cores, centro=(0,0), partes_criticas=["corpo"])
        self.final_boss = FinalBoss(boss9_partes, boss9_cores, centro=(0,0), partes_criticas=["cabeca", "tronco"])

        self.enemies = []
        self.p_projectiles = []
        self.b_projectiles = []
        self.paredes = []


    def hadle_events(self):
        self.keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if self.state != GameState.IN_GAME:          
                if self.keys[pygame.K_r]:
                    #self.state = GameState.IN_GAME
                    self.__init__()


            if self.keys[pygame.K_SPACE] and self.state == GameState.IN_GAME:

                if (
                    self.player.time_since_last_shot >
                    self.player.cooldown_tiro
                    and self.player.isBig
                ):
                    projectile = self.player.shoot(["corpo"])
                    self.p_projectiles.append(projectile)
                    self.player.time_since_last_shot = 0

    def draw_playing(self):
        self.screen.fill("black")

        #--- Player
        #if self.player.alive:
        self.player.draw(self.screen)

        #--- Tiros do player
        for projectile in self.p_projectiles:
            projectile.draw(self.screen)

        # Tiros do Boss
        for projectile in self.b_projectiles:
            projectile.draw(self.screen)

        #--- Final Boss
        self.final_boss.draw(self.screen)

        #---- Paredes
        for parede in self.paredes:
            parede.draw(self.screen)




        # chama inimidors.draw() num for de inimigos
        # chama tiros.draw() num for de tiros ainda na tela

    def update_playing(self, dt):

        if not self.player.alive: self.state = GameState.GAME_OVER
        if not self.final_boss.alive: self.state = GameState.GAME_WIN

        # --- Player
        self.player.update(dt)

        #--- Tiros do player
        for projectile in self.p_projectiles:
            projectile.update(dt)

        self.p_projectiles = [
            p for p in self.p_projectiles
            if p.alive
        ]

        #--- Final Boss
        if self.final_boss.alive:
            self.final_boss.update(dt, self.player)

        # --- Tiros do Boss
        for projectile in self.b_projectiles:
            projectile.update(dt)

        self.b_projectiles = [
            b for b in self.b_projectiles
            if b.alive
        ]

        if self.final_boss.time_since_last_shot > self.final_boss.cd_shoot:
            projectile = self.final_boss.shoot(["fogo_interno"], self.player)
            self.b_projectiles.append(projectile)

        # Checa colisão
        self.tratar_colisao()

        # Cria paredes
        # --- Gerador de Paredes do Boss ---
        if self.final_boss.alive:
            self.final_boss.time_since_last_parede += dt
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




    def draw_game_over(self):

        # Renderiza os textos (Texto, Antialias, Cor)
        texto_go = self.fonte_titulo.render("GAME OVER", True, (255, 50, 50))
        texto_restart = self.fonte_subtitulo.render("Pressione R para recomeçar", True, (255, 255, 255))

        # Pega as hitboxes do texto para centralizar na tela
        rect_go = texto_go.get_rect(center=(WIDTH / 2, 720 / 2 - 50))
        rect_restart = texto_restart.get_rect(center=(WIDTH / 2, 720 / 2 + 50))

        # Cola os textos na tela
        self.screen.blit(texto_go, rect_go)
        self.screen.blit(texto_restart, rect_restart)

    def draw_game_win(self):
        # Renderiza os textos (Texto, Antialias, Cor)
        texto_go = self.fonte_titulo.render("GAME WIN", True, (50, 50, 250))
        texto_restart = self.fonte_subtitulo.render("Pressione R para recomeçar", True, (255, 255, 255))

        # Pega as hitboxes do texto para centralizar na tela
        rect_go = texto_go.get_rect(center=(WIDTH / 2, 720 / 2 - 50))
        rect_restart = texto_restart.get_rect(center=(WIDTH / 2, 720 / 2 + 50))

        # Cola os textos na tela
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
                self.player.vidas -= 1
                # cd de dano
                print("colisao no player")

        # boss x projetil player
        for p_proj in self.p_projectiles:
            p_proj_hitbox = p_proj.hitboxes[0]
            for b_hitbox  in boss_hitbox:
                if self.verificar_colisao(p_proj_hitbox, b_hitbox):
                    # boss toma dano
                    # distroi projetil
                    p_proj.alive = False
                    self.final_boss.vida -= 5

                    print("colisao projetil com boss")


        # player x projetil boss
        for b_proj in self.b_projectiles:
            b_proj_hitbox = b_proj.hitboxes[0]
            if self.verificar_colisao(b_proj_hitbox, player_hitbox):
                # boss toma dano
                # distroi projetil
                b_proj.alive = False
                self.player.vidas -= 1

                print("colisao projetil com boss")

        # player x paredes
        for parede in self.paredes:
            for p_hitbox in parede.hitboxes:
                if self.verificar_colisao(player_hitbox, p_hitbox):
                    print("COLISÃO COM A PAREDE LASER!")
                    self.player.vidas -= 1

        # player x projetil minions



    # TODO:
    #  lidar com eventos
    #  gerar updates em tudo
    #  desenhar
    #  lupar as coisas nisso

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000
            self.hadle_events()

            if self.state == GameState.IN_GAME:
                self.update_playing(dt)
                self.draw_playing()
            elif self.state == GameState.GAME_OVER:
                self.draw_game_over()
            elif self.state == GameState.GAME_WIN:
                self.draw_game_win()

            #...

            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()