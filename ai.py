
from player import Player
import random

class Ai(Player):
    def __init__(self):
        super().__init__()

    def player_choice(self):
        self.chosen_gesture = random.choice(self.gesture_list)
        print(f'AI has played {self.chosen_gesture}')