totalcost = 0
totalcostvat = 0
pronumber = ["1", "2", "3"]
number = ["1","2"]
outofstock = 0
import time
import datetime
#stock of items here:
stockofprocessorp3 = 8
stockofprocessorp5 = 30
stockofprocessorp7 = 2

stockofram16 = 2
stockofram32 = 20

stockofstorage1tb = 8
stockofstorage2tb = 0

stockof19 = 12
stockof23 = 1

stockofminicase = 5
stockofmidi = 3

stockofusb = 10

## start
print("Welcome to PC builder")
print("Todays date is the:",datetime.datetime.now().strftime("%d-%m-%Y"))
time.sleep(1)
print()
pricewant = int(input("Enter the price you are willing to spend on your computer:"))
print("****************************************************************")
print("Hello what type of processor are you interested in today?")
time.sleep(1)
print("Please enter either 1,2 or 3")
print("****************************************************************")
processor = (input("You can choose from P3(£100) [1], P5(£150) [2] and P7(£200) [3]"))

avaialble = True


#while totalcost <= pricewant:

while (processor not in pronumber):
    processor = (input("You can choose from P3[1], P5[2] and P7[3]"))
if processor == "1":
##Stock of P3 Processor
    if stockofprocessorp3 == 0:
        avaialble = False
        while avaialble == False:
            processor = (input("Sorry there is no stock you can choose from P5[2] and P7[3]"))
            avaialble = True
        if processor == "2":
            print("You have chosen P5")
            stockofprocessorp5 = stockofprocessorp5 - 1
            print()
            time.sleep(1)
            print("That will cost you £150")
            totalcost = totalcost + 150
            print("Your bill so far is:", totalcost, )
            print()
            time.sleep(1)
            if pricewant <= totalcost:
                print("This is above the amount you are willing to spend of: £",pricewant)
            else:
                print("This is still below your budget of: £",pricewant)
                print("You still have: £",pricewant - totalcost)
                print()
            print("There are", stockofprocessorp5,"left in stock")


        elif processor == "3":
            print("You have chosen P7")
            stockofprocessorp7 = stockofprocessorp7 - 1
            print()
            time.sleep(1)
            print("That will cost you £200")
            totalcost = 200 + totalcost
            print("Your bill so far is:", totalcost, )
            print()
            time.sleep(1)
            if pricewant <= totalcost:
                print("This is above the amount you are willing to spend of: £",pricewant)
            else:
                print("This is still below your budget of: £",pricewant)
                print("You still have: £",pricewant - totalcost)
            print()
            print("There are",stockofprocessorp7, "left in stock")
        else:
            print("Error")
    else:
        print("You have chosen P3")
        stockofprocessorp3 = stockofprocessorp3 - 1
        print()
        time.sleep(1)
        print("That will cost you £100")
        totalcost = 100 + totalcost
        print("Your bill so far is:", totalcost, )
        print()
        time.sleep(1)
        if pricewant <= totalcost:
            print("This is above the amount you are willing to spend of: £",pricewant)
        else:
            print("This is still below your budget of: £",pricewant)
            print("You still have: £",pricewant - totalcost)
        print()
        print("There are", stockofprocessorp3,"left in stock")

