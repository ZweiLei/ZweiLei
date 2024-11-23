# This program is a rock/scissors/paper game with computer. 
# We plan to have 4 functions, including getting computer's choice, collecting user's choice, compare who is the winner, and print the result.
import random

class Game1:
    def __init__(self) -> None:
        self.pc_pick = self.get_pc_pick()
        self.user_pick = self.get_user_pick()
        self.result = self.get_result()

    def get_pc_pick(self):
        rand_number = random.randint(1, 3)
        options = {1: 'rock', 2: 'paper', 3: 'scissors'}
        return options[rand_number]
    
    def get_user_pick(self):
        while True:
            user_pick = input('Please enter rock/paper/scissors: ')
            user_pick = user_pick.lower()

            if user_pick in ('rock', 'paper', 'scissors'):
                break
            else:
                print('Something wrong, please enter again: ')
        return user_pick
    
    def get_result(self):
        if self.pc_pick == self.user_pick:
            return 'FAIR'
        elif self.user_pick == 'rock' and self.pc_pick == 'scissors':
            return 'WIN'
        elif self.user_pick == 'scissors' and self.pc_pick == 'paper':
            return 'WIN'
        elif self.user_pick == 'paper' and self.pc_pick == 'rock':
            return 'WIN'
        else:
            return 'LOSE'

    def print_result(self):
        print(f"Computer's pick: {self.pc_pick}")
        print(f"Your pick: {self.user_pick}")
        print(f"YOU {self.result}")
    
if __name__ == "__main__":
    game = Game1()
    game.print_result()

