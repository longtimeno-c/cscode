class Node:
    """
    Represents a single node in the binary tree.
    Attributes:
    - LeftPointer (int): Index of the left child (-1 if no child).
    - Data (int): The actual data stored in the node.
    - RightPointer (int): Index of the right child (-1 if no child).
    """
    def __init__(self, data):
        self.LeftPointer = -1  # No left child initially
        self.Data = data  # Store the node's data
        self.RightPointer = -1  # No right child initially

    def GetLeft(self):
        """Returns the index of the left child."""
        return self.LeftPointer

    def GetRight(self):
        """Returns the index of the right child."""
        return self.RightPointer

    def GetData(self):
        """Returns the data stored in the node."""
        return self.Data

    def SetLeft(self, left_index):
        """Sets the index of the left child."""
        self.LeftPointer = left_index

    def SetRight(self, right_index):
        """Sets the index of the right child."""
        self.RightPointer = right_index

    def SetData(self, data):
        """Sets the data value of the node."""
        self.Data = data


class TreeClass:
    """
    Represents the binary tree.
    Attributes:
    - Tree (list): Array of nodes (size 20).
    - FirstNode (int): Index of the root node (-1 if tree is empty).
    - NumberNodes (int): The number of nodes currently in the tree.
    """
    def __init__(self):
        self.Tree = [Node(-1) for _ in range(20)]  # Initialize 20 nodes with data -1
        self.FirstNode = -1  # No root node yet
        self.NumberNodes = 0  # Start with 0 nodes

    def InsertNode(self, NewNode):
        """
        Inserts a new node into the tree.
        """
        if self.NumberNodes >= 20:
            print("Tree is full, cannot insert more nodes.")
            return
        
        if self.FirstNode == -1:
            # If the tree is empty, insert the first node at index 0
            self.Tree[self.NumberNodes] = NewNode
            self.FirstNode = 0
        else:
            # Insert node in the correct position
            current_index = self.FirstNode
            while True:
                if NewNode.GetData() < self.Tree[current_index].GetData():
                    # Go to the left
                    if self.Tree[current_index].GetLeft() == -1:
                        self.Tree[current_index].SetLeft(self.NumberNodes)
                        break
                    else:
                        current_index = self.Tree[current_index].GetLeft()
                else:
                    # Go to the right
                    if self.Tree[current_index].GetRight() == -1:
                        self.Tree[current_index].SetRight(self.NumberNodes)
                        break
                    else:
                        current_index = self.Tree[current_index].GetRight()

            self.Tree[self.NumberNodes] = NewNode  # Store the new node
        
        self.NumberNodes += 1  # Increment number of nodes

    def OutputTree(self):
        """
        Outputs the left pointer, data, and right pointer of each inserted node.
        """
        if self.NumberNodes == 0:
            print("No nodes")
            return

        print("Index | Left | Data | Right")
        print("---------------------------")
        for i in range(self.NumberNodes):
            print(f"{i:^5} | {self.Tree[i].GetLeft():^4} | {self.Tree[i].GetData():^4} | {self.Tree[i].GetRight():^4}")


# Main program
def main():
    """
    Creates a binary tree, inserts nodes, and outputs the tree structure.
    """
    TheTree = TreeClass()  # Create an instance of TreeClass

    # Insert the given nodes
    nodes_to_insert = [10, 11, 5, 1, 20, 7, 15]
    for value in nodes_to_insert:
        TheTree.InsertNode(Node(value))

    # Output the tree structure
    TheTree.OutputTree()


# Run the main program
if __name__ == "__main__":
    main()