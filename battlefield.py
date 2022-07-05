from human import Human
from ai import Ai
player_1 = Human()
player_2 = None
class Battlefield:
    def __init__(self):
        pass

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.get_players()
        self.get_gesture()

    def get_players(self):
        print('How many players? 1 or 2')
        user_input = int(input(''))
        if user_input == 1:
            player_2 = Ai()
        elif user_input == 2:
            player_2 = Human()

    def get_gesture(self):
        player_1.player_choice()
        player_2.player_choice()

    def compare_gesture():
        if player_1.player_choice() == player_2.player_choice():
            print ('It is a tie, play again!')
        elif player_1.player_choice() == 'Rock':
            if player_2.player_choice() == 'Scissors' or 'Lizard':
                print(f'{player_1} wins')
            elif player_2.player_choice() == 'Paper' or 'Spock':
                print(f'{player_2} wins')
        elif player_1.player_choice() == 'Scissors':
            if player_2.player_choice() == 'Paper' or 'Lizard':
                print(f'{player_1} wins')
            elif player_2.player_choice() == 'Rock' or 'Spock':
                print(f'{player_2} wins')
        elif player_1.player_choice() == 'Paper':
            if player_2.player_choice() == 'Rock' or 'Spock':
                print(f'{player_1} wins')
            elif player_2.player_choice() == 'Scissors' or 'Lizard':
                print(f'{player_2} wins')
        elif player_1.player_choice() == 'Lizard':
            if player_2.player_choice() == 'Spock' or 'Paper':
                print(f'{player_1} wins')
            elif player_2.player_choice() == 'Rock' or 'Scissors':
                print(f'{player_2} wins')
        elif player_1.player_choice() == 'Spock':
            if player_2.player_choice() == 'Scissors' or 'Rock':
                print(f'{player_1} wins')
            elif player_2.player_choice() == 'Lizard' or 'Paper':
                print(f'{player_2} wins')
            
        pass
        
        

    def display_welcome(self):
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock')
        print('Each match will be a best of three games')

    def display_rules(self):
        print('Rock crushes Scissors \nScissors cuts Paper \nPaper covers Rock \nRock crushes Lizard \nLizard poisons Spock \nSpock smashes Scissors \nScissors decapitates Lizard \nLizard eats Paper \nPaper disproves Spock \nSpock vaporizes Rock\n')



    