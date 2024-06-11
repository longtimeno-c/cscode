# Mario pyramids

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0 and value <= 8:
                return value
            else:
                print("Please enter a positive integer between 1 and 8.")
        except ValueError:
            print("Please enter a valid integer.")

def print_pyramid(height):
    for i in range(1, height + 1):
        # Printing spaces for left half
        print(" " * (height - i), end="")
        # Print hashes for left half
        print("#" * i, end="")
        
        # Print gap between pyramids
        print("  ", end="")
        
        # Print hashes for right pyramid
        print("#" * i)

def main():
    height = get_int("Height of the half-pyramids: ")
    print_pyramid(height)


main()
