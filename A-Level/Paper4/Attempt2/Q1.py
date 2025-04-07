def AskUserInput():
    while True:
        search = input('Enter number to search for: ')
        if search.isdigit():
            number = int(search)
            if 0 <= number <= 100:
                return number
            else:
                print('That is not a valid number!\nChoose a number between 0 and 100.')
        else:
            print('That is not a valid number!\nChoose a number between 0 and 100.')

def PrintArray(DataArray):
    print(DataArray) # Print array

def Readfile():
    DataArray = []
    with open('Data.txt', 'r') as file: # Open the file
        for line in file: # For every line in the file... for i in j
            if line.strip().isdigit(): # Remove blank spaces, ensure only digits
                DataArray.append(int(line.strip())) # Append integers to array
                if len(DataArray) == 25: # Ensure only 25 values added
                    break
    return DataArray

def LinearSearch(array, target):
    positions = []
    for index in range(len(array)):
        if array[index] == target:
            positions.append(index)
    return positions

def main():
    search = AskUserInput()
    data = Readfile()
    PrintArray(data)
    occurences = LinearSearch(data, search)
    if occurences:
        print(f"Value {search} found at positions: {occurences}")
        print(f"Total occurrences: {len(occurences)}")
    else:
        print(f"Value {search} not found in the array.")
main()
