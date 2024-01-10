import random

class GuessNumberGame:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.guesses = 0

    def guess(self, number):
        self.guesses += 1
        if number < self.number_to_guess:
            return "Higher"
        elif number > self.number_to_guess:
            return "Lower"
        else:
            return "Correct"
