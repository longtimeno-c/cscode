# Global variables
WordArray = []
NumberWords = 0

def ReadWords(filename):
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

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
