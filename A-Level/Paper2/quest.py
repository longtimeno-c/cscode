start = 100
end = 150


def Select():
    for i in range (start+1, end):
        thisString = str(i)
        lastDigit = int(thisString[-1])
        secondDigit = int(thisString[-2])
        Total = lastDigit + secondDigit
        if Total == 6:
            print("Great success! Number is:", i)
Select()