from human import Human
from ai import Ai

class Battlefield:
    def __init__(self):
        self.player_1 = Human()
        self.player_2 = None

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.get_players()
        self.compare_gesture()
        self.display_winner()
        self.play_again()

    def display_welcome(self):
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock')
        print('Each match will be a best of three games')

    def display_rules(self):
        print('Rock crushes Scissors \nScissors cuts Paper \nPaper covers Rock \nRock crushes Lizard \nLizard poisons Spock \nSpock smashes Scissors \nScissors decapitates Lizard \nLizard eats Paper \nPaper disproves Spock \nSpock vaporizes Rock\n')


    def get_players(self):
        print('How many players? 1 or 2')
        user_input = int(input(''))
        if user_input == 1:
            self.player_2 = Ai()
        elif user_input == 2:
            self.player_2 = Human()

    def get_gesture(self):
        self.player_1.player_choice()
        self.player_2.player_choice()

    def compare_gesture(self):
        while self.player_1.win_count < 2 and self.player_2.win_count < 2:
            self.get_gesture()
            if self.player_1.chosen_gesture == self.player_2.chosen_gesture:
                print ('It is a tie, play again!')
            elif self.player_1.chosen_gesture == 'Rock':
                if self.player_2.chosen_gesture == 'Scissors' or 'Lizard':
                    self.player_1.win_count += 1
                    print(f'{self.player_1}. wins')
                elif self.player_2.chosen_gesture == 'Paper' or 'Spock':
                    self.player_2.win_count += 1
                    print(f'{self.player_2} wins')
            elif self.player_1.chosen_gesture == 'Scissors':
                if self.player_2.chosen_gesture == 'Paper' or 'Lizard':
                    self.player_1.win_count += 1
                    print(f'{self.player_1} wins')
                elif self.player_2.chosen_gesture == 'Rock' or 'Spock':
                    self.player_2.win_count += 1
                    print(f'{self.player_2} wins')
            elif self.chosen_gesture == 'Paper':
                if self.player_2.chosen_gesture == 'Rock' or 'Spock':
                    self.player_1.win_count += 1
                    print(f'{self.player_1} wins')
                elif self.player_2.chosen_gesture == 'Scissors' or 'Lizard':
                    self.player_2.win_count += 1
                    print(f'{self.player_2} wins')
            elif self.player_1.chosen_gesturechosen_gesture == 'Lizard':
                if self.player_2.chosen_gesture == 'Spock' or 'Paper':
                    self.player_1.win_count += 1
                    print(f'{self.player_1} wins')
                elif self.player_2.chosen_gesture == 'Rock' or 'Scissors':
                    self.player_2.win_count += 1
                    print(f'{self.player_2} wins')
            elif self.player_1.chosen_gesture == 'Spock':
                if self.player_2.chosen_gesture == 'Scissors' or 'Rock':
                    self.player_1.win_count += 1
                    print(f'{self.player_1} wins')
                elif self.player_2.chosen_gesture == 'Lizard' or 'Paper':
                    self.player_2.win_count += 1
                    print(f'{self.player_2} wins')

    
    def display_winner(self):
        if self.player_1.win_count == 2:
            print('player 1 is your winner!')
        elif self.player_2.win_count == 2:
            print('player 2 is your winner!')

    def play_again(self):
        print('Do you want to play again?')
        user_input = input('yes or no')
        if user_input == 'yes':
            self.run_game()
        elif user_input == 'no':
            print('Thank you for playing')




            
        
        

    

   


    