elif processor == "2":
##Stock of P5 Processor
    if stockofprocessorp5 == 0:
        avaialble = False
        while avaialble == False:
            processor = (input("Sorry there is no stock you can choose from P3[1] and P7[3]"))
            avaialble = True
        if processor == "1":
            print("You have chosen P3")
            stockofprocessorp3 = stockofprocessorp3 - 1
            print()
            time.sleep(1)
            print("That will cost you £100")
            totalcost = totalcost + 100
            print("Your bill so far is:", totalcost, )
            print()
            time.sleep(1)
            if pricewant <= totalcost:
                print("This is above the amount you are willing to spend of: £",pricewant)
            else:
                print("This is still below your budget of: £",pricewant)
                print("You still have: £",pricewant - totalcost)
            print()
            print("There are", stockofprocessorp3,"left in stock")

        elif processor == "3":
            print("You have chosen P7")
            stockofprocessorp7 = stockofprocessorp7 - 1
            print()
            time.sleep(1)
            print("That will cost you £200")
            totalcost = 200 + totalcost
            print("Your bill so far is:", totalcost, )
            print()
            time.sleep(1)
            if pricewant <= totalcost:
                print("This is above the amount you are willing to spend of: £",pricewant)
            else:
                print("This is still below your budget of: £",pricewant)
                print("You still have: £",pricewant - totalcost)
            print()
            print("There are", stockofprocessorp7,"left in stock")

        else:
            print("Error")
    else:
        print("You have chosen P5")
        stockofprocessorp5 = stockofprocessorp5 - 1
        print()
        time.sleep(1)
        print("That will cost you £150")
        totalcost = 150 + totalcost
        print("Your bill so far is:", totalcost, )
        print()
        time.sleep(1)
        if pricewant <= totalcost:
            print("This is above the amount you are willing to spend of: £",pricewant)
        else:
            print("This is still below your budget of: £",pricewant)
            print("You still have: £",pricewant - totalcost)
        print()
        print("There are", stockofprocessorp5,"left in stock")

elif processor == "3":
##Stock of P7 Processor
    if stockofprocessorp7 == 0:
        avaialble = False
        while avaialble == False:
            processor = (input("Sorry there is no stock you can choose from P3[1] and P7[3]"))
            avaialble = True
        if processor == "1":
            print("You have chosen P3")
            stockofprocessorp3 = stockofprocessorp3 - 1
            print()
            time.sleep(1)
            print("That will cost you £100")
            totalcost = totalcost + 100
            print("Your bill so far is:", totalcost, )
            print()
            time.sleep(1)
            if pricewant <= totalcost:
                print("This is above the amount you are willing to spend of: £",pricewant)
            else:
                print("This is still below your budget of: £",pricewant)
                print("You still have: £",pricewant - totalcost)
            print()
            print("There are", stockofprocessorp3,"left in stock")

        elif processor == "2":
            print("You have chosen P5")
            stockofprocessorp5 = stockofprocessorp5 - 1
            print()
            time.sleep(1)
            print("That will cost you £150")
            totalcost = totalcost + 150
            print("Your bill so far is:", totalcost, )
            print()
            time.sleep(1)
            if pricewant <= totalcost:
                print("This is above the amount you are willing to spend of: £",pricewant)
            else:
                print("This is still below your budget of: £",pricewant)
                print("You still have: £",pricewant - totalcost)
            print()
            print("There are", stockofprocessorp5,"left in stock")
        else:
            print("error")
    else:
        print("You have chosen P7")
        stockofprocessorp7 = stockofprocessorp7 - 1
        print()
        time.sleep(1)
        print("That will cost you £200")
        totalcost = 200 + totalcost
        print("Your bill so far is:", totalcost, )
        print()
        time.sleep(1)
        if pricewant <= totalcost:
            print("This is above the amount you are willing to spend of: £",pricewant)
        else:
            print("This is still below your budget of: £",pricewant)
            print("You still have: £",pricewant - totalcost)
        print()
        print("There are", stockofprocessorp7,"left in stock")
else:
    print("Error")

time.sleep(1)

## RAM


time.sleep(2)
print()
print("****************************************************************")
print("How much RAM are you interested in?")
print("****************************************************************")
RAM = input("16GB(£75) [1], 32GB(£150) [2]")

while (RAM not in number):
    RAM = input("16GB [1], 32GB [2]")
if RAM == "1":
## Stock of RAM16
    if stockofram16 == 0:
        avaialble = False
        while avaialble == False:
            RAM = input("16GB is out of stock please select another option:32GB(£150) [2]")
            avaialble = True
        if RAM == "2":
            print("You have chosen 32GB")
            print()
            stockofram32 = stockofram32 - 2
            time.sleep(1)
            print("That will cost you £75")
            totalcost = totalcost + 75
            print("Your bill so far is:", totalcost, )
            if pricewant <= totalcost:
                print("This is above the amount you are willing to spend of: £",pricewant)
            else:
                print("This is still below your budget of: £",pricewant)
                print("You still have: £",pricewant - totalcost)
            print()
            print("There are this many RAM sticks left in stock:", stockofram32)
        else:
            print("Error")

    else:
        print("You have chosen 16GB")
        print()
        stockofram16 = stockofram16 -2
        time.sleep(1)
        print("That will cost you £75")
        totalcost = totalcost + 75
        print("Your bill so far is:", totalcost, )
        if pricewant <= totalcost:
            print("This is above the amount you are willing to spend of: £",pricewant)
        else:
            print("This is still below your budget of: £",pricewant)
            print("You still have: £",pricewant - totalcost)
        print()
        print("There are this many RAM sticks left in stock:", stockofram16)

elif RAM == "2":
## Stock of RAM32
    if stockofram32 == 0:
        avaialble = False
        while avaialble == False:
            RAM = input("32GB is out of stock please select another option:16GB(£75) [1]")
            avaialble = True
        if RAM == "1":
            print("You have chosen 16GB")
            print()
            stockofram16 = stockofram16 -2
            time.sleep(1)
            print("That will cost you £75")
            totalcost = totalcost + 75
            print("Your bill so far is:", totalcost, )
            if pricewant <= totalcost:
                print("This is above the amount you are willing to spend of: £",pricewant)
            else:
                print("This is still below your budget of: £",pricewant)
                print("You still have: £",pricewant - totalcost)
            print()
            print("There are this many RAM sticks left in stock:", stockofram16)
    else:
        print("You have chosen 32GB")
        print()
        stockofram32 = stockofram32 - 2
        time.sleep(1)
        print("That will cost you £75")
        totalcost = totalcost + 75
        print("Your bill so far is:", totalcost, )
        if pricewant <= totalcost:
            print("This is above the amount you are willing to spend of: £",pricewant)
        else:
            print("This is still below your budget of: £",pricewant)
            print("You still have: £",pricewant - totalcost)
        print()
        print("There are this many RAM sticks left in stock:", stockofram32)


else:
    print("Error try agan")


## storage

time.sleep(2)
print()
print("****************************************************************")
print("How much storage are you interested in?")
print("****************************************************************")
storage = input("Storage 1TB(£50) [1], Storage 2TB(£100) [2]")

while (storage not in number):
    storage = input("Storage 1TB(£50) [1], Storage 2TB(£100) [2]")
if storage == "1":

    if stockofstorage1tb == 0:
        avaialble = False
        while avaialble == False:
            storage = input("Storage 1TB(£50) [1], Storage 2TB(£100) [2]")
            avaialble = True
        if storage == "2":
            print("You have chosen 2TB of storage")
            print()
            time.sleep(1)
            print("That will cost you £100")
            totalcost = totalcost + 100
            print("Your bill so far is:", totalcost,)
            if pricewant <= totalcost:
                print("This is above the amount you are willing to spend of: £",pricewant)
            else:
                print("This is still below your budget of: £",pricewant)
                print("You still have: £",pricewant - totalcost)
            print()
            print("There are this many HDD of this type left in stock:", stockofstorage2tb)
        else:
            print("Error")
    else:
        print("You have chosen 1TB of storage")
        print()
        time.sleep(1)
        print("That will cost you £50")
        totalcost = totalcost + 50
        print("Your bill so far is:", totalcost, )
        if pricewant <= totalcost:
            print("This is above the amount you are willing to spend of: £",pricewant)
        else:
            print("This is still below your budget of: £",pricewant)
            print("You still have: £",pricewant - totalcost)
        print()
        print("There are this many HDD of this type left in stock:", stockofstorage1tb)

