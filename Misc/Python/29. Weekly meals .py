## Meal
count = 0
total = 0
day = 0
balance = int(input("Input your bank balance:"))

while count <= 5:
    day = day +1
    print("Day:",day)
    d1 = int(input("The cost of the first drink:"))
    d2 =int(input("The cost of the second drink:"))
    m1 = int(input("The cost of the meal:"))
    total = total + d1 + d2 + m1
    count = count +1

print()
print("Total cost of meals:",total)
    

cost = balance - total

print()
if cost <= 0:
    print("Cannot afford")
else:
    print("The cost of meal is:",total)
    print("Money left is:",cost)

