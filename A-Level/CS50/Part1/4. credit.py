def main():
    # Prompt user for credit card number
    card_number = input("Enter your credit card number: ")
    
    # Check if the input is a number
    if not card_number.isnumeric():
        print("INVALID")
        return
    
    # Check if the length of the card number is valid for American Express, MasterCard, or Visa
    if len(card_number) != 15 and len(card_number) != 16:
        print("INVALID")
        return
    
    # Check if it's an American Express card
    if len(card_number) == 15 and card_number.startswith(("34", "37")):
        print("AMEX")
        return
    
    # Check if it's a MasterCard
    if len(card_number) == 16 and card_number.startswith(("51", "52", "53", "54", "55")):
        print("MASTERCARD")
        return
    
    # Check if it's a Visa card
    if card_number.startswith("4"):
        print("VISA")
        return
    
    # If it doesn't match any of the above conditions, it's invalid
    print("INVALID")



main()
