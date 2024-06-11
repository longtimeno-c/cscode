#concatenating text

import time 

#age = 14

#print("Kumar " + " Ahmad are " + str(age) + "years old")

#animal

animal = input("Enter the name of an animal: ") #getting name of animal
vovels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

if animal[0] in vovels:
    description = input("How would you describe an " + animal + "?") #finding descrip
    print ("An",animal,"is",description) #orinting info above

    

else:
    description = input("How would you describe a " + animal + "?") #finding descrip
    print("An ",animal,"is",description) #orinting info above


print("you will find it under",animal[0],"in the dictionary") #getting first letter to find in dictionary

