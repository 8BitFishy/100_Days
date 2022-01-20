#FileNotFound
#with open("filename.txt") as file:
#   file.readlines()

#KeyError
#a_dictionary = {"key":"value"}
#value = a_dictionary["otherkey"]

#IndexError
#fruit_list = ["apple", "banana", "orange"]
#fruit = fruit_list[3]

#TypeError
#text = "abc"
#print(text+5)



'''
import os
import time

#os.remove("a_file.txt")
#time.sleep(5)

try:
    file = open("a_file.txt")
    a_dictionary = {"key":"value"}
    #print(a_dictionary["otherkey"])

except FileNotFoundError:
    print("File exception")
    file = open("a_file.txt", "w")
    file.write("something")

except KeyError as error_message:
    print(f"The key {error_message} does not exist")
    a_dictionary["otherkey"] = "othervalue"

else:
    print(file.read())

finally:
    print("Do something finally")
    file.close()
    raise KeyError("This is a made up error message")
'''



height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 2:
    raise ValueError("Humans are not that tall dingus")

bmi = weight / (height ** 2)

print(bmi)