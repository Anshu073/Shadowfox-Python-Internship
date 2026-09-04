# Hangman Game
import random

words = ("orange","banana","apple","cherry")

hangman_art = {
    0 : (
        "   ",
        "   ",
        "   "),
    1 : (
        " O ",
        "   ",
        "   "),
    2 : (
        " O ",
        " | ",
        "   "),
    3 : (
        " O ",
        "/| ",
        "   "),
    4 : (
        " O ",
        "/|\\",
        "   "),
    5 : (
        " O ",
        "/|\\",
        "/  "),
    6 : (
        " O ",
        "/|\\",
        "/ \\")
    }

def display_man(wrong_guesses):
    print("****************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("****************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    isRunning =True
    isContinue = True


    while isContinue:
        while isRunning:
            display_man(wrong_guesses)
            display_hint(hint)

            guess = input("Enter a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input!")
                continue

            if guess in guessed_letters:
                print(f"{guess} is already guessed")
                continue

            guessed_letters.add(guess)
            
            if guess in answer:
                for i in range(len(answer)):
                    if answer[i] == guess:
                        hint[i] = guess
            else:
                wrong_guesses += 1
            
            if "_" not in hint:
                display_man(wrong_guesses)
                display_answer(answer)
                print("YOU WIN!")
                isRunning = False
            elif wrong_guesses >= len(hangman_art) - 1:
                display_man(wrong_guesses)
                display_answer(answer)
                print("YOU LOSE!")
                isRunning = False

        again = input("Want to Play Again? (Y/N): ").lower()
        if again == "y":
            answer = random.choice(words)
            hint = ["_"] * len(answer)
            wrong_guesses = 0
            guessed_letters = set()
            isRunning = True
        elif again == "n":
            isContinue = False
        else:
            print("Please enter a valid Input!")


if __name__ == '__main__':
    main()