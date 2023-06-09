import random


def main():
    instruction()  # calling instructions
    proverb()
    decision()  # calling decision function


# this function prints the first message that needs to be displayed in the screen
def instruction():
    print("****************************************************************")
    A = 'I N S T R U C T I O N S'
    title = A.center(64)  # used to print instructions in center
    print(title)
    print("Guess all the words in the proverb before the number of times a letter get revealed \nexceeds the number of"
          "words in the proverb.", "\nA letter gets revealed every time you don’t guess any words, and for every word\n"
                                   "you guess that is not in the proverb.""\nYou can specify as many words as "
                                   "you like at each guess.")
    print("*********************************************************************")


# for generating random proverb
def proverb():
    listP = ["Absence makes the heart grow fonder.",
             " Action speaks louder than words", "All's fair in love and war.",
             "A dog is a man's best friend.", "Don't bite off more than you can chew."]  #have added few proverb u can add many as u like

    proverbChosen = random.choice(listP)  # random proverb generating
    word_count = len(proverbChosen.split())  # counts the words present in proverb

    print(proverbChosen) # do remove this line as it prints the proverb i kept this for checking purpose only 

    guesses = ''  # empty part that will store the guessed word

    turns = 8  # the user has this number of trials
    while turns > 0:
        wrong = 0  # how many times the user guessed wrong words
        for char in proverbChosen:

            if char in guesses:
                print(char, end=" ")
            elif char == ' ':
                print(' ', end=" ")
            elif char == "'":
                print("'", end=" ")  # prints the ' if its in the proverb
            else:
                print("~", end=" ")
                wrong += 1  # each time wrong word is guessed, its value is increased by 1

        if wrong == 0:
            print("You guessed it right")
            print("The proverb is: ", proverbChosen)
            break

        print()
        guess = input("Guess:")
        guesses += guess  # stores the input word in guesses

        if guess not in proverbChosen:

            turns -= 1  # in case of wrong ans the turn decreases by 1

            print("Misses:", guess)

            # this will print the number of
            # turns left for the user
            print("You have", + turns, 'more guesses')

            if turns == 0:
                print("You Loose")


# asking user if they want to play the game again
def decision():
    ask = input("Do you want to play again? Yes or No ")
    if ask == "yes" or ask == "Yes":
        main()
    elif ask == "no" or ask == "No":
        print("Thankyou for playing this game.Have a great day a head")
    else:
        print("please enter either yes or no")
        decision()


main()
