import random
import time


answer = input("Would you like to generate a random number?")


if answer == ("yes"):
    time.sleep(1)
    number = random.randint(1,10)
    print(number)
    
else:
    print("Sorry bye")

time.sleep(1)
