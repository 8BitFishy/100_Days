import csv
import pandas

#No pandas
print("Using no pandas")
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        print(row)
        if row[1] != 'Temperature':
            temperatures.append(int(row[1]))
    print("\n", temperatures,"\n\n\n")

#Pandas
#read csv
print("Using pandas")
data = pandas.read_csv("weather_data.csv")
print(data)
print()

#get column data
print("Getting a column:")
temperatures = data["Temperature"]
print(temperatures)
print(data.Condition)


#Get data types
print("\nGet data types")
print(type(data))
print(type(temperatures))
print()

#Converting data
print("Converting data to dict")
data_dict = data.to_dict()
print(data_dict)
print()

#Converting and manipulating list
print("Converting data to list and manipulating")
temp_list = data["Temperature"].to_list()

print(f"Average = {sum(temp_list) / len(temp_list)}")
print(f"Average = {data['Temperature'].mean()}")
print(f"Max temp = {data['Temperature'].max()}")
print()

#Getting bits of data
print("Getting bits of data")
print(data[data.Day == "Monday"])
print()
max_temp = data['Temperature'].idxmax()
print(f"Hottest day was {data.Day[max_temp]}")
print()
print(data[data.Day == "Monday"].Temperature * 9/5 + 32)
print()

#Creating datasets
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
print("Creating dataframes and csv files")
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("created_csv")


print(f"\nIterating through dataframe")
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(value)

student_dataframe = pandas.DataFrame(student_dict)
print("\n", student_dataframe, "\n")

#loop through columns
print("\nLoop through columns\n")
for (key, value) in student_dataframe.items():
    print("Key:", key)
    print("Values:\n", value, "\n")

#loop through rows
print("\nLoop through rows\n")
for (index, row) in student_dataframe.iterrows():
    print("index:", index)
    print(f"student: {row.student}, score: {row.score}\n")

#loop through rows
print("\nLoop through keys and items\n")
for (x, y) in student_dataframe.iteritems():
    print("Key: ", x)
    print(y)

print("\n\n\n\n")

nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
print(nato_dataframe)
for (index, row) in nato_dataframe.iterrows():
    print(row)

phonetic_alphabet = {row.letter: row.code for (index, row) in nato_dataframe.iterrows()}
print("\n\nDict:\n")
print(phonetic_alphabet)

word = input("Enter a word: ").upper()
code = [phonetic_alphabet[letter] for letter in word]
print(code)