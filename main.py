import random
from colorama import Fore, Style, init

#Initialize colorama for colored text
init(autoreset=True)

#LOAD WORDS
def load_words(filename="words.txt"):
    try:
        with open(filename, "r") as file:
            words = [line.strip().upper() for line in file if line.strip()]
        return words
    except FileNotFoundError:
        print(Fore.RED + "Error: words.txt not found!")
        return []

#GAME LOGIC
def play_game():
    words = load_words()
    if not words:
        return

    #Choose difficulty
    print(Fore.CYAN + "\nSelect Difficulty:")
    print("1. Easy (6 chances)")
    print("2. Medium (4 chances)")
    print("3. Hard (3 chances)")
    choice = input(Fore.YELLOW + "Enter choice: ")

    if choice == "1":
        total_chances = 6
    elif choice == "2":
        total_chances = 4
    else:
        total_chances = 3

    #Pick a random word
    word = random.choice(words)
    guessed_word = "_" * len(word)
    used_letters = set()

    print(Fore.GREEN + "\nWelcome to the Word Guessing Game!")
    print(f"The word has {len(word)} letters. Let's begin!")

    #Main game loop
    while total_chances > 0:
        print(Fore.CYAN + "\nWord: " + Fore.WHITE + guessed_word)
        print(Fore.MAGENTA + f"Used letters: {', '.join(sorted(used_letters)) if used_letters else 'None'}")
        print(Fore.YELLOW + f"Chances left: {total_chances}")

        letter = input(Fore.CYAN + "Guess a letter: ").upper()

        #Input validation
        if not letter.isalpha() or len(letter) != 1:
            print(Fore.RED + "Please enter a single valid letter.")
            continue

        if letter in used_letters:
            print(Fore.RED + "You already guessed that letter!")
            continue

        used_letters.add(letter)

        #Check guessed letter
        if letter in word:
            for index in range(len(word)):
                if word[index] == letter:
                    guessed_word = guessed_word[:index] + letter + guessed_word[index + 1:]
            print(Fore.GREEN + "Correct guess!")
        else:
            total_chances -= 1
            print(Fore.RED + "Incorrect guess.")

        # Win condition
        if guessed_word == word:
            print(Fore.GREEN + f"\nCongratulations! You guessed the word: {word}")
            break

    #Lose condition
    else:
        print(Fore.RED + f"\nGame Over! The correct word was: {word}")

#MENU
def main_menu():
    while True:
        print(Fore.YELLOW + "WELCOME TO WORD GUESSING GAME")
        print(Fore.CYAN + "\n1. Play Game")
        print("2. Instructions")
        print("3. Quit")

        choice = input(Fore.YELLOW + "\nEnter your choice: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            print(Fore.CYAN + """
🔹 Guess the letters of a secret word.
🔹 Each incorrect guess reduces your chances.
🔹 Difficulty levels affect your number of chances.
🔹 Win by revealing the entire word before running out of chances!
""")
        elif choice == "3":
            print(Fore.MAGENTA + "Goodbye! See you next time.")
            break
        else:
            print(Fore.RED + "Invalid choice! Please try again.")

#START
if __name__ == "__main__":
    main_menu()