elif storage == "2":
    if stockofstorage2tb == 0:
        avaialble = False
        while avaialble == False:
            storage = input("Sorry this is not in stock please select another option Storage 1TB(£50) [1]")
            avaialble = True
        if storage == "1":
            print("You have chosen 1TB of storage")
            print()
            time.sleep(1)
            print("That will cost you £50")
            totalcost = totalcost + 50
            print("Your bill so far is:", totalcost, )
            if pricewant <= totalcost:
                print("This is above the amount you are willing to spend of: £",pricewant)
            else:
                print("This is still below your budget of: £",pricewant)
                print("You still have: £",pricewant - totalcost)
            print()
            print("There are this many HDD of this type left in stock:", stockofstorage1tb)
        else:
            print("Error")
    else:
        print("You have chosen 2TB of storage")
        print()
        time.sleep(1)
        print("That will cost you £100")
        totalcost = totalcost + 100
        print("Your bill so far is:", totalcost,)
        if pricewant <= totalcost:
            print("This is above the amount you are willing to spend of: £",pricewant)
        else:
            print("This is still below your budget of: £",pricewant)
            print("You still have: £",pricewant - totalcost)
        print()
        print("There are this many HDD of this type left in stock:", stockofstorage2tb)

else:
    print("Error")



## screen

##stock of screen

time.sleep(2)
print()
print("****************************************************************")
print("What monitor are you interested in?")
print("****************************************************************")
monitor = input("19'(£65) [1] or 23'(£120) [2]")


## Stock of monitor
while (monitor not in number):
    monitor = input("19'(£65) [1] or 23'(£120) [2]")

if monitor == "1":
    if stockof19 ==0:
        avaialble = False
        while avaialble == False:
            monitor = input("This monitor is out of stock please select another option: 23'(£120) [2]")
            avaialble = True
        if monitor == "2":
            print("You have chosen the 23 inch display")
            print()
            stockof23 = stockof23 -1
            time.sleep(1)
            print("That will cost you £120")
            totalcost = totalcost + 120
            print("Your bill so far is:", totalcost,)
            if pricewant <= totalcost:
                print("This is above the amount you are willing to spend of: £",pricewant)
            else:
                print("This is still below your budget of: £",pricewant)
                print("You still have: £",pricewant - totalcost)
            print()
            print("There are this many monitors of this type left in stock:", stockof23)
        else:
            print("Error")
    else:
        print("You have chosen the 19 inch display")
        print()
        stockof19 = stockof19 -1
        time.sleep(1)
        print("That will cost you £65")
        totalcost = totalcost + 65
        print("Your bill so far is:", totalcost,)
        if pricewant <= totalcost:
            print("This is above the amount you are willing to spend of: £",pricewant)
        else:
            print("This is still below your budget of: £",pricewant)
            print("You still have: £",pricewant - totalcost)
        print()
        print("There are this many monitors of this type left in stock:", stockof19)


elif monitor == "2":
    if stockof23 == 0:
        avaialble = False
        while avaialble == False:
            monitor = input("This monitor is out of stock please select another option: 19'(£65) [1]")
            avaialble = True
        if monitor == "1":
            print("You have chosen the 19 inch display")
            print()
            stockof19 = stockof19 -1
            time.sleep(1)
            print("That will cost you £65")
            totalcost = totalcost + 65
            print("Your bill so far is:", totalcost,)
            if pricewant <= totalcost:
                print("This is above the amount you are willing to spend of: £",pricewant)
            else:
                print("This is still below your budget of: £",pricewant)
                print("You still have: £",pricewant - totalcost)
            print()
            print("There are this many monitors of this type left in stock:", stockof19)
        else:
            print("Error")
    else:
        print("You have chosen the 23 inch display")
        print()
        stockof23 = stockof23 -1
        time.sleep(1)
        print("That will cost you £120")
        totalcost = totalcost + 120
        print("Your bill so far is:", totalcost,)
        if pricewant <= totalcost:
            print("This is above the amount you are willing to spend of: £",pricewant)
        else:
            print("This is still below your budget of: £",pricewant)
            print("You still have: £",pricewant - totalcost)
        print()
        print("There are this many monitors of this type left in stock:", stockof23)


