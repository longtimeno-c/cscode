import random

# Generate a list of random first names
first_names = ["Alice", "Bob", "Charlie", "David", "Emily", "Frank", "Grace", "Henry", "Isabelle", "Jane"]

# Generate a list of random surnames
surnames = ["Smith", "Jones", "Brown", "Taylor", "Wilson", "Davies", "Evans", "Robinson", "Wright", "Thompson"]

# Shuffle the lists to generate random combinations of first names and surnames
random.shuffle(first_names)
random.shuffle(surnames)

# Create a list of names by combining the first names and surnames
names = ["{} {}".format(first, surname) for first, surname in zip(first_names, surnames)]

# Export the names to a register file
with open("Register.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

# Create a list of subjects
subjects = ["Maths", "English", "Science", "History", "Geography"]

# Generate a random report for each student and each subject
for student in names:
    # Create a dictionary to store the reports for each subject
    reports = {}

    # Generate a random report for each subject
    for subject in subjects:
        # Generate a random grade between 1 and 10
        grade = random.randint(1, 10)

        # Generate a random report comment
        if grade < 5:
            comment = "well"
        elif grade < 8:
            comment = "Satisfactory"
        else:
            comment = "Excellent"

        # Generate a detailed paragraph for the subject
        paragraph = "{} has performed {} in {} this term. {} has demonstrated a good understanding of the subject, but there is still room for improvement. In the next term, {} should focus on {} in order to improve their grade. Overall, {} is making good progress in {}.".format(student, comment, subject, student, student, subject, student, subject)

        # Add the report to the dictionary
        reports[subject] = paragraph

    # Export the reports to a text file named after the student
    with open(student + ".txt", "w") as file:
        file.write("School report for {}:\n\n".format(student))
        for subject, paragraph in reports.items():
            file.write("{}:\n".format(subject))
            file.write("{}\n\n".format(paragraph))
