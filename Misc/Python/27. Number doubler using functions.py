def calcdouble(amount):
    amount = 2 * amount
    return amount

question = int(input("Number you want to double"))
answer = calcdouble(question)
print("Double", question,"is", answer)
