import random

def chooseasuit(number):
    if number ==1:
        suit "hearts"
    elif == 2:
        suit "Diamonds"
    elif == 3:
        suit == "clubs"
    else:
        suit == "spades"
    return suit
def chooseavalue(number):
    if number == 11:
        value = "Jack"
    elif number == 12:
        value = "Queen"
    elif number == 13:
        value = "king"
    elif number == 1:
        value = "Ace"

    else:
        value = number
    return value

for counter in range(10):
    randomNum = random.randint(1,4)
    print(randomNum)
    suit = chooseasuit(randomNum)
    
