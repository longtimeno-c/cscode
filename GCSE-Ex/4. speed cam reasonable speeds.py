#speed camera edited reasonable speed limits
import time

print("******************************")
print("Hello, please enter your speed")
print("******************************")
speed = float(input("Enter speed: "))

if speed >= 150 or speed <= 0:
    print("Re-enter a valid number")
    speed2 = float(input("Enter speed: "))

    if speed >= 150 or speed <= 0:
        print("Re-enter a valid number")
        speed3 = float(input("Enter speed: "))

    elif speed2 >= 75:
        print("Issue a fine this person is speedyyyyyy")

    elif speed2 >= 70 :
        print("Issue a warning")
        
    else:
        print("No action")
    

elif speed >= 75:
    print("Issue a fine this person is speedyyyyyy")

elif speed >= 70 :
    print("Issue a warning")

else:
    print("No action")
