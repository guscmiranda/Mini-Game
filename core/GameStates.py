from enum import Enum

class GameState(Enum):
    IN_GAME = 1
    GAME_OVER = 2
    GAME_WIN = 3
    TRANSITION = 4