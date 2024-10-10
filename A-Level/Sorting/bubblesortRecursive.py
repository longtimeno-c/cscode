# Function to perform recursive bubble sort
def bubble_sort_recursive(arr, n=None):
    # Initialize n on the first call
    if n is None:
        n = len(arr)
 
    # Base case: If the size of the array is 1, it is sorted
    if n == 1:
        return
 
    # Perform one pass of bubble sort
    for i in range(n - 1):
        # Swap if the element found is greater than the next element
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
 
    # Recursive call for the remaining array
    bubble_sort_recursive(arr, n - 1)
 
# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
 
# Perform bubble sort
bubble_sort_recursive(arr)
 
# Print the sorted array
print("Sorted array:", arr)