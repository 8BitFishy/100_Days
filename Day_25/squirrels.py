import csv
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

'''red = grey = black = 0

colours = data["Primary Fur Color"].to_list()

for colour in colours[1:]:
    if colour == 'Cinnamon':
        red+=1
    elif colour == 'Gray':
        grey += 1
    elif colour == 'Black':
        black += 1
    elif str(colour).lower() == "nan":
        pass
    else:
        print(f"Unrecognised colour found - {colour}")

new_data_dict = {
    'Fur': ["Grey", "Red", "Black"],
    'Count': [grey, red, black]
}

new_data = pandas.DataFrame(new_data_dict)

print(new_data)
new_data.to_csv("Colours")
'''

grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

new_data_dict = {
    'Fur': ["Grey", "Red", "Black"],
    'Count': [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

new_data = pandas.DataFrame(new_data_dict)

print(new_data)
new_data.to_csv("Colours")