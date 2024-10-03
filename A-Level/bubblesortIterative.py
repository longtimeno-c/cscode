# Function to perform iterative bubble sort
def bubble_sort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
        # Flag to check if any swapping occurred
        swapped = False
 
        # Last i elements are already sorted, so skip them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
 
        # If no elements were swapped, the array is already sorted
        if not swapped:
            break
 
# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
 
# Perform bubble sort
bubble_sort(arr)
 
# Print the sorted array
print("Sorted array:", arr)