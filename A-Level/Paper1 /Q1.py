# Global variables
DataStored = [0] * 20  # 1D array with space for up to 20 integers
NumberItems = 0        # Quantity of items in the array

def Initialise():
    global DataStored, NumberItems
    while True:
        try:
            NumberItems = int(input("Enter the quantity of numbers (1-20): "))
            if 1 <= NumberItems <= 20:
                break
            else:
                print("Please enter a number between 1 and 20.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    for i in range(NumberItems):
        while True:
            try:
                DataStored[i] = int(input(f"Enter number {i+1}: "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

def BubbleSort():
    global DataStored, NumberItems
    for i in range(NumberItems - 1):
        for j in range(NumberItems - 1 - i):
            if DataStored[j] > DataStored[j + 1]:
                DataStored[j], DataStored[j + 1] = DataStored[j + 1], DataStored[j]

def BinarySearch(DataToFind):
    global DataStored, NumberItems
    low = 0
    high = NumberItems - 1
    
    while low <= high:
        mid = (low + high) // 2
        if DataStored[mid] == DataToFind:
            return mid
        elif DataStored[mid] < DataToFind:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

if __name__ == "__main__":
    NumberItems = 0
    Initialise()
    print("Contents of DataStored before sorting:", DataStored[:NumberItems])
    BubbleSort()
    print("Contents of DataStored after sorting:", DataStored[:NumberItems])
    
    DataToFind = int(input("Enter number to search for: "))
    index = BinarySearch(DataToFind)
    if index != -1:
        print(f"Number {DataToFind} found at index {index}.")
    else:
        print(f"Number {DataToFind} not found.")