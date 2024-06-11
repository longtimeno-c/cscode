##DECLARATION

#results = String
#name = String
#swimmer1-5] = String
#Swim[1-5] = Array
#count = Integer
#printcount = Integer
#time[1-3] = Integer
#tottime = Integer
#Avgscore[1-5] = Integer
#

import re 

##----------------------------------------------------##
#Getting data from files#
##----------------------------------------------------## 

results = ("Swimmer Results")
name = ("Swimmer Name")
with open(results,"r") as file:
  swimmer1 = file.readline()
  swimmer2 = file.readline()
  swimmer3 = file.readline()
  swimmer4 = file.readline()
  swimmer5 = file.readline()

## To verify it read the file correctly by printing values 
#print(swimmer1)
#print(swimmer2)
#print(swimmer3)
#print(swimmer4)
#print(swimmer5)

##----------------------------------------------------##
#Creating Arrays from data collected#
##----------------------------------------------------##
 
swim=[]
count = 1

##Each of the 5 swimmers is split by numbers and letters 
swim1= re.split ('(\d+)' ,swimmer1)
#removes unwanted characters from text file 
swim1.remove(",")
swim1.remove(",")
swim1.remove("\n")
#print(swim1)

##Repeated for each swimmer

swim2= re.split ('(\d+)' ,swimmer2) 
swim2.remove(",")
swim2.remove(",")
swim2.remove("\n")
#print(swim2)


swim3= re.split ('(\d+)' ,swimmer3)
swim3.remove(",")
swim3.remove(",")
swim3.remove("\n")
#print(swim3)

swim4= re.split ('(\d+)' ,swimmer4)
swim4.remove(",")
swim4.remove(",")
swim4.remove("\n")
#print(swim4)

swim5= re.split ('(\d+)' ,swimmer5)
swim5.remove(",")
swim5.remove(",")
swim5.remove("\n")
#print(swim5)

print()


##----------------------------------------------------##
#Calculating Average time and output from Arrays#
##----------------------------------------------------##

Avgscore = []
##Count for each swimmer 
#Had to do individual because it didnt work as a while loop 
#printcount1 = 0
#printcount2 = 0
#printcount3 = 0
#printcount4 = 0
#printcount5 = 0

print("------------------------")

#Printing name and the three times:
#while printcount1 <= 3:
#  print(swim1[printcount1])
#  printcount1 = printcount1 + 1 

#Calling times from arry made
time1 = int(swim1[1])
time2 = int(swim1[2])
time3 = int(swim1[3])
#Adding up times for swimmer 
tottime = time1 + time2 + time3 
#Calculating average
Avgscore1 = tottime / 3
#Output name
print(swim1[0])
#Output Average:
print("---------")
print("Average: ")
print(Avgscore1)
print("------------------------")
print()

##Repeated

#while printcount2 <= 3:
#  print(swim2[printcount2])
#  printcount2 = printcount2 + 1 

time1 = int(swim2[1])
time2 = int(swim2[2])
time3 = int(swim2[3])

tottime = time1 + time2 + time3 
Avgscore2 = tottime / 3
print(swim2[0])
print("---------")
print("Average: ")
print(Avgscore2)
print("------------------------")
print()

#while printcount3 <= 3:
#  print(swim3[printcount3])
#  printcount3 = printcount3 + 1

time1 = int(swim3[1])
time2 = int(swim3[2])
time3 = int(swim3[3])

tottime = time1 + time2 + time3 
Avgscore3 = tottime / 3
print(swim3[0])
print("---------")
print("Average: ")
print(Avgscore3)
print("------------------------")
print()

#while printcount4 <= 3:
#  print(swim4[printcount4])
#  printcount4 = printcount4 + 1

time1 = int(swim4[1])
time2 = int(swim4[2])
time3 = int(swim4[3])

tottime = time1 + time2 + time3 
Avgscore4 = tottime / 3
print(swim4[0])
print("---------")
print("Average: ")
print(Avgscore4)
print("------------------------")
print()

#while printcount5 <= 3:
#  print(swim5[printcount5])
#  printcount5 = printcount5 + 1

time1 = int(swim5[1])
time2 = int(swim5[2])
time3 = int(swim5[3])

tottime = time1 + time2 + time3 
Avgscore5 = tottime / 3
print(swim5[0])
print("---------")
print("Average: ")
print(Avgscore5)
print("------------------------")
print()