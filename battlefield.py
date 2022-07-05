

class Battlefield:
    def __init__(self):
        pass

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        

    def display_welcome(self):
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock')
        print('Each match will ne a best of three games')

    def display_rules(self):
        print('Rock crushes Scissors \n Scissors cuts Paper \n Paper covers Rock \n Rock crushes Lizard \n Lizard poisons Spock \n Spock smashes Scissors \n Scissors decapitates Lizard \n Lizard eats Paper \n Paper disproves Spock \n Spock vaporizes Rock\n')



    