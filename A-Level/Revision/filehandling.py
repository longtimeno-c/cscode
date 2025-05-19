# create a python program that takes a text file open called names. 
# asks how many names they want to add to the file 
# and then puts that number of names one line each. Closes the file 
# and the opens it in read mode and outputs the contents through print

numNames = int(input("Enter number of names:"))

with open ('names.txt', 'w') as file:
    file.write("Testing")
    for i in range (numNames):
        name = input("Enter name")
        file.write(f'{name} /n')
    file.close()

