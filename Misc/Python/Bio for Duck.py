#Biograpgy for duck
import time
import random

print("This is a biography about my Duck")
time.sleep(2)
#1st rotation
V1 = input("Please type one of the following, Age, Name, Job ")
print()
if V1 == "Age" :
    print("My Duck is 37")
    
elif V1 == "Name" :
    print("My Ducks name is The Duckter")

elif V1 == "Job" :
    print("My Duck is a Duckter")

else:
    print("That isnt one of the selected topics")

time.sleep(2)
print()
#2nd rotation

V2 = input("Please type one of the following if you want to learn more about my Duck, Age, Name, Job ")
print()
if V2 == "Age" :
    print("My Duck is 37")
    
elif V2 == "Name" :
    print("My Ducks name is The Duckter")

elif V2 == "Job" :
    print("My Duck is a Duckter")

else:
    print("That isnt one of the selected topics")

time.sleep(2)
print()
#3rd rotation


V3 = input("Please type one of the following if you want to learn more about my Duck, Age, Name, Job ")

if V3 == "Age" :
    print("My Duck is 37")
    
elif V3 == "Name" :
    print("My Ducks name is The Duckter")
    
elif V3 == "Job" :
    print("My Duck is a Duckter")

else:
    print("That isnt one of the selected topics")

FF = input("What do you think The Duckters Favorite film is? ")
print()
if FF == "Duckter Who" :
    print("How did you guess?")
    
elif FF == "The Mighty Ducks" :
    print("This one is the best!!")

elif FF == "Duck Duck Goose" :
    print("eyyy how did you guess?")
else:
    print("No you were close but 'Duck Duck Goose' is one of his favorites!")

print()
print()
time.sleep(2)
print("Here you can see what the Duckter looks like:)")
print()
print("Lemme Just generate a link")
import itertools
import threading
import sys

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(3)
done = True
print()
time.sleep(1)
print()
print("https://drive.google.com/file/d/1CvtoGPx-a3rt2siBJfNgi3g1WFwOnawh/view?usp=sharing")
print()
print("because loading it in here is hard :)")
time.sleep(10)
import turtle

width = 800
height = 500
 
window = turtle.Screen() 
window.setup(width, height) 
window.title("Tristianity")

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
text = turtle.Turtle() 
text.color("black") 
text.penup() 
text.setposition(-100,170) 
text.write("Merry Thristmans", font=("Apple Chancery", 30, "bold"), align="center") 
text.setposition(130, 140) 
text.color("dark blue") 
text.write("Tesus", font=("Avenir", 30, "bold"), align="right") 
text.color("black") 
text.write("Thrist", font=("Avenir", 30, "normal"), align="left") 
text.setx(50) 
text.write("from", font=("Apple Chancery", 20, "bold"), align="right")
text.hideturtle()
time_delay = 0 
