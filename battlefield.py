from human import Human
from ai import Ai

class Battlefield:
    def __init__(self):
        player_1 = Human()
        player_2 = None

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.get_players()

    def get_players(self):
        print('How many players? 1 or 2')
        user_input = int(input(''))
        if user_input == 1:
            player_2 = Ai()
        elif user_input == 2:
            player_2 = Human()

    def get_gesture(self):
        pass
        

    def display_welcome(self):
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock')
        print('Each match will be a best of three games')

    def display_rules(self):
        print('Rock crushes Scissors \nScissors cuts Paper \n Paper covers Rock \n Rock crushes Lizard \n Lizard poisons Spock \n Spock smashes Scissors \n Scissors decapitates Lizard \n Lizard eats Paper \n Paper disproves Spock \n Spock vaporizes Rock\n')



    