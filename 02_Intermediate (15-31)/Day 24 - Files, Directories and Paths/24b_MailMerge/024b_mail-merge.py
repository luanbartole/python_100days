# Step 1: Get the list of names from the file
with open("Input/Names/invited_names.txt") as file:
    invited_names = file.readlines()

# Remove the newline character from each name
for i in range(len(invited_names)):
    invited_names[i] = invited_names[i].strip()  # .strip() removes '\n' and other surrounding whitespace

# Step 2: Read the starting letter template
with open("Input/Letters/starting_letter.txt") as file:
    template = file.readlines()

# Step 3: Create and save a personalized letter for each invited name
for name in invited_names:
    # Join the template lines into a single string
    final_letter = ''.join(template)

    # Replace the placeholder [name] with the actual name
    final_letter = final_letter.replace("[name]", name)

    # Save the personalized letter in the Output/ReadyToSend directory
    with open(f"Output/ReadyToSend/{name}.txt", mode="w") as file:
        file.write(final_letter)
