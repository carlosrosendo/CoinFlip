
import random

choice = input(
    'Welcome to the game, would you like to do "Heads" or "Tails"?')


random_side = random.randint(0, 1)
if random_side == 1:
    heads = print("Heads")

else:
    tails = print("Tails")

if choice == "Heads" and random_side == 1:
    print("You guessed Heads, You Won!")
elif choice == "Tails" and random_side == 0:
    print("You guessed Tails, you Won!")
else:
    print("You guessed wrong, you Loose!")
