from re import T
from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()

    def player_choice(self):
        loop = True
        while loop is True:
            print("Press '0' for Rock \nPress '1' for Paper \nPress '2' for Scissors \nPress '3' for Lizard \nPress '4' for Spock")
            user_input = int(input('Which gesture would you like to play? '))
            if user_input == 0:
                self.chosen_gesture = self.gesture_list[0]
                break
            elif user_input == 1:
                self.chosen_gesture = self.gesture_list[1]
                break
            elif user_input == 2:
                self.chosen_gesture = self.gesture_list[2]
                break
            elif user_input == 3:
                self.chosen_gesture = self.gesture_list[3]
                break
            elif user_input == 4:
                self.chosen_gesture = self.gesture_list[4]
                break
            elif user_input != 0 or user_input != 1 or user_input != 2 or user_input != 3 or user_input != 4:
                print('Invalid response, please try again.')

        print(f'Player one chose {self.chosen_gesture}')
            