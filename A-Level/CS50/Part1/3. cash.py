# What coins to give when someone needs x amount of change

## Ensuring its a positive number
def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative value.")
        except ValueError:
            print("Please enter a valid number.")

## Calculating coins needed from amount
def calculate_change(change):
    # Convert pounds to pence to avoid precision issues
    change_pence = int(change * 100)
    coins = {50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
    
    for coin in coins:
        while change_pence >= coin:
            coins[coin] += 1
            change_pence -= coin
    
    return coins

def main():
    change = get_float("Change owed in pounds: ")
    coin_breakdown = calculate_change(change)
    print("Coins needed:")
    for coin, count in coin_breakdown.items():
        if count > 0:
            print(f"{count} coin(s) of {coin:.2f} pounds")


main()
