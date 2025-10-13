import random
import time

money = 1000

while money > 0:
    chance = 0
    multiplier = 0

    print("You Have:", money, "<-- Dollars")
    bet = int(input("Enter The Amount Of money you want to gamble: "))
    while (money < bet):
        print("You Don't Have Enough Funds! Balance: ---> ", money)
        bet = int(input("Enter The Amount Of money you want to gamble: "))
    print("this is a roll gambling game, there is a \n random number generator from 1 to 100 you have to pick a target, and guess if its \n going to be higher or lower")
    target = int(input("target:"))
    while target > 97 or target < 4:
      target = int(input("Please Choose Numbers Between 3-97!"))
    choice = input("Choose Over or Under")
    while True:
        if choice in ["over", "under"]:
            break
        else:
            choice = input("PLEASE choose only over or under")
            break
    if choice in ["over"]:
        chance = 100 - target
    if choice in ["under"]:
        chance = target - 1
    chance = chance / 100
    multiplier = 0.98 / chance

    print(target, choice, "Rolling...")
    roll = random.randint(1, 100)
    time.sleep(1) 

    print("Rolled", roll)
    if choice in ["over"]:
        if (roll > target):
            print("You Won!")
            money += round(bet * multiplier) - bet
            multiplier = round(multiplier, 2)
            print(money, " With ", multiplier, "x multiplier!", sep="")
        else:
            print("You Lost!")
            money -= bet
            print("You Have", money, "Now")
    elif choice in ["under"]:
        if (roll < target):
            print("You Won!")
            money += round(bet * multiplier) - bet
            multiplier = round(multiplier, 2)
            print(money, " With ", multiplier, "x multiplier!", sep="")
        else:
            print("You Lost!")
            money -= bet
            print("You Have", money, "Now")

print("GAME OVER! You're broke!")
jsjsjs