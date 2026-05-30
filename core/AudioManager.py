import pygame

class AudioManager:
    def __init__(self):
        pygame.mixer.init()

        self.musics = {
            "fase-1": "../assets/audio/Before_The_Boss_Arrives.ogg",
            "fase-2": "../assets/audio/The_Tutorial_Had_Teeth.ogg",
            "fase-3": "../assets/audio/King_of_the_Arena.ogg",
            "game-win": "../assets/audio/Game_Win.ogg", # Não existe
            "game-over": "../assets/audio/Game_Over.ogg", # Não existe
        }
        self.musica_atual = None

        self.efects = {}
        #self.load_efects()

    def load_efects(self):
        self.efects["player_shot"] = pygame.mixer.Sound("assets/audio/Player_Shot.wav")
        self.efects["boss_shot"] = pygame.mixer.Sound("assets/audio/Boss_Shot.wav")
        self.efects["boss_wall"] = pygame.mixer.Sound("assets/audio/Boss_Wall.wav")
        self.efects["player_hit"] = pygame.mixer.Sound("assets/audio/Player_Hit.wav")


    def play_music(self, music_name, loop=-1):

        if music_name in self.musics and music_name != self.musica_atual:
            try:
                pygame.mixer.music.load(self.musics[music_name])
                pygame.mixer.music.stop()
                pygame.mixer.music.play(loop)
                self.musica_atual = music_name
                pygame.mixer.music.set_volume(0.008)
            except Exception as e:
                print(f"Erro ao carregar musica {self.musics[music_name]}: {e}")

    def stop_music(self):
        pygame.mixer.music.stop()
        self.musica_atual = None

    def play_efect(self, efect_name):
        if efect_name in self.efects:
            self.efects[efect_name].play()

