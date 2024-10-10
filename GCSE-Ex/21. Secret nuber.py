#secret number

import random

secret_number = random.randint(0,100)
number = int(input("Enter your guess"))

while number != secret_number:
    print("Sorry your number is incorrect")
    if number < secret_number:
        print("Try higher...")
        number = int(input("guess again"))
    else:
        print("Try a lower number")
        number = int(input("guess again"))
                     
print("You guessed correct! My nunber was", secret_number)

