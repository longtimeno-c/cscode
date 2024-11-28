import time
# Variables:
# arrayData = Array
# numToSearch = Int
# numberInArray = Int
# count = Int
# answer = Boolean
# yanswer = array
# nanswer = array
# inputNumber = int
# search = int

arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]


yanswer = ["Yes", "yes", "Y", "y"]
nanswer = ["No", "no", "N", "n"]

print('This is the array', arrayData)

def linearsearch(numToSearch):
    print("Beginning search...")
    numberInArray = len(arrayData)
    count = 0
    while (count < numberInArray):
        if numToSearch == arrayData[count]:
            print("Number has been found!")
            time.sleep(1)
            if count == 0:
                count =+1
            print("Has been found at position", count)
            return True
        else:
            print("Not in pass!")
            count += 1
    print("Number was not found!")
    return False

def BubbleSort():
    time.sleep(1)
    print('Sorting...')
    time.sleep(1)

    for i in range(len(arrayData) - 1):
        swapped = False
        for j in range(len(arrayData) - 1 - i):
            if arrayData[j] > arrayData[j + 1]:
                arrayData[j], arrayData[j + 1] = arrayData[j + 1], arrayData[j]
                swapped = True
        if not swapped:
            # Break early if no swaps were made
            arrayData

    # Output the sorted array
    print("Sorted Array:", arrayData)

    return

answer = False
while answer == False:
    search = input("Would you like to search for a numer using linear search? ")
    if search in yanswer:
        inputNumber = int(input("What number would you like to search for? "))
        print("Searching for...", inputNumber)
        linearsearch(inputNumber)
        answer = True
    elif search in nanswer:
        bubbleSortApprove = input("Would you like to sort the Array using Bubble sort?")
        if bubbleSortApprove in yanswer:
            BubbleSort()
        answer = True
    else:
        print("Cancelled")
        answer = True
