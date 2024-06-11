#binary search
import random

max_number = 10
min_number = 0
searchingfor = 7
count_number_searches = 0
searches = 0

midpoint = ((max_number + min_number)/2)
while midpoint != searchingfor:
    if searchingfor < midpoint:
        max_number = midpoint -1

    else:
        minnumber = midpoint + 1
    searches =+ searches
    print("My Current number is", max_number, "Current midpoint is", midpoint)
count_number_searches = count_number_searches + 1
print(midpoint, " Searches performed =", searches)
