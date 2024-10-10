highscores = [ [12,18], [23,5], [9,16] ]
print("Highscores")
print(highscores[1][0])

##student scores
print()
print()
print("Student marks")
count = 0
valid = False
studentname = ["Matthew", "Simon", "David"]
studentmark = [ [12,18], [23,5], [9,19] ]
while count <= 2:
    studentmark1 = (studentmark [count] [0])
    studentmark2 = (studentmark [count] [1])
    def student(count):
        print("---------------")
        print("Student name: ")
        print(studentname [count])
        print("Marks: ")
        print(studentmark [count] [0])
        print(studentmark [count] [1])
        print("---------------")
        print()
    print(student(0))
    count = count +1
    print(student(1))
    count = count +1
    print(student(2))
    count = count +1
    

