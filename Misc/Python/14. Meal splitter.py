#meal splitter


print("*************************************")
print("Hallo, welcome to the meal splitter!")
print("*************************************")
pppay = int(input("How many people need to pay?"))
bill = int(input("How much was the bill?"))


if bill < 20:
    bill = bill + 5
    price = str(bill/pppay)

else:
    bill = bill * 1.2
    price = str(bill/pppay)

print("Each person should pay: ", price)
