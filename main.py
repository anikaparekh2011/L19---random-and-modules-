import random

number = str(random.randint(1,9))

playing = True 

while playing:
    guess = input("enter a number to guess: ")
    if guess == number:
        print("you guessed the right number!")
        break
    else:
        print("you are wrong try again")