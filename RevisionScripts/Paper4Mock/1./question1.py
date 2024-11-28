# Define the Node class to represent each node in the linked list
class Node:
    def __init__(self, data=0, nextNode=-1):
        self.data = data
        self.nextNode = nextNode

# Initialize the linked list as a 1D array of Node objects
linkedList = [
    Node(1, 2),  # Index 0
    Node(5, 4),  # Index 1
    Node(6, 3),  # Index 2
    Node(7, -1), # Index 3
    Node(2, 9),  # Index 4
    Node(0, 7),  # Index 5 (emptyList pointer)
    Node(56, 3), # Index 6
    Node(56, 6), # Index 7
    Node(9, -1), # Index 8
    Node(0, -1)  # Index 9
]

# Pointers
startPointer = 0
emptyList = 5

# Procedure to output nodes from the linked list
def outputNodes(linkedList, startPointer):
    currentPointer = startPointer
    while currentPointer != -1:
        print(linkedList[currentPointer].data, end=" ")
        currentPointer = linkedList[currentPointer].nextNode
    print()  # For a new line after output

# Main program to call the outputNodes procedure
if __name__ == "__main__":
    print("Linked List Data:")
    outputNodes(linkedList, startPointer)