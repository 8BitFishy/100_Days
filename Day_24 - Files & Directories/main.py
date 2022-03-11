
with open("Names/names.txt") as file:
    names = file.readlines()
    for i in range(len(names)):
        names[i] = names[i].strip()

with open("Template.txt") as template:
    text = template.read()

for recipient in names:
    with open(f"Output/{recipient}.txt", 'w') as letter:
        letter.write(f"Dear {recipient}\n")
        letter.write(text)
