def calculate_energy(mass):
    c = 300000000  # Speed of light in meters per second
    energy = mass * c**2
    return energy

def main():
    mass = int(input("Enter the mass (in kilograms): "))
    energy = calculate_energy(mass)
    print("Equivalent energy (in Joules):", energy)


main()