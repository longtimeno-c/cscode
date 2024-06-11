answer_yes = ["Yes", "Y", "yes", "y"]
answer_no = ["No", "N", "no", "n"]

import time

print("""
WELCOME! LET'S START THE ADVENTURE

You are standing outside of your house and you see a man running towards you and asking for urgent shelter.

Will you provide shelter to him. (Yes / No)
""")

ans1 = input(">>")

print("Loading.")
print("Loading..")
print("Loading...")
print("Done!")

time.sleep(1)

print()
if ans1 in answer_yes:
    print("\nAfter 2 minutes, the Police came to your house, and ask you that whether the thief is in your house or not. Will you say (Yes / No)\n")

    ans2 = input(">>")
    import itertools
    import threading
    import sys

    done = False
    #here is the animation
    def animate():
        for c in itertools.cycle(['.', '..', '...', '....']):
            if done:
                break
            sys.stdout.write('\rloading ' + c)
            sys.stdout.flush()
            time.sleep(0.1)#speed of loading 0.01 is a good one
        sys.stdout.write('\rDone!     ')

    t = threading.Thread(target=animate)
    t.start()

    #long process here
    time.sleep(0.8)
    done = True
    
    print()
    print()
    time.sleep(1)


    
    if ans2 in answer_yes:
        print("\nYou are an honest person. He was a thief & You won the Game")

    elif ans2 in answer_no:
        print("\nYou helped a thief. Now, go to Jail. GAME OVER")
        
    else:
        print("\nYou typed the wrong input. GOODBYE!")



elif ans1 in answer_no:
    print("\nNow, he is trying to kill you. Will, you knock him down? (Yes / No)\n")

    ans3 = input(">>")
    
    if ans3 in answer_yes:
        print("\nCongrats! He was a thief & You helped the police to catch him with your bravery.")

    elif ans3 in answer_no:
        print("\nSorry! You are dead. He was a thief & He killed you. GAME OVER")
        
    else:
        print("\nYou typed the wrong input. GOODBYE!")



else:
    print("\nYou typed the wrong input. GOODBYE!")


print()
print()
print("Would you like to continue to the next round?")
print("Type yes/no")

round2 = input(">>")

answerA = ["A","a"]
answerB = ["B","b"]

if round2 in answer_yes:
    print("LOADING ROUND 2")
    time.sleep(0.5)
    print("Loading.")
    time.sleep(0.5)
    print("Loading..")
    time.sleep(0.5)
    print("Loading...")
    time.sleep(0.5)
    print("Loading.")
    time.sleep(0.5)
    print("Loading..")
    time.sleep(0.5)
    print("Loading...")
    print()
    print("DONE!")
    time.sleep(0.5)
    
    print()
    print("\You are walking around the city when you hear a scream. A man in his early 20's runs out of an alley. Do you: (A.) go and investigate? Or (B.) you run after the man. (A/B) \n")

    ans4 = input(">>")

    if ans4 in answerA:
        print("You go to investigate but are stopped to find a corpse bleeding out onto the street")
        print()
        time.sleep(2)
        print("You panic and run but run into a figure standing behind you")
        print("The figure raises a dark above his head and brings it down on your skull")
        time.sleep(1)
        print("It goes dark")
        print()
        print()
        print()
        print("ROUND LOST")
        
    elif ans4 in answerB:
        print("You make a good choice")
        print()
        print("You folow the man")
        print("Gunshots can be heard behind you")
        time.sleep(0.5)
        print("You escape with the man and survive another day")
        time.sleep(1)
        print()
        print("GAME OVER")
        

elif round2 in answer_no:
    print("Okay thank you for playing")
     

else:
    print("You have typed an incorrect format")

    







