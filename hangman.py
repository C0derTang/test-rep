import random

def hangman():
    word = random.choice(["python", "java", "syntax", "javascript", "c", "function", "mathematics", "logistics", "console", "ruby", "r", "programming", "coding", "scratch", "git", "github"])
    valid_letters = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guess_made= ''
    while len(word) > 0:
        main = ""
        missed = 0
        for letter in word:
            if letter in guess_made:
                main += letter
            else:
                main += "_" + " "
        if main == word:
            print(main)
            print("You win!")
            break
        print("Guess the word:", main)
        guess = input()

        if guess in valid_letters:
            guess_made = guess_made + guess
            valid_letters = valid_letters.replace(guess, "")
        else:
            print("Enter a valid character")
        if guess not in word:
            turns -= 1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You lose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break



name = input("Enter your name\n")
print("Welcome", name)
print("---------------")
print("Try to guess the word in less than 10 tries!")
hangman()
print()
