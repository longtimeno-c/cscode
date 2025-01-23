class Tree:
    def __init__(self, TreeName, HeightGrowth, MaxHeight, MaxWidth, Evergreen):
        self.__TreeName = TreeName
        self.__HeightGrowth = HeightGrowth
        self.__MaxHeight = MaxHeight
        self.__MaxWidth = MaxWidth
        self.__Evergreen = Evergreen

    def GetTreeName(self):
        return self.__TreeName

    def GetGrowth(self):
        return self.__HeightGrowth

    def GetMaxHeight(self):
        return self.__MaxHeight

    def GetMaxWidth(self):
        return self.__MaxWidth

    def GetEvergreen(self):
        return self.__Evergreen


def ReadData():
    trees = []
    try:
        with open('Trees.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                tree = Tree(data[0], int(data[1]), int(data[2]), int(data[3]), data[4])
                trees.append(tree)
    except FileNotFoundError:
        print("File not found.")
    return trees


def PrintTrees(tree):
    if tree.GetEvergreen() == "Yes":
        print(f"{tree.GetTreeName()} has a maximum height {tree.GetMaxHeight()} cm, "
              f"a maximum width {tree.GetMaxWidth()} cm, and grows {tree.GetGrowth()} cm a year. "
              f"It does not lose its leaves.")
    else:
        print(f"{tree.GetTreeName()} has a maximum height {tree.GetMaxHeight()} cm, "
              f"a maximum width {tree.GetMaxWidth()} cm, and grows {tree.GetGrowth()} cm a year. "
              f"It loses its leaves each year.")


def ChooseTree(trees):
    max_height = int(input("Enter the maximum height in cm: "))
    max_width = int(input("Enter the maximum width in cm: "))
    evergreen = input("Do you want the tree to be evergreen (Yes/No): ")

    suitable_trees = [tree for tree in trees if tree.GetMaxHeight() <= max_height 
                      and tree.GetMaxWidth() <= max_width and tree.GetEvergreen() == evergreen]

    if suitable_trees:
        for tree in suitable_trees:
            PrintTrees(tree)

        tree_name = input("Enter the name of the tree you would like to buy: ")
        starting_height = int(input("Enter the height of the tree in cm when bought: "))

        for tree in suitable_trees:
            if tree.GetTreeName() == tree_name:
                years_to_grow = (tree.GetMaxHeight() - starting_height) // tree.GetGrowth()
                print(f"It will take {years_to_grow} years for the tree to reach its maximum height.")
                break
    else:
        print("No trees meet all the requirements.")


def main():
    trees = ReadData()
    if trees:
        ChooseTree(trees)


main()