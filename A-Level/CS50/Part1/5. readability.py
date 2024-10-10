# Readability

def count_letters(text):
    letters = sum(1 for char in text if char.isalpha())
    return letters

def count_words(text):
    words = len(text.split())
    return words

def count_sentences(text):
    sentences = text.count('.') + text.count('!') + text.count('?')
    return sentences

def coleman_liau_index(letters, words, sentences):
    L = (letters / words) * 100
    S = (sentences / words) * 100
    index = 0.0588 * L - 0.296 * S - 15.8
    return index

def main():
    text = input("Enter some text: ")
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)
    index = coleman_liau_index(letters, words, sentences)
    
    grade = round(index)
    if grade >= 16:
        print("Grade 16+")
    elif grade < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {grade}")


main()
