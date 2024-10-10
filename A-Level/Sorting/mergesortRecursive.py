import random
import psutil
import os
import time
import matplotlib.pyplot as plt

def merge_sort_recursive(arr):
    # Base case: if the array has one or zero elements, it's already sorted
    if len(arr) <= 1:
        return arr
 
    # Find the middle index
    mid = len(arr) // 2
 
    # Recursively sort the left and right halves
    left_half = merge_sort_recursive(arr[:mid])
    right_half = merge_sort_recursive(arr[mid:])
 
    # Merge the sorted halves
    return merge(left_half, right_half)
 
def merge(left, right):
    sorted_array = []
    left_index, right_index = 0, 0
 
    # Merge the two halves into a sorted array
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1
 
    # If there are any remaining elements in left, add them
    while left_index < len(left):
        sorted_array.append(left[left_index])
        left_index += 1
 
    # If there are any remaining elements in right, add them
    while right_index < len(right):
        sorted_array.append(right[right_index])
        right_index += 1
 
    return sorted_array
 
# Function to get current memory usage
def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024  # Convert to MB

def merge_sort_recursive_with_memory_tracking(arr, memory_usage, timestamps):
    current_memory = get_memory_usage()
    memory_usage.append(current_memory)
    timestamps.append(time.time())

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort_recursive_with_memory_tracking(arr[:mid], memory_usage, timestamps)
    right_half = merge_sort_recursive_with_memory_tracking(arr[mid:], memory_usage, timestamps)

    return merge(left_half, right_half)

# Generate a dataset of 1,000,000 random integers (reduced for faster execution)
arr = [random.randint(1, 1000000) for _ in range(1000000)]

memory_usage = []
timestamps = []
start_time = time.time()

print(f"Memory usage before sorting: {get_memory_usage():.2f} MB")

# Perform recursive merge sort with memory tracking
sorted_arr = merge_sort_recursive_with_memory_tracking(arr, memory_usage, timestamps)

print(f"Memory usage after sorting: {get_memory_usage():.2f} MB")

# Print the first 10 elements of the sorted array
print("First 10 elements of the sorted array:", sorted_arr[:10])
print("Length of the sorted array:", len(sorted_arr))

# Plot the memory usage graph
plt.figure(figsize=(10, 6))
plt.plot([t - start_time for t in timestamps], memory_usage)
plt.title("Memory Usage During Recursive Merge Sort")
plt.xlabel("Time (seconds)")
plt.ylabel("Memory Usage (MB)")
plt.grid(True)
plt.show()