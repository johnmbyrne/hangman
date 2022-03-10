import random

def hangman():
    """
    Classic Hangman game function
    """


    word = random.choice(["football","tennis","rugby","basketball","snooker","hurling","squash"])
    letters_choice = 'qwertyuiopasdfghjklzxcvbnm'
    guesses = 12
    guess_made = ''

    while len(word) > 0:
        answer = ''
        wrong = 0

        for letter in word:
            if letter in guess_made:
                answer = answer + letter
            else:
                answer = answer + '_'+''
        if answer == word:
            print(answer)
            print("Congratulations, you're a Winner!")
        
        print("Guess the word:", answer)
        guess = input()

        if guess in letters_choice:
            guess_made = guess_made + guess
        else:
            print("Enter a letter from a-z:")
            guess = input()

hangman()        
