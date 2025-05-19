# Bubble sort iterative.

# randomNum = [0,4,5,34,2,5,8,4,1,6,9,5,3,10]


# def bubble ():
#     for i in range (len(randomNum)):
#         # print("This is i", i)
#         for j in range (len(randomNum) - 1):
#             # print("This is j", j)
#             if randomNum[j] > randomNum[j+1]:
#                 temp = randomNum[j]
#                 # print("Temp is ", temp)
#                 randomNum[j] = randomNum[j+1]
#                 randomNum[j+1] = temp
# bubble()
# print(randomNum)

# def linearSearch():
#     searchNum = int(input("What are you searching for? "))
#     for i in range (len(randomNum)):
#         if randomNum[i] == searchNum:
#             print("Number found term:", i+ 1)
#         else:
#             print("Number not found")


# linearSearch()
        

# a carsalesman wants a program where he can input how many sales he made that month, 
# he then wants to work out the total he made for the month in sales, the average, 
# the biggest sale and smallest sale (do this without a list and then with a list) 
# so two program output the answers

totalMonth= 0
averageMonth = 0
biggestSale = 0
smallestSale = 1000
sales = []

def findAverage(sales):
    for i in range (len(sales)):
        total =+ sales[i]
        averageMonth = total / (len(sales))
    return averageMonth

def __main__(biggestSale, smallestSale):
    numSales = int(input("Enter number of sales: "))
    for i in range (numSales):
        sale = int(input("Enter sale value: "))
        sales.append(sale)
        if sale >= biggestSale:
            biggestSale = sale
        if sale <= smallestSale:
            smallestSale = sale
    print(biggestSale)
    print(smallestSale)

    findAverage(sales)


__main__(biggestSale, smallestSale)