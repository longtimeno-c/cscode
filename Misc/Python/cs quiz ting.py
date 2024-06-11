#cs class conversation
#Convert the 0 into a number so we can add scores
score = 0
score = int(score)
#Max's assets

import time
import random

print ("Hi, my name is David Attenbrough and I watch Bird Programs")
print ("Do you like watching Bird Programs?")

while True:
    response = input("Hit 'yes' or 'no' for your answer\n")

    if response == "yes":
        score = score + 1
        break
    else:
        print("Incorrect!!! Try again.")

        while True:
            response = input("Hit 'yes' or 'no' for your answer\n")

            if response == "yes":
                score = score + 1
                stop = True
                break
            else:
                print("Incorrect!!! You ran out of your attempts")
                stop = True
                break
        if stop:
            break
print()
print("Your current score is " + str(score) + " out of 4")
print()
time.sleep(1)
print ("Great glad to hear you like watching Bird programs")
time.sleep(1)
print ("I beleive in Tristianity which is a religion that worships flipflops")
time.sleep(1)
print ("Do you support Tristianity?")

while True:
    response = input("Hit 'yes' or 'no' for your answer\n")

    if response == "yes":
        score = score + 1
        break
    else:
        print("Your a bit of a dissapointment! you have 1 attempt remaining")

        while True:
            response = input("Hit 'yes' or 'no' for your answer\n")

            if response == "yes":
                score = score + 1
                stop = True
                break
            else:
                print("Your a bit of a dissapointment! you have 0 attempts remaining")
                stop = True
                break
        if stop:
            break
print()
print("Your current score is " + str(score) + " out of 4")
print()
time.sleep(1)

print ("Nice to hear it! Not that you had a choice! :)")

time.sleep(1)
print()
V1 = input("so now that you have passed that short quiz what is your first name?")

if V1 == "Tristan" :
    print("You have the name of a brilliant man!")
    
elif V1 == "bob" or V1 == "Ben" :
    print("ur name sounds pretty dumb")

elif V1 == "Max" :
    print("Max ur just 'special' Boy")
    
else:
    print("Nice!")
print()   
time.sleep(1)
print()
V2 = input("And your Surname?")
if V2 =="Hill":
    print("You have a good name good sir")

elif V2 == "Walker":
    print("Bad name choice")

else:
    print("Good name")
print()
time.sleep(1)

full_name= V1 + V2

Sushi1 = input("So " + full_name + " what is your favourite Sushi?")

if Sushi1 == "no idea" or Sushi1 == "no Clue" :
    print("Thats not exactly Sushi now is it?")

elif Sushi1 == "temaki" or Sushi1 == "Gunkan Maki" or Sushi1 == "Narezushi" or Sushi1 == "Oshizushi" or Sushi1 == "Nigiri" or Sushi1 == "Toro" or Sushi1 == "futomaki" or Sushi1 == "anago" :
    print("That is the best kinds of Sushi!")
    score = score + 1

else:
    print("Imagine not knowing Sushi")

SRes = input ("Do you have a favorite Sushi resturant " +V1+ " ?")

if SRes == "no" or SRes == "not really" or SRes == "No"  :
    print("Thats a shame to be honest!")

elif SRes == "Kyoto Kitchens" or SRes == "Yo Sushi":
    print("ah we meet again")

elif SRes == "Yes" or SRes == "Sure" or SRes == "Sure" or SRes == "yeah" or SRes == "Yeah" :
    print("feel free to come back and share")

else:
    print("Nice! " +SRes+ " sounds great!")


time.sleep(1)
print()
print("Your current score is " + str(score) + " out of 4")
print()
time.sleep(1)
print ("Do you like pancakes?")

while True:
    response = input("Hit 'yes' or 'no' for your answer\n")

    if response == "yes":
        score = score + 1
        break
    else:
        print("Your a bit of a dissapointment! you have 1 attempt remaining")

        while True:
            response = input("Hit 'yes' or 'no' for your answer\n")

            if response == "yes":
                score = score + 1
                stop = True
                break
            else:
                print("Your a bit of a dissapointment! you have 0 attempts remaining")
                stop = True
                break
        if stop:
            break

time.sleep(1)
print()
print("Your current score is " + str(score) + " out of 4")
print()
time.sleep(1)
#This bit here needs some work....
print("You have now answered all the Questions!")
if str(score) == 4:
    print("Well done you got full marks!")

else:
    print("Close you nearly got there")

print()
time.sleep(1)

print("cya later alligator")

time.sleep(2)
exit()
