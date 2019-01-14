import random
number=random.randint(1,99)



def guess():
    guesses = 0
    while guesses < 5:

        number_guessed = int(input("Guess a number between 1-99: "))

        if number_guessed < 1:
            print("The number must not be less than 1")
        elif number_guessed > 99:
            print("The number must not be more than 99")
        else:
            guesses += 1
            guesses_rem = 5 - guesses
            print("You have " + str(guesses_rem) + " Guesses")
        if number == number_guessed:
            print("Congratulations, you have found the number" + str(number))
            print("You guess it in : ", str(guesses) + " guesses")
            break
    if number !=number_guessed:

        print("You loose, the number is "+ str(number))
        repeat= input("Do you want to play again? Click y for yes and n for no: ")
        if repeat == 'y':
            guess()
        else:
            print("You have terminated the game!")







guess()