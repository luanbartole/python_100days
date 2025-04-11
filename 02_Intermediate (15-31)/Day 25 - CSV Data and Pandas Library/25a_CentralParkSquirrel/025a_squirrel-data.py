# Importing the pandas library for data manipulation and analysis
import pandas

# Reading the CSV file containing data about squirrels in Central Park
data = pandas.read_csv("central_park_squirrel_data.csv")

# Creating a dictionary to store fur colors and their corresponding counts
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],  # List of fur colors to count
    "Count": []  # This will be filled with the number of squirrels of each color
}

# Looping through each fur color in the list
for color in data_dict["Fur Color"]:
    # Counting the number of squirrels with the current fur color
    squirrel_count = len(data[data["Primary Fur Color"] == color])
    # Appending the count to the 'Count' list in the dictionary
    data_dict["Count"].append(squirrel_count)

# Creating a DataFrame from the dictionary to organize the data in tabular form
df = pandas.DataFrame(data_dict)

# Saving the DataFrame to a new CSV file called 'squirrel_count.csv'
df.to_csv("squirrel_count.csv")
