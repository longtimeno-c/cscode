array = []
#  Try insures there are limited errors.
try:
    # 'with' auto closes file when running
    with open('file.txt', "r") as file:
        array = [line.strip() for line in file]
except FileNotFoundError:
    print(f"File {file} not found or unable to open.")
print(array)