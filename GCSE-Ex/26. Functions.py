import random
import time


def calcdouble(amount):
    amount = 2 * amount
    return amount

def calchalf(amount):
    amount = amount / 2
    return amount 

def tenmore(amount):
    amount = amount + 10
    return amount 
    

question = int(input("Number you want to double"))
answer = calcdouble(question)
answer1 = calchalf(question)
answer2 = tenmore(question)
print("Double", question,"is", answer)
time.sleep(1)
print()
print("Half of", question,"is", answer1)
time.sleep(1)
print()
print("Ten more of", question,"is", answer2)
