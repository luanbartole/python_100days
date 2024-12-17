# This program calculates the split bill based on the tip percentage and number of people paying for it.

# Prints the header
print("="*50)
print(""" _______  ___  _______  _______  ___  _______ 
|       ||   ||       ||       ||   ||       |
|_     _||   ||    _  ||    _  ||   ||    ___|
  |   |  |   ||   |_| ||   |_| ||   ||   |___ 
  |   |  |   ||    ___||    ___||   ||    ___|
  |   |  |   ||   |    |   |    |   ||   |___ 
  |___|  |___||___|    |___|    |___||_______|""")
print("="*50)
print("Welcome to Tippie, your Tip Calculator!")
print("\nInformations:")

# Input
bill = float(input("Total Bill: $"))
tip = float(input("Tip Percentage (%): "))
people = int(input("Number of People: "))

# Calculate the individual bill rounded to 2 decimal numbers
split_bill = round(bill*(1+tip/100)/people,2)

# Output
print("="*50)
print(f"Individual Bill: ${split_bill}")
print("="*50)