else:
    print("Error")


time.sleep(1)

## case

time.sleep(2)
print()
print("****************************************************************")
print("What Case are you interested in?")
print("****************************************************************")
Case = input("Mini Tower(£40) [1] or Midi Tower(£70) [2]")

while (Case not in number):
    Case = input("Mini Tower(£40) [1] or Midi Tower(£70) [2]")
if Case == "1":
    if stockofminicase == 0:
        avaialble = False
        while avaialble == False:
            Case = input("That item is out of stock please pick another option: Midi Tower(£70) [2]")
            avaialble = True
        if Case == "2":
            print("You have chosen the Midi Tower")
            print()
            stockofmidi = stockofmidi -1
            time.sleep(1)
            print("That will cost you £70")
            totalcost = totalcost + 70
            print("Your bill so far is:", totalcost,)
            if pricewant <= totalcost:
                print("This is above the amount you are willing to spend of: £",pricewant)
            else:
                print("This is still below your budget of: £",pricewant)
                print("You still have: £",pricewant - totalcost)
            print()
            print("The stock of the mini case is:", stockofmidic)
        else:
            print("Error")
    else:
        print("You have chosen the Mini Tower")
        print()
        stockofminicase = stockofminicase -1
        time.sleep(1)
        print("That will cost you £40")
        totalcost = totalcost + 40
        print("Your bill so far is:", totalcost,)
        if pricewant <= totalcost:
            print("This is above the amount you are willing to spend of: £",pricewant)
        else:
            print("This is still below your budget of: £",pricewant)
            print("You still have: £",pricewant - totalcost)
        print()
        print("The stock of the mini case is:", stockofminicase)

elif Case == "2":
    if stockofmidi == 0:
        avaialble = False
        while avaialble == False:
            Case = input("That item is out of stock please pick another option: Mini Tower(£40) [1]")
            avaialble = True
        if Case == "1":
            print("You have chosen the Mini Tower")
            print()
            stockofminicase = stockofminicase -1
            time.sleep(1)
            print("That will cost you £40")
            totalcost = totalcost + 40
            print("Your bill so far is:", totalcost,)
            if pricewant <= totalcost:
                print("This is above the amount you are willing to spend of: £",pricewant)
            else:
                print("This is still below your budget of: £",pricewant)
                print("You still have: £",pricewant - totalcost)
            print()
            print("The stock of the mini case is:", stockofminicase)
        else:
            print("Error")

    else:
        print("You have chosen the Midi Tower")
        print()
        stockofmidi = stockofmidi -1
        time.sleep(1)
        print("That will cost you £70")
        totalcost = totalcost + 70
        print("Your bill so far is:", totalcost,)
        if pricewant <= totalcost:
            print("This is above the amount you are willing to spend of: £",pricewant)
        else:
            print("This is still below your budget of: £",pricewant)
            print("You still have: £",pricewant - totalcost)
        print()
        print("The stock of the mini case is:", stockofmidi)

else:
    print("Error")


time.sleep(1)


## USB ports


time.sleep(2)
print()
print("****************************************************************")
print("How many USB ports would you like?")
print("****************************************************************")
USB = input("2 ports(£10) [1] or 4 ports(£20) [2]")

while (USB not in number):
    USB = input("2 ports(£10) [1] or 4 ports(£20) [2]")
if USB == "1":
    if stockofusb <= 1:
        avaialble = False
        while avaialble == False:
            USB = input("This item is out of stock please select another item: 4 ports(£20) [2]")
            avaialble = True
        if USB == "2":
            print("You have chosen 4 ports")
            print()
            stockofusb = stockofusb - 4
            time.sleep(1)
            print("That will cost you £20")
            totalcost = totalcost + 20
            print("Your bill so far is:", totalcost,)
            if pricewant <= totalcost:
                print("This is above the amount you are willing to spend of: £",pricewant)
            else:
                print("This is still below your budget of: £",pricewant)
                print("You still have: £",pricewant - totalcost)
            print()
        else:
            print("Error")
    else:
        print("You have chosen 2 USB ports")
        print()
        stockofusb = stockofusb - 2
        time.sleep(1)
        print("That will cost you £10")
        totalcost = totalcost + 10
        print("Your bill so far is:", totalcost,)
        if pricewant <= totalcost:
            print("This is above the amount you are willing to spend of: £",pricewant)
        else:
            print("This is still below your budget of: £",pricewant)
            print("You still have: £",pricewant - totalcost)
        print()

elif USB == "2":
    if stockofusb <= 3:
        avaialble = False
        while avaialble == False:
            USB = input("This item is out of stock please select another item: 2 ports(£10) [1]")
            avaialble == True
        if USB == "1":
            print("You have chosen 2 USB ports")
            print()
            stockofusb = stockofusb - 2
            time.sleep(1)
            print("That will cost you £10")
            totalcost = totalcost + 10
            print("Your bill so far is:", totalcost,)
            if pricewant <= totalcost:
                print("This is above the amount you are willing to spend of: £",pricewant)
            else:
                print("This is still below your budget of: £",pricewant)
                print("You still have: £",pricewant - totalcost)
            print()
        else:
            print("Error")
    else:
        print("You have chosen 4 ports")
        print()
        stockofusb = stockofusb - 4
        time.sleep(1)
        print("That will cost you £20")
        totalcost = totalcost + 20
        print("Your bill so far is:", totalcost,)
        if pricewant <= totalcost:
            print("This is above the amount you are willing to spend of: £",pricewant)
        else:
            print("This is still below your budget of: £",pricewant)
            print("You still have: £",pricewant - totalcost)
        print()

else:
    print("Error")

print("There are this many USB ports in stock",stockofusb)



time.sleep(1)


print()
print()
## VAT

totalcostvat = totalcost * 1.2

## checkstock

print("Checking stock.")
time.sleep(2)
print("Checking stock..")
time.sleep(2)
print("Checking stock...")

print("All your items are in stock")
print()
time.sleep(1)
name= input("To complete your order please enter your name:")
surname = input("And your last name:")


print("Your total cost today",name,"",surname,"is £",totalcost,)
time.sleep(1)
print("Your were willing to spend £",pricewant)
print()
time.sleep(1)

##processor display
if processor == "1":
    displayproc = ("P3")
elif processor == "2":
    displayproc = ("P5")
elif processor == "3":
    displayproc = ("P7")
else:
    print("_")

if RAM == "1":
    displayram = ("16GB")
elif RAM == "2":
    displayram = ("32GB")
else:
    print("_")
##Storage display
if storage == "1":
    displaystorage = ("1TB")
elif storage == "2":
    displaystorage = ("2TB")
else:
    print("Error")

##Monitor display
if monitor == "1":
    displaymonitor = ("19'")
elif monitor == "2":
    displaymonitor = ("23'")
else:
    print("_")

##Display case
if Case == "1":
	displaycase = ("MiniCase")
elif Case == "2":
	displaycase = ("MidiCase")
else:
	print("_")
	
##display USB
if USB == "1":
    displayusb = ("2 USB ports")
elif USB == "2":
    displayusb = ("4 USB ports")
else:
    print("_")


print(" _Your current Spec sheet is as follows:_")
print("- - - - - - - - - - - - - - - - - - - - - ")
print("- - - - Processor ->",displayproc,)
print("- - - - Ram ->",displayram,)
print("- - - - Storage ->",displaystorage,)
print("- - - - Monitor ->",displaymonitor,)
print("- - - - Case ->",displaycase,)
print("- - - - - - - - - - - - - - - - - - - - - ")
print("- - - - Order placed on the:",datetime.datetime.now().strftime("%d-%m-%Y"))
print("- TOTAL BILL (incl VAT) = £",totalcostvat,"- - - -")
print("- - - - - - - - - - - - - - - - - - - - - ")



time.sleep(1)
