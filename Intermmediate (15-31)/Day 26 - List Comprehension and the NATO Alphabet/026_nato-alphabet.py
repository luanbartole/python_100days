import pandas

# Open csv containing the data.
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Dictionary comprehension to map letters to their phonetic code.
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

while True:
    name = input("Write a name: ").upper()
    try:
        nato_name = [phonetic_dict[letter] for letter in name]
    except KeyError as e:
        print(f"Character '{e.args[0]}' is not valid. Please enter only A-Z letters.")
    else:
        print(nato_name)
        break
