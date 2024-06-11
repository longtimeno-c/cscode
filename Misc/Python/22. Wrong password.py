#Password checker limit
attempt = input("Please enter your password: ")
attempt = attempt.title()
Limit = 1

if Limit <= 5:
    while attempt != "12345":
        attempt = input("Incorrect try again: ")
        attempt = attempt.title()
        Limit = Limit +1

elif Limit > 5:
    print("You have entered the wrong password too many times")

else:
    print("error")

print("Well done that is correct")
    
