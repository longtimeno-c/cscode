class TreasureChest:
    def __init__(self, question, answer, points):
        self.__question = question
        self.__answer = answer
        self.__points = points

    def getQuestion(self):
        """Returns the question."""
        return self.__question

    def checkAnswer(self, user_answer):
        """Checks if the user's answer is correct."""
        return user_answer == self.__answer

    def getPoints(self, attempts):
        """Calculates points based on the number of attempts."""
        if attempts == 1:
            return self.__points
        elif attempts == 2:
            return self.__points // 2
        elif attempts == 3 or attempts == 4:
            return self.__points // 4
        else:
            return 0


def readData():
    """Reads data from the file and creates TreasureChest objects."""
    arrayTreasure = []

    try:
        with open("TreasureChestData.txt", "r") as file:
            while True:
                # Read question
                question = file.readline().strip()
                if not question:
                    break  # End of file

                # Read answer
                answer = file.readline().strip()
                if not answer.isdigit():
                    print("Invalid answer format.")
                    continue
                answer = int(answer)

                # Read points
                points = file.readline().strip()
                if not points.isdigit():
                    print("Invalid points format.")
                    continue
                points = int(points)

                # Create TreasureChest object
                treasure_chest = TreasureChest(question, answer, points)
                arrayTreasure.append(treasure_chest)

    except FileNotFoundError:
        print("Error: TreasureChestData.txt not found.")
        return

    # Ask questions to the user
    for treasure in arrayTreasure:
        attempts = 0
        correct = False

        while not correct:
            user_answer = int(input(f"{treasure.getQuestion()} "))
            attempts += 1

            if treasure.checkAnswer(user_answer):
                print("Correct!")
                print(f"Points awarded: {treasure.getPoints(attempts)}")
                correct = True
            else:
                print("Incorrect. Try again.")

# Run the readData function
readData()