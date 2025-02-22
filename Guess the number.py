import random #library

#global casting
NUM_DIGITS = 3 #size of the number.
MAX_GUESTS = 2 #number of guests allowed per game.

def get_secret_nbr():
    """Returns a string made of NUM_DIGITS random digits"""

    numbers = list('1234567890') #create a list from 0 to 9.
    random.shuffle(numbers) #shuffle numbers in random order
    
    #Get the numbers for NUM_DIGITS out of the pool.
    secret_nbr = ''
    for i in range(NUM_DIGITS):
        secret_nbr += str(numbers[i])
    return secret_nbr

def get_clues(guess, secret_nbr):
    """Returns a string with cold, warm, hot clues for a guess
    and a secret number pair"""

    if guess == secret_nbr:
        return 'That is correct!'
    
    #Conditionals for the clues and append to clues
    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_nbr:
            #correct digit, correct place.
            clues.append('Fermi') 
        elif guess [i] in secret_nbr:
            #correct digit, incorrect place.
            clues.append('Pico') 
    #if clues does not have anything it means that no digits are correct
    if len(clues) == 0:
        return 'Bagels'
    else:
    #sort in alphabetical order to not give extra clues.
        clues.sort()
        return ' '.join(clues)

def main():
    print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython,com
          
I am thinking of a number with no repeating digits.
Try to guess what it is. Here are some clues:

When I say:     That means:
    Pico        One digit is correct but in the wrong position.
    Fermi       One digit is in the right position.
    Bagels      No digits is correct''')

    while True: #Main game loop.
        #stores the secret number to be guessed.
        secret_nbr = get_secret_nbr()
        print("I have thought up a number")
        print("You have {} guesses to get it".format(MAX_GUESTS))

        num_guesses = 1

        while(num_guesses <= MAX_GUESTS):
            guess = ''
        #loops until a valid guess.
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess {}#:'.format(num_guesses))
                guess = input('> ')

            clues = get_clues(guess, secret_nbr)
            print(clues)
            num_guesses += 1

            if guess == secret_nbr:
                break #they are correct, and breaks the loop.
            if num_guesses > MAX_GUESTS:
                print("You ran out of guesses")
                print("The answer was {}.".format(secret_nbr))
        
        #Ask if the player wants another round.
        print("Do you want to play again? (yes or no)")
        response = input ('> ').lower()

        if response.startswith('n'):
            print("Thanks for playing")
            break

if __name__ == '__main__':
    main()
