import random

game_number = random.randint(1,10)


guess = int(input("Enter a number Between 1 and 10:"))
if guess > game_number:
    print("too high")
elif guess < game_number:
    print("too low ")
else:
    print("you win")