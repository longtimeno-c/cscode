array = []
# 'with' auto closes file when running
with open('file.txt', "r") as file:
    array = [line.strip() for line in file]
print(array)