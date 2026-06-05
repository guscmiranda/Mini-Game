from enum import Enum

class GameState(Enum):
    '''
    Ajuda a controlar os estados do jogo,
    cada um possui métodos de desenho e lida diferente com
    os updates e inputs do jogador
    '''
    IN_GAME = 1
    GAME_OVER = 2
    GAME_WIN = 3
    TRANSITION = 4