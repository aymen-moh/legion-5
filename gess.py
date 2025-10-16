import random
import time

def blackjack():
  while True:
    cards = (1, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
    rd = random.randint(0, 12) # random deck yall
    fh = 0   # first hand   #
    sh = 0   # second hand #
    card_selection = cards[ud] # kool
    hit = False
    stand = False
    while (ud < 21):


blackjack()










def roll():
  money = 50000
  bet = int(input("Enter The Amout of Money You Can lose: ")) 
  while (money < bet):
    print("You Only Have:", money)
    bet = int(input("Bet: ")) 
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
  while True:
    guess = 0
    money = 50000
    again = ""
    multiplier = 36.67
  
    bet = int(input(""))
    lives = 6
    rn = random.randint(1, 100) 
    guess = int(input(f"Guess a Number Between 1 and 100!: {rn} "))
    win = False
    bet = int(input("Enter The Amout of Money You Can lose: ")) 
  while (money < bet):
    print("You Only Have:", money)
   
    while (lives > 0) and not win:
      
    
      if guess < rn:
        multiplier = round(multiplier / 2, 2)
        print("Lives Left:", lives)
        print(f"Current multiplier: {multiplier}")
        guess = int(input("Guess Higher!: "))
        
        
        lives -= 1
      elif guess > rn:
        multiplier = round(multiplier / 2, 2)
        print("Lives Left:", lives)
        print(f"Current multiplier: {multiplier}")
        guess = int(input("Guess Lower!: "))
        lives -= 1
        
      else:
        money += round(bet * multiplier, 0)
        print(f"You Win! YOU WON {bet * multiplier} WITH {multiplier}x Your bet!")
        win = True
        
        
      if lives == 0:
        money -= bet
        print("You Lost!")
        print(f"The Number Was: {rn}")
        print(f"YOU HAVE {money} now! ")
        again = 67
    if money <= 0:
      print("You Are Broke!")
    again = input("Press Anything To Play Again!")
    win = False