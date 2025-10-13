import random
dif = int(input("set difficulty: \n 1 = easy \n 2 = medium\n 3 = hard\n 4 extreme "))
if (dif == 1):
  guesses = 12
elif (dif == 2):
    guesses = 9
elif (dif == 3):
      guesses = 6
elif (dif == 4):
        guesses = 4
else:
          dif = int(input("Please Choose Numbers 1 through 4 to select difficultylty! "))
  
roll = random.randint(1, 100)
guess = int(input("Guess a Random Number Between 1 and 100"))

while True:
  if (roll > guess):
    guesses -= 1
    print("guesses left:", guesses)
    guess = int(input("Guess Higher!"))
  elif (roll < guess):
    guesses += 1
    print("guesses:", guesses)
    guess = int(input("Guess Lower!"))
  else:
    print("You Won! You had", guesses, "guesses!")
    
    break