items = ['Florida', 'Georgia', 'Delaware', 'Alabama', 'California']
item_to_find = input("Enter the state to find:")

index = 0 
found = False 
while found == False and index < len(items):
    if items[index] == item_to_find:
        found = True
    else:
        index = index + 1

if found == True:
    print('Item found at position', index)
else:
    print('item not found')