import random

random_number = random.randrange(1,20)
number_of_guesses = 0

name = (input("Hello! What is your name?" + "\n"))
print ("\n")
print("Well, {name}, I am thinking of a number between 1 and 20. \nTake a guess")
while True:
    number_of_guesses += 1
    number_of_player = int(input())
    print("\n")
    if number_of_player == random_number:
        print("Good job, {name}! You guessed my number in {number_of_guesses} guesses!")
        break
    elif number_of_player < random_number:
        print ("Your guess is too low. \nTake a guess")
        continue
    else:
        print ("Your guess is too high. \nTake a guess")
        continue