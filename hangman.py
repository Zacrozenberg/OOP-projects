import random


WORDS = [
    'CASA', 'CARRO', 'MONO', 'ESTERNOCLEIDOMASTOIDEO', 'PYTHON', 'DJANGO',
    'MILTON', 'LENIS', 'SWAPPS', 'LOGIA', 'UNITTESTING'
]


class Hangman:
    def __init__(self, word_to_guess, number_of_lives=10):
        self.word_to_guess = word_to_guess
        self.remaining_letters = [letter for letter in word_to_guess]
        self.remaining_lives = number_of_lives

    @staticmethod
    def get_user_input():
        # Get a single letter as input from the user with validation
        while True:
            user_input = input("Enter a letter: ")

            # Check if the input is not empty and is a single character
            if user_input.isalpha() and len(user_input) == 1:
                letter = user_input
                return letter.upper()
            else:
                print("Please enter a valid single letter.")

    def display_status(self):
        # Display the word with _ for letters not found yet
        status = ['_' if l in self.remaining_letters else l for l in self.word_to_guess]

        # Print the result
        print("".join(status) + '\n')

    def update_letters(self, letter):
        print(f'{letter} is a hit !\n')
        self.remaining_letters = [l for l in self.remaining_letters if l != letter]
        if len(self.remaining_letters) == 0:
            print(f'Congrats ! You have found the word {self.word_to_guess}')
            quit()

    def update_lives(self, letter):
        print(f'{letter} is a miss !')
        self.remaining_lives -= 1
        print(f'You have {self.remaining_lives} lives left\n')

        if self.remaining_lives == 0:
            print(f'Sorry! You are out of lives and were unable to find the world {self.word_to_guess}')
            quit()

    def play_a_round(self):
        # Ask user for a letter and plays the round

        self.display_status()
        input_letter = self.get_user_input()

        if input_letter in self.remaining_letters:
            self.update_letters(input_letter)
        else:
            self.update_lives(input_letter)

    def play(self):
        while True:
            self.play_a_round()


if __name__ == '__main__':
    word_to_guess = random.choice(WORDS)
    hangman = Hangman(word_to_guess)
    hangman.play()
