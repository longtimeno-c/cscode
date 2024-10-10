import random

# Set the number of corns to a random value between 200 and 250
num_corns = random.randint(200, 250)

# Set the quality of each corn to a random value between 1.0 and 2.0
corns = [(i, random.uniform(1.0, 2.0)) for i in range(num_corns)]

# Remove any corn with a quality value below 1.5
corns = [corn for corn in corns if corn[1] >= 1.5]

# Calculate the number of corns above various quality thresholds
num_above_1 = len([corn for corn in corns if corn[1] > 1])
num_above_1_2 = len([corn for corn in corns if corn[1] > 1.2])
num_above_1_5 = len([corn for corn in corns if corn[1] > 1.5])
num_above_1_8 = len([corn for corn in corns if corn[1] > 1.8])

# Calculate the number of corns available for sale
num_for_sale = len(corns)

# Calculate the discount based on the number of corns purchased
if num_for_sale >= 10:
    discount = 0.05
elif num_for_sale >= 15:
    discount = 0.1
else:
    discount = 0

# Calculate the number of corns removed for poor quality
num_removed = num_corns - num_for_sale

# Export the data to a text file
# Export the data to a text file
with open("corns.txt", "w") as file:
    file.write("Number of corns above various quality thresholds:\n")
    file.write("- Above 1.0: {}\n".format(num_above_1))
    file.write("- Above 1.2: {}\n".format(num_above_1_2))
    file.write("- Above 1.5: {}\n".format(num_above_1_5))
    file.write("- Above 1.8: {}\n".format(num_above_1_8))
    file.write("Number of corns available for sale: {}\n".format(num_for_sale))
    file.write("Discount applied: {}%\n".format(discount*100))
    file.write("Number of corns removed for poor quality: {}\n".format(num_removed))
