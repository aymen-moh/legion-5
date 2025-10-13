import random

roll = random.randint(1, 100)
guess = int(input("Guess a Random Number Between 1 and 100"))
guesses = 0
while True:
  if (roll > guess):
    guesses += 1
    print("guesses:", guesses)
    guess = int(input("Guess Higher!"))
  elif (roll < guess):
    guesses += 1
    print("guesses:", guesses)
    guess = int(input("Guess Lower!"))
  else:
    print("You Won! it took you", guesses, "guesses!")
    break