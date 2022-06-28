import keyboard
import random 
from colorama import Fore 

words = open('words_alpha.txt', "r").readlines()
guess_count = 10

def _guess(word):
    global guess_count
    guess = input("Enter your guess: ")
    if len(guess) > len(word.strip()) or len(guess) < len(word.strip()):
        print(f"Guess cannot be greater or less than {len(word.strip())}")
        _guess(word)
    if guess.lower() == word.lower():
        print("You won!")
        return main()
    else:
        guessSplit = [letter for letter in guess]
        wordSplit = [letter for letter in word]
        res = ""
        correct = 0
        for _i, i in enumerate(guessSplit):
            if i in wordSplit:
                # Letter correct
                if guessSplit[_i] == wordSplit[_i]:
                    # Letter correct with index
                    res += Fore.GREEN + i + Fore.RESET
                    wordSplit[_i] = " "
                    correct += 1
                else:
                    # Letter correct elsewhere
                    res += Fore.YELLOW + i + Fore.RESET
            else:
                res += i
        guess_count -= 1
        print(f"{res}")
        if correct == len(word.strip()):
            print("You won!")
            return main()
        if guess_count == 0:
            print(f"You lost! The word was: {word}")
            main()
        else:
            print("You have " + str(guess_count) + " guesses left")
            _guess(word)

def main():
    while True:
        input("Press enter to start game ")
        print("Selecting a random word...")
        word = words[random.randint(0, len(words) - 1)]
        print("Word selected!")
        print(f"Hint: {len(word.strip())} letters")
        _guess(word)
        

if __name__ == "__main__":
    main()