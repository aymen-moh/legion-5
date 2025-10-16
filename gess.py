import random
import time


def blackjack():
  playing = True
  while playing:
    playing = False
    firsthand = 0
    secondhand =0
    thirdhand = 0
    fourthhand = 0
    fifthhand = 0
    sixthhand = 0
    seventhhand = 0
    FBH = 0
    SBH = 0
    card_deck = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11)
    FirstPull = True
    SecondPull = False
    ThirdPull = False
    FourthPull = False
    FifthPull = False
    SixthPull = False
    
    HitOrStand = ""
    s = "succsess message"
    while FirstPull:
      
        RandomNumber = random.randint(0, 12)
        firsthand = card_deck[RandomNumber]
        RandomNumber = random.randint(0, 12)
        secondhand = card_deck[RandomNumber]
        RandomNumber = random.randint(0, 12)
        FBH = card_deck[RandomNumber]
        print(f"Your Hand: {firsthand}, {secondhand} Total: {firsthand + secondhand} \n Dealer is Showing {FBH}") 
        FirstPull = False
        SecondPull = True
        
        
    while SecondPull:
      HitOrStand = input("Type \"hit\" To Hit And \"stand\" To Stand")
      if HitOrStand in ["hit"]:
        RandomNumber = random.randint(0, 12)
        thirdhand = card_deck[RandomNumber]
        print(f"Your Hand: {firsthand}, {secondhand}, {thirdhand} Total: {firsthand + secondhand + thirdhand} \n Dealer is Showing {FBH}")
        SecondPull = False
        ThirdPull = True# SLEF NOTE: DONT FORGET TO IMPLEMENT THE STAND SYSTEM AND THE BUST SYSTEM IF YOU READ THIS GET 67'ed
    while ThirdPull:
      userhandtotal = firsthand + secondhand + thirdhand + fourthhand + sixthhand + seventhhand
      HitOrStand = input("Type \"hit\" To Hit And \"stand\" To Stand \n Dealer is Showing {FBH}")
      if HitOrStand in ["hit"]:
        RandomNumber = random.randint(0, 12)
        fourthhand = card_deck[RandomNumber]
        print(f"Your Hand: {firsthand}, {secondhand}, {thirdhand}, {fourthhand} Total: {firsthand + secondhand + thirdhand + fourthhand}")
        FourthPull = True
        ThirdPull = False
    while FourthPull:
      HitOrStand = input("Type \"hit\" To Hit And \"stand\" To Stand \n Dealer is Showing {FBH}")
      if HitOrStand in ["hit"]:
        RandomNumber = random.randint(0, 12)
        fifthhand = card_deck[RandomNumber]
        print(f"Your Hand: {firsthand}, {secondhand}, {thirdhand}, {fourthhand}, {fifthhand} Total: {firsthand + secondhand + thirdhand + fourthhand + fifthhand}")
        FourthPull = False
        FifthPull = True
    while FifthPull:
      HitOrStand = input("Type \"hit\" To Hit And \"stand\" To Stand \n Dealer is Showing {FBH}")
      if HitOrStand in ["hit"]:
        RandomNumber = random.randint(0, 12)
        sixthhand = card_deck[RandomNumber]
        print(f"Your Hand: {firsthand}, {secondhand}, {thirdhand}, {fourthhand}, {fifthhand}, {sixthhand} Total: {firsthand + secondhand + thirdhand + fourthhand + fifthhand + sixthhand}")
        FifthPull = False
        SixthPull = True
    while SixthPull:
      HitOrStand = input("Type \"hit\" To Hit And \"stand\" To Stand \n Dealer is Showing {FBH}")
      if HitOrStand in ["hit"]:
        RandomNumber = random.randint(0, 12)
        seventhhand = card_deck[RandomNumber]
        print(f"Your Hand: {firsthand}, {secondhand}, {thirdhand}, {fourthhand}, {fifthhand}, {sixthhand}, {seventhhand} Total: {firsthand + secondhand + thirdhand + fourthhand + fifthhand + sixthhand + seventhhand}")
        SixthPull = False
    
    
      
      
      
      

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