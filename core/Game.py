import pygame

from GameStates import GameState
from entities.Spaceship import Spaceship
from entities.FinalBoss import FinalBoss
from models.spaceship_ray import *
from models.final_boss import  *
from models.spaceship import *



WIDTH = 1280

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.state = GameState.IN_GAME
        self.running = True
        self.keys = pygame.key.get_pressed()

        self.player = Spaceship(spaceship_partes, spaceship_cores, centro=(0,0), partes_criticas=["corpo"])
        self.final_boss = FinalBoss(boss9_partes, boss9_cores, centro=(0,0), partes_criticas=["cabeca", "tronco"])

        self.enemies = []
        self.projectiles = []

        self.time_since_last_spawn = 0

    def hadle_events(self):
        self.keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if self.state != GameState.IN_GAME:          
                if self.keys[pygame.K_r]:
                    pass # reinicia

            if self.keys[pygame.K_SPACE] and self.state == GameState.IN_GAME:

                if (
                    self.player.time_since_last_shot >
                    self.player.cooldown_tiro
                    and self.player.isBig
                ):
                    projectile = self.player.shoot(["corpo"])
                    self.projectiles.append(projectile)
                    self.player.time_since_last_shot = 0


    def draw_playing(self):
        self.screen.fill("black")

        #--- Player
        self.player.draw(self.screen, True)

        #--- Tiros do player
        for projectile in self.projectiles:
            projectile.draw(self.screen, True)

        #--- Final Boss
        self.final_boss.draw(self.screen, True)

        # chama inimidors.draw() num for de inimigos
        # chama tiros.draw() num for de tiros ainda na tela

    def update_playing(self, dt):

        # --- Player
        self.player.update(dt)

        #--- Tiros do player
        for projectile in self.projectiles:
            projectile.update(dt)

        self.projectiles = [
            p for p in self.projectiles
            if p.alive
        ]

        #--- Final Boss
        self.final_boss.update(dt, self.player)

    def draw_game_over(self):
        self.screen.fill((50,0,0))
        pass

    def checar_colisao(self):
        # ou verifica todos os pontos da borda ou usa o métododo raio

        # player x boss
        player_hitbox = self.player.hitboxes
        boss_hitbox = self.final_boss.hitboxes

        # distMin = player_hitbox.raio + boss_hitbox.raio
        # math.hupot()
        # player x projetil boss
        # player x bordas
        # player x projetil minions
        # boss x projetil player


        pass

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

            #...

            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()