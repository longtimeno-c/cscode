import time 



#question 1
print ("What is your first name?")

firstname = input()

print("Enter your birthdate in ddmmyyyy")

ddmmyyyy = input()

print ("Hello,", firstname)

time.sleep(2)

print()
print ("What is your surname?")

surname = input()

#question 2
print ("Hello,",firstname,surname)

#question 3
print("Your initials are:",firstname[0],surname[0])

fullname = firstname + " " + surname

time.sleep(2)


#question 5
#display as upper text 
print(firstname.upper())

time.sleep(1)

#question 6
#Letters in first name

lettersf = len(firstname)

print ("there are",lettersf,"letters in your first name")
print()

time.sleep(2)


#question 7
#Login system

username = (surname[0] + surname[1] + surname[2] + firstname[0] + str(len(surname)))

print("your username is:",username)

time.sleep(2)

print()

password = (firstname[0] + surname[0] + ddmmyyyy)

print("Your password is:",password)

