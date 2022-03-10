import random

def hangman():
    """
    Classic Hangman game function
    """
    word = random.choice(["football","tennis","rugby","basketball","snooker","hurling","squash"])  # The word list the game will choose from
    letters_choice = 'qwertyuiopasdfghjklzxcvbnm'  # The valid inputs the user can select from
    guesses = 12  # The maximum number of times the game will loop if the word is not guessed
    guess_made = ''

    # Main gameplay section
    while len(word) > 0:
        answer = ''
        wrong = 0

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
        
        print("Guess the word:", answer)
        guess = input()

        # To make sure only valid letters are picked
        if guess in letters_choice:
            guess_made = guess_made + guess
        else:
            print("Enter a letter from a-z:")
            guess = input()

hangman()        
