#calculator

def adding():
    num1 = int(input("What would u like to add?"))
    num2 = int(input("What would you like to add to that?"))
    answer = num1 + num2
    return answer


def subtract():
    num1 = int(input("what would you like to subtract?"))
    num2 = int(input("What would you like to subtract by?"))
    answer = num1 - num2
    return answer

def multiply():
    num1 = int(input("what would you like to multiply?"))
    num2 = int(input("What would you like to multiply by?"))
    answer = num1 * num2
    return answer

def divide():
    num1 = int(input("what would you like to divide?"))
    num2 = int(input("What would you like to divide by?"))
    answer = num1 / num2
    return answer


method = input("Would you like to add/subtract or divide or multiply?")

if method == ("add"):
    answer1 = adding()
    print(answer1)

elif method == ("subtract"):
    answer2 = subtract()
    print(answer2)

elif method == ("mutiply"):
    answer3 = multiply()
    print(answer3)

elif method == ("divide"):
    answer4 = divide()
    print(answer4)

else:
    print("error")
