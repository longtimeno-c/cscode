# Bubble sort implementation
numcount = int(input("How many numbers are there? "))
array = []

# Input the numbers
for _ in range(numcount):
    array.append(int(input("Enter a single digit number: ")))

print("Original Array:", array)

# array = array.sort

# Bubble sort - main bit
for i in range(len(array) - 1):
    swapped = False
    for j in range(len(array) - 1 - i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            swapped = True
    if not swapped:
        # Break early if no swaps were made
        break

# Output the sorted array
print("Sorted Array:", array)