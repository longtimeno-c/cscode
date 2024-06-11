#quiz question

answer = input("What is the capital of France?")

answer = answer.title()

while answer != "Paris":
    answer = input("Incorrect, try again")
    answer = answer.title()

print("Correct! Well done!")

