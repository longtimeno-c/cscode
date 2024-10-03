import random
import psutil
import os
import time
import matplotlib.pyplot as plt

def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024  # Convert to MB

def merge_sort_iterative(arr, memory_usage, timestamps):
    # Get the length of the array
    n = len(arr)
    # Initial size of the subarrays to be merged
    current_size = 1
 
    # Outer loop for merging subarrays of size current_size
    while current_size < n:
        # Starting index of the left subarray
        left_start = 0
        # Merging subarrays in pairs
        while left_start < n - current_size:
            # Midpoint of the left subarray
            mid = left_start + current_size - 1
            # Ending index of the right subarray
            right_end = min(left_start + 2 * current_size - 1, n - 1)
 
            # Merge the subarrays arr[left_start...mid] and arr[mid+1...right_end]
            merge(arr, left_start, mid, right_end)
 
            # Move to the next pair of subarrays
            left_start += 2 * current_size
 
        # Increase the current size of the subarrays
        current_size *= 2
 
        # Track memory usage after each pass
        memory_usage.append(get_memory_usage())
        timestamps.append(time.time())
 
def merge(arr, left_start, mid, right_end):
    # Create temporary arrays for left and right subarrays
    left_subarray = arr[left_start:mid + 1]
    right_subarray = arr[mid + 1:right_end + 1]
 
    # Initial indexes for left subarray, right subarray, and main array
    left_index = 0
    right_index = 0
    main_index = left_start
 
    # Merging the temporary arrays back into the main array
    while left_index < len(left_subarray) and right_index < len(right_subarray):
        if left_subarray[left_index] <= right_subarray[right_index]:
            arr[main_index] = left_subarray[left_index]
            left_index += 1
        else:
            arr[main_index] = right_subarray[right_index]
            right_index += 1
        main_index += 1
 
    # Copy any remaining elements of left_subarray, if any
    while left_index < len(left_subarray):
        arr[main_index] = left_subarray[left_index]
        left_index += 1
        main_index += 1
 
    # Copy any remaining elements of right_subarray, if any
    while right_index < len(right_subarray):
        arr[main_index] = right_subarray[right_index]
        right_index += 1
        main_index += 1
 
# Generate a dataset of 10,000,000 random integers
arr = [random.randint(1, 10000000) for _ in range(10000000)]

memory_usage = []
timestamps = []
start_time = time.time()

print(f"Memory usage before sorting: {get_memory_usage():.2f} MB")

# Perform iterative merge sort with memory tracking
merge_sort_iterative(arr, memory_usage, timestamps)

print(f"Memory usage after sorting: {get_memory_usage():.2f} MB")

# Print the first 10 elements of the sorted array
print("First 10 elements of the sorted array:", arr[:10])
print("Length of the sorted array:", len(arr))

# Plot the memory usage graph
plt.figure(figsize=(10, 6))
plt.plot([t - start_time for t in timestamps], memory_usage)
plt.title("Memory Usage During Iterative Merge Sort")
plt.xlabel("Time (seconds)")
plt.ylabel("Memory Usage (MB)")
plt.grid(True)
plt.show()