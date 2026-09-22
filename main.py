import random

game_number = random.randint(1,10)
#print(game_number)
guess_counter=0

while(True):
    guess = int(input("Enter a number Between 1 and 10:"))
    guess_counter= guess_counter +1
    if guess > game_number:
        print("too high")
    elif guess < game_number:
        print("too low ")
    else:
        print("you win")
        print("Good job you got in", guess_counter, "times")
        break
   
        