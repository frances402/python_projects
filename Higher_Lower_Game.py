import random
seedVal = int(input("What seed should be used? "))
random.seed(seedVal)

while (True):
    lower = int(input("What is the lower bound? "))
    upper = int(input("What is the upper bound? "))
    if lower > upper:
        print("Lower bound must be less than upper bound.")
    else:
        break
number = random.randint(lower, upper)

while (True):
    guess = int(input("What is your guess?"))
    if guess > number:
        print("Nope, too high.")
    elif guess < number:
        print("Nope, too low.")
    elif guess == number:
        print("You got it!")
        break
