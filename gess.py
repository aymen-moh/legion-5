import random
money = 50000






















def gg(): # GUESSING GAME FOR THOSE WHO ARE READING ALSO 67
  
  
  lives = random.randint(5, 6)
  rn = random.randint(1, 100) 
  guess = int(input("Guess a Number Between 1 and 100!: "))
  if lives == 0:
    print("You Lost!")
    lives = -1
  while (lives > 0):
    if guess < rn:
      print("Lives Left:", lives)
      guess = int(input("Guess Higher!: "))
      lives -= 1
    elif guess > rn:
      print("Lives Left:", lives)
    
      guess = int(input("Guess Lower!: "))
      lives -= 1
    else:
      print("You Win!")
      break
  if lives == 0:
    print("You Lost!")
    lives = -1
gg()