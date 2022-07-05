from human import Human
from ai import Ai
from player import Player
player_1 = Human()
player_2 = Ai()
class Battlefield:
    def __init__(self):
        player_1 = Human()
        player_2 = None

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.get_players()
        self.compare_gesture()
        self.display_winner()

    def display_welcome(self):
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock')
        print('Each match will be a best of three games')

    def display_rules(self):
        print('Rock crushes Scissors \nScissors cuts Paper \nPaper covers Rock \nRock crushes Lizard \nLizard poisons Spock \nSpock smashes Scissors \nScissors decapitates Lizard \nLizard eats Paper \nPaper disproves Spock \nSpock vaporizes Rock\n')


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

    def compare_gesture(self):
        while player_1.win_count < 2 and player_2.win_count < 2:
            self.get_gesture()
            if player_1.chosen_gesture == player_2.chosen_gesture:
                print ('It is a tie, play again!')
            elif player_1.chosen_gesture == 'Rock':
                if player_2.chosen_gesture == 'Scissors' or 'Lizard':
                    player_1.win_count += 1
                    print('player_1 wins')
                elif player_2.chosen_gesture == 'Paper' or 'Spock':
                    player_2.win_count += 1
                    print('player_2 wins')
            elif player_1.chosen_gesture == 'Scissors':
                if player_2.chosen_gesture == 'Paper' or 'Lizard':
                    player_1.win_count += 1
                    print('player_1 wins')
                elif player_2.chosen_gesture == 'Rock' or 'Spock':
                    player_2.win_count += 1
                    print('player_2 wins')
            elif player_1.chosen_gesture == 'Paper':
                if player_2.chosen_gesture == 'Rock' or 'Spock':
                    player_1.win_count += 1
                    print('player_1 wins')
                elif player_2.chosen_gesture == 'Scissors' or 'Lizard':
                    player_2.win_count += 1
                    print('player_2 wins')
            elif player_1.chosen_gesture == 'Lizard':
                if player_2.chosen_gesture == 'Spock' or 'Paper':
                    player_1.win_count += 1
                    print('player_1 wins')
                elif player_2.chosen_gesture == 'Rock' or 'Scissors':
                    player_2.win_count += 1
                    print('player_2 wins')
            elif player_1.chosen_gesture == 'Spock':
                if player_2.chosen_gesture == 'Scissors' or 'Rock':
                    player_1.win_count += 1
                    print('player_1 wins')
                elif player_2.chosen_gesture == 'Lizard' or 'Paper':
                    player_2.win_count += 1
                    print('player_2 wins')

    
    def display_winner(self):
        if player_1.win_count == 2:
            print('player 1 is your winner!')
        elif player_2.win_count == 2:
            print('player 2 is your winner!')


            
        
        

    

   


    