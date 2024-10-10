racers = 10
count = 0
fastest = 100000000000000
while count != 10:
    time = int(input("Input time"))
    count = count + 1
    if count == 1:
        Racer1 = time
        if Racer1 <= fastest:
            fastest = Racer1
    elif count == 2:
        Racer2 = time
        if Racer2 <= fastest:
            fastest = Racer2
    elif count == 3:
        Racer3 = time
        if Racer3 <= fastest:
            fastest = Racer3
    elif count == 4:
        Racer4 = time
        if Racer4 <= fastest:
            fastest = Racer4
    elif count == 5:
        Racer5 = time
        if Racer5 <= fastest:
            fastest = Racer5
    elif count == 6:
        Racer6 = time
        if Racer6 <= fastest:
            fastest = Racer6
    elif count == 7:
        Racer7 = time
        if Racer7 <= fastest:
            fastest = Racer7
    elif count == 8:
        Racer8 = time
        if Racer8 <= fastest:
            fastest = Racer8
    elif count == 9:
        Racer9 = time
        if Racer9 <= fastest:
            fastest = Racer9
    elif count == 10:
        Racer10 = time
        if Racer10 <= fastest:
            fastest = Racer10


print("Racer1 =",Racer1)
print("Racer2 =",Racer2)
print("Racer3 =",Racer3)
print("Racer4 =",Racer4)
print("Racer5 =",Racer5)
print("Racer6 =",Racer6)
print("Racer7 =",Racer7)
print("Racer8 =",Racer8)
print("Racer9 =",Racer9)
print("Racer10 =",Racer10)
print("The fastet time was",fastest)


