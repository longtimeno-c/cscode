def TwoParts():
    valid = False
    TotalA = 0
    entered = 0
    while valid == False:
        entered = int(input("Enter number: "))
        if entered == 0:
            print(f"Total A: {TotalA}")
            valid = True
        elif entered != "0":
            TotalA += entered
        else:
            print("Error")
TwoParts()