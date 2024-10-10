import random

choice = input("Choose an (I)nsult or a (C)ompliment")

insult = ["Your fat","Your weird", "Your crazy"]
compliment = ["Your amazing","Your Funny", "Your So hot"]

randomnumber = random.randint(0,2)

if choice == ("I"):
    print (insult[randomnumber])

elif choice == ("C"):
    print (compliment[randomnumber])
else:
    print("Error")
               
