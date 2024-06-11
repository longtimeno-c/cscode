import random
import time 

Needed = 20
inPiggyBank = 10.50
extra = int(input("How much extra money do you have?"))
total = inPiggyBank + extra
if total >= Needed:
    print("We have enough :)")
else:
    print("Sorry we need more :(")
