#quiz question 2
answer = input("What is the capital of Italy")
answer = answer.title()
Counter = 1

while answer != "Rome":
    answer= input("Incorrect,Try again:")
    answer = answer.title()
    Counter = Counter + 1

print("correct well done!")
print("You had ",Counter,"attempts")
