def dollars_to_float(d):
    # Check if the input string contains "$"
    if '$' in d:
        # Split the input string at the "$" symbol and convert the second part to float
        return float(d.split('$')[1])
    else:
        # If no "$" symbol is found, directly convert the input string to float
        return float(d)


def percent_to_float(p):
    # Check if the percentage ends with %
    if p.endswith('%'):
        # Remove the % sign and convert to float
        return float(p[:-1]) / 100
    else:
        # If no % sign is found, assume it's a whole number percentage
        return float(p) / 100

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    #print("Meal cost:", dollars)
    percent = percent_to_float(input("What percentage would you like to tip? "))
    #print("Tip percentage:", percent)
    tip = dollars * (percent / 100)  # Convert percentage to fraction
    print(f"Leave ${tip:.2f}")

main()
