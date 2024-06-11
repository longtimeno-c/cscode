answer_yes = ["Yes", "Y", "yes", "y"]
answer_no = ["No", "N", "no", "n"]
#This is the first question
print("""
WELCOME! LET'S START THE ADVENTURE

You are standing outside of your house and you see a man running towards you and asking for urgent shelter.

Will you provide shelter to him. (Yes / No)
""")

ans1 = input(">>")

#The answer to the first question changes the response
#Answer 2 is for no
#Answer 1 is for yes

if ans1 in answer_yes:
    print("\nAfter 2 minutes, the Police came to your house, and ask you that whether the thief is in your house or not. Will you say (Yes / No)\n")

    ans2 = input(">>")
   
#This is the second response V and the question was placed in ans1 ^


    
    if ans2 in answer_yes:
        print("\nYou are an honest person. He was a thief & You won the Game")


        
#This is if you said yes to the second question and hid the theif V


        
    elif ans2 in answer_no:
        print("\nYou helped a thief. Now, go to Jail. GAME OVER")


        
#This is if the text inputted is in the wrong format for the second Question

        
    else:
        print("\nYou typed the wrong input. GOODBYE!")

#This is the alternative 2nd question if you typed no to hiding the theif  


elif ans1 in answer_no:
    print("\nNow, he is trying to kill you. Will, you knock him down? (Yes / No)\n")

#This now has its own following questions and decisions 

    ans3 = input(">>")

# V This is if you said to knocking down the theif V 


    if ans3 in answer_yes:
        print("\nCongrats! He was a thief & You helped the police to catch him with your bravery.")


# V This is if you dont knock down the thief V

    elif ans3 in answer_no:
        print("\nSorry! You are dead. He was a thief & He killed you. GAME OVER")


#and again this is for the wrong input of the variable 2nd question 

    else:
        print("\nYou typed the wrong input. GOODBYE!")



        
#This is if the format of the first answer didnt match the above. V


else:
    print("\nYou typed the wrong input. GOODBYE!")
