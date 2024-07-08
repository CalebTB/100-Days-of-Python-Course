import os
import random


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    random_word_list = ["bamboo", "forest", "panda", "dam", "water", "imagine", "dragons"]
    end_of_game = False

    hangman_choice = random.choice(random_word_list)
    lives = 5
    blank_list = []
    correct_guessed_list = []
    overall_guessed_list = []

    for letter in hangman_choice:
        blank_list += "_"

    while not end_of_game:
        isGuessCorrect = False

        print("GAME STATS:")
        print(f"Lives: {lives}")
        print(f"Letters Guessed: {overall_guessed_list}\n")
        print(f"{blank_list}\n")
        user_guess = str(input("\nGuess a letter: ")).lower()

        if user_guess not in overall_guessed_list:  # Checks if in overall guess list, if so append
            overall_guessed_list.append(user_guess)
            for list_number in range(len(hangman_choice)):
                if user_guess == hangman_choice[list_number]:  # Replaces "_" with the user letter guess
                    blank_list[list_number] = user_guess
                    isGuessCorrect = True
            if isGuessCorrect:
                pass
            else:
                lives = lives - 1

                if lives == 0:
                    clear()
                    print("GAME STATS:")
                    print(f"Lives: {lives}")
                    print(f"Letters Guessed: {overall_guessed_list}\n")
                    print(f"The word was: {hangman_choice}...GAME OVER")
                    end_of_game = True
                    break
        else:
            print("You have already guessed that letter!")

        clear()
        # Check Answer
        correct_guessed_list = "".join(blank_list)
        if correct_guessed_list == hangman_choice:
            print("GAME STATS:")
            print(f"Lives: {lives}")
            print(f"Letters Guessed: {overall_guessed_list}\n")
            print(blank_list)
            end_of_game = True
            print(f"You guessed the word: {correct_guessed_list}")


if __name__ == '__main__':
    main()
