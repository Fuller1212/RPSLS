from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()

    def player_choice(self):
        while loop is True:
            print("Press '0' for Rock \n Press '1' for Paper \n Press '2' for Scissors \n Press '3' for Lizard \n Press '4' for Spock")
            user_input = int(input('Which gesture would you like to play? '))
            if user_input != 0 or 1 or 2 or 3 or 4:
                print('Invalid response, please try again.')
                loop = True
            else:
                loop = False
        if user_input == 0:
            self.chosen_gesture = 'Rock'
        elif user_input == 1:
            self.chosen_gesture = 'Paper'
        elif user_input == 2:
            self.chosen_gesture = 'Scissors'
        elif user_input == 3:
            self.chosen_gesture = 'Lizard'
        elif user_input == 4:
            self.chosen_gesture = 'Spock'