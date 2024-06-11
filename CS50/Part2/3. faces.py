def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    userinput = input("Enter text: ")
    convertedtext = convert(userinput)
    print("Converted text:", convertedtext)


main()
