# create a calculator program which takes two numbers as variables and passes them as parameters 
# to the different functions which are separate add, minus, divide, times, mod and div.
# Then returns the answers to main part of code and outputs
panswer = ["*", "/", "+", "-"]

def Add(firstNum, secondNum):
    print("Adding")
    value = firstNum + secondNum
    return value
def Subtract(firstNum, secondNum):
    print("Subtract")
    value = firstNum - secondNum
    return value
def Multiply(firstNum, secondNum):
    print("Multiply")
    value = firstNum * secondNum
    return value
def Divide(firstNum, secondNum):
    print("Divide")
    value = firstNum / secondNum
    return value


def __main__():
    valid = False
    firstNum = int(input("Enter the first number: "))
    secondNum = int(input("Enter the second number: "))
    while valid == False:
        typeofCalc = input("Enter form of calculation using *, /, +, - : ")
        if typeofCalc in panswer:
            valid = True
    if typeofCalc == "+":
        value = Add(firstNum, secondNum)
    elif typeofCalc == "-":
        value = Subtract(firstNum, secondNum)
    elif typeofCalc == "*":
        value = Multiply(firstNum, secondNum)
    elif typeofCalc == "/":
        value = Divide(firstNum, secondNum)

    print("Answer is!", value)
        
    
__main__()
