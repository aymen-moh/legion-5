import random
import time 

roll = 0
money = 10000
while (money > 0):
  bet = int(input("Enter The Amount Of Money You Are Willing To Gamble (lose) Note, there is a 3% house edge: "))
  money = money - bet
  roll = random.randint(1, 100)
  if (roll <= 45):
    print("You Win! --- 2x")
    money = money + bet * 2
    print(money)