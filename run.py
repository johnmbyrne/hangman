import random


def hangman():
    """
    Classic Hangman game function
    """
    # The word list the game will choose from
    selection = (["football", "tennis", "rugby", "basketball",
                  "snooker", "hurling", "squash"])
    # Randomly selecting from the word list
    word = random.choice(selection)
    # The valid inputs the user can select from
    letters_choice = 'qwertyuiopasdfghjklzxcvbnm'
    guesses = 12
    guess_made = ''

    # Main gameplay section
    while len(word) > 0:
        answer = ''

        # What the game will do with the letter guesses
        for letter in word:
            if letter in guess_made:
                answer = answer + letter
            else:
                answer = answer + '_'+''
        # If the word is correctly guessed
        if answer == word:
            print(answer)
            print("Congratulations, you're a Winner!")
            break
        print("Guess the word (one letter at a time):", answer)
        guess = input()
        guess = guess.lower()
        """
        To make sure any letter entered is converted
        to lower case before comparing to the selected word
        """
        # To make sure only valid letters are picked
        if guess in letters_choice:
            guess_made = guess_made + guess
        elif len(guess) > 1:
            print(name, "enter a single letter from a-z:")
            guess = input()
            guess = guess.lower()
        elif guess not in letters_choice:
            print(name, "only pick letters from a-z please:")
            guess = input()
            guess = guess.lower()

        # What happens when wrong guess is made
        if guess not in word:
            guesses = guesses - 1
            if guesses == 11:
                print("11 incorrect guesses left")
                print("I I I I")
                print("I I I I")
                print("I I I X")
            if guesses == 10:
                print("10 incorrect guesses left")
                print("(Hint: it's a sport)")
                print("I I I I")
                print("I I I I")
                print("I I X X")
            if guesses == 9:
                print("9 incorrect guesses left")
                print("I I I I")
                print("I I I I")
                print("I X X X")
            if guesses == 8:
                print("8 incorrect guesses left")
                print("I I I I")
                print("I I I I")
                print("X X X X")
            if guesses == 7:
                print("7 incorrect guesses left")
                print("I I I I")
                print("I I I X")
                print("X X X X")
            if guesses == 6:
                print("6 incorrect guesses left")
                print("I I I I")
                print("I I X X")
                print("X X X X")
            if guesses == 5:
                print("5 guesses left")
                print("I I I I")
                print("I X X X")
                print("X X X X")
            if guesses == 4:
                print("4 incorrect guesses left")
                print("I I I I")
                print("X X X X")
                print("X X X X")
            if guesses == 3:
                print("3 incorrect guesses left")
                print("I I I X")
                print("X X X X")
                print("X X X X")
            if guesses == 2:
                print("2 incorrect guesses left")
                print("I I X X")
                print("X X X X")
                print("X X X X")
            if guesses == 1:
                print("1 incorrect guess left")
                print("I X X X")
                print("X X X X")
                print("X X X X")
            if guesses == 0:
                print("Nope, you lost!")
                print("The correct answer was", word)
                print("X X X X")
                print("X X X X")
                print("X X X X")
                break

# The initial introduction
name = input("Enter your name: ")
print("Hi", name)
print("Let's play Hangman!\n")
print("Guess the word, but you'll only get 12 wrong attempts!\n")
hangman()
print()
