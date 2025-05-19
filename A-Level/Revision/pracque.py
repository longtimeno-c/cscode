# A cinema has 10 rows with 12 seats in each row. The system needs to track which seats are available and which are booked.
# a) Declare a suitable 2D array to represent this seating arrangement using pseudocode.
# b) Write pseudocode for a function that:

# Books a seat at a specific row and column
# Checks if a requested seat is available
# Counts and returns the total number of available seats.



seats = [[]]

# [[1,0,1,1,0,1,0,1,1,0,1,0], [], [],[], [], [], [], [], [], []]

def book_seat(row, col):
    if seats[row][col] == 0:
        seats[row][col] = 1
        return True
    else:
        return False
def check_seat(row, col):
    if seats[row][col] == 0:
        return True
    else:
        return False
def count_available_seats():
    count = 0
    for row in seats:
        for seat in row:
            if seat == 0:
                count += 1
    return count
def initialize_seats():
    for i in range(10):
        row = []
        for j in range(12):
            row.append(0)
        seats.append(row)
    return seats
def display_seats():
    for i in range(10):
        for j in range(12):
            if seats[i][j] == 0:
                print("O", end=" ")
            else:
                print("X", end=" ")
        print()
# Initialize the seating arrangement
initialize_seats()