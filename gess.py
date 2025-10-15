import random



















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
 
  
  while (money > 0):
    dice = random.randint(1,100)
    money = money - bet
    if coc in ["over"]:
        risk = 100 - tar
    if coc in ["under"]:
        risk = tar - 1
    risk = risk / 100
    multiplier = 0.98 / risk
    print(multiplier)
  
    if (coc == "over"):
      if (dice > tar):
        money = money * multiplier
        
        
      
      
    elif coc == "under":
      print(49)
    
    else:
      ()
      
      
roll()


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
