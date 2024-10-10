def main():
    # Prompt user for input
    user_input = input("Enter your text: ")

    # Replace spaces with three periods
    modified_input = user_input.replace(" ", "...")

    # Output the modified input
    print("Modified text:", modified_input)

main()
