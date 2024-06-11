import time
count = 0
convayerbelt = 1
on = 0
totalfood = 0
cost = 0
mostexpensive = 0 
leastexpensive = 1000000000000000000000000000000000
yes = ["yes","y", "Yes"]
resturant = False

while resturant == False:
    ##input from staff 
    resurantopen = input("Is the resturant open?")
    if resurantopen in yes:
        resturant = True
        convayerbelt = False
        print()
        print("************************************")
        print("Welcome the resturat is open")
        print("Running the resturant stat board...")
        print("************************************")
        print()
        time.sleep(1)
        while convayerbelt == False:
            ##Laser input 
            sushidetected = int(input("How much sushi was detected by the laser?"))
            totalfood = totalfood + sushidetected
            if sushidetected >= 1:
                ##Order/ table number cost input 
                priceofserving = int(input("What is the total cost of that sushi served?"))
                cost = cost + priceofserving
                if priceofserving >= mostexpensive:
                    mostexpensive = priceofserving
                if leastexpensive >= priceofserving:
                    leastexpensive = priceofserving
                    
                count = count +1
            elif sushidetected == 0:
                convayerbelt = True
            else:
                print("Error")
            print()
        print("***************************************************")
        print("Belt stopped, no sushi")
        print("***************************************************")
        time.sleep(1)
        print()
        print("***************************************************")
        print("Number of tables served",count)
        print("Dishes served",totalfood)
        print("Total revenue",cost)
        print("The most expensive order was:",mostexpensive)
        print("The least expensive order was:",leastexpensive)
        print("***************************************************")
        print()
        time.sleep(5)
        count = 0
        cost = 0
        mostexpensive = 0 
        leastexpensive = 10000000000000000000000
        totalfood = 0
        resturant = False
    else:
        print("***************************************************")
        print("Belt stopped, resurant closed")
        print("***************************************************")
        print()
        time.sleep(4)
