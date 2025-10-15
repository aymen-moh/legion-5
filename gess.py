import random
import time



def roll():
  money = 50000
  bet = int(input("Enter The Amout of Money You Can lose: ")) 
  while (money < bet):
    print("You Only Have:", money)
    bet = int(input(""))
    
  tar = int(input("Choose a Target: "))
  coc = input("Choose Over or Under: ")
  while (coc != "over") and (coc != "under"):
    coc = input("PLEASE CHOOSE EITHER \"over\" OR \"under\": ")
  multiplier = 0 
  risk = 0
  replay = ""
 
  
  while (money > 0):
    money = money - bet
    time.sleep(0.910) 
    dice = random.randint(1,100)
    print("Rollin'...")
    print("ROLLED:", dice)
    if coc in ["over"]:
        risk = 100 - tar
    if coc in ["under"]:
        risk = tar - 1
    risk = risk / 100
    multiplier = round(0.98 / risk, 2)
  
    if (coc == "over"):
      if (tar < dice):
        money = round(money + bet * multiplier,)
        print(f"----YOU WON---- {money} With {multiplier}x Multiplier!")
        print("")
        
      else:
        print(f"------YOU LOST------ you lost {bet} dollars and have {money} left")
        print("")
    if (coc == "under"):
      if (tar > dice):
        money = round(money + bet * multiplier,)
        print(f"----YOU WON---- {money} With {multiplier}x Multiplier!")
        print("")
        
      else:
        print(f"------YOU LOST------ you lost {bet} dollars and have {money} left")
        print("")
    if (money < 0):
        print("YOU LOST ALL OF IT AND YOU ARE NOW IN DEBT!")
    elif (money == 0):
        print("YOU LOST ALL OF IT!")
    if (money > 0):
      replay = input("Press Anything To Play Again")


def gg(): # GUESSING GAME FOR THOSE WHO ARE READING ALSO 67
  multiplier = 24
  money = 50000
  lives = 5
  rn = random.randint(1, 100) 
  guess = int(input("Guess a Number Between 1 and 100!: "))
  if lives == 0:
    print("You Lost!")
    lives = -1
  while (lives > 0):
    if guess < rn:
      multiplier = round(multiplier / 2,)
      print("Lives Left:", lives)
      print(f"Current multiplier: {multiplier}")
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
