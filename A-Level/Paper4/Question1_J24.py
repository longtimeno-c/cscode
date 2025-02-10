# Global variables
WordArray = []
NumberWords = 0

def ReadWords(filename):
    """
    Reads words from a given file and stores them in WordArray.
    Stores the number of valid words in NumberWords.
    Calls Play() after reading words.
    """
    global WordArray, NumberWords
    WordArray = []  # Reset the array

    try:
        with open(filename, 'r') as file:
            # Read main word
            main_word = file.readline().strip()
            WordArray.append(main_word)
            
            # Read the rest of the words
            for line in file:
                WordArray.append(line.strip())

        # Store the number of words (excluding the main word)
        NumberWords = len(WordArray) - 1

        # Call Play() function
        Play()

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

def Play():
    """
    Plays the word-guessing game with the user.
    Outputs the main word, checks answers, and provides feedback.
    """
    global WordArray

    # Extract the main word
    main_word = WordArray[0]
    correct_answers = set(WordArray[1:])  # Store answers in a set for quick lookup
    user_answers = set()  # Store user's correct guesses

    print(f"\nMain word: {main_word}")
    print(f"You need to find {NumberWords} words.")

    while True:
        user_input = input("Enter a word (or type 'no' to stop): ").strip().lower()

        if user_input == "no":
            break

        if user_input in correct_answers:
            print("Correct!")
            user_answers.add(user_input)
            WordArray[WordArray.index(user_input)] = None  # Replace with null
        else:
            print("Not an answer.")

    # Calculate percentage correct
    percentage_correct = (len(user_answers) / NumberWords) * 100 if NumberWords > 0 else 0
    print(f"\nGame Over! You got {len(user_answers)} out of {NumberWords} ({percentage_correct:.2f}%).")

    # Display missed words
    missed_words = [word for word in correct_answers if word not in user_answers]
    if missed_words:
        print("You missed the following words:")
        print(", ".join(missed_words))
    else:
        print("You found all the words!")

def main():
    """
    Asks the user for a difficulty level and calls ReadWords() with the correct file.
    """
    difficulty = input("Enter difficulty level (easy, medium, hard): ").strip().lower()

    file_map = {
        "easy": "Easy.txt",
        "medium": "Medium.txt",
        "hard": "Hard.txt"
    }

    if difficulty in file_map:
        ReadWords(file_map[difficulty])
    else:
        print("Invalid input. Please enter 'easy', 'medium', or 'hard'.")

# Run the main function
if __name__ == "__main__":
    main()
