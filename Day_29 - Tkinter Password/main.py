from tkinter import *
from random import randrange, choice
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    Password_Input.delete(0, "end")
    password = ""
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
               "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    symbols = ["!", "&", "%", "$", "*", "/", "+", "#"]

    for i in range(20):
        character_select = randrange(0, 3)
        if character_select == 0:
            character = choice(letters)
            if randrange(0, 2) == 1:
                character = character.capitalize()
            else:
                pass
        elif character_select == 1:
            character = randrange(0, 10)
        else:
            character = choice(symbols)
        password = password + str(character)
    Password_Input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def checkforduplicated(website, password):
    saved_websites = []
    saved_passwords = []
    website = website.strip().lower()
    password = password.strip().lower()

    with open("ultra_top_secret.txt", 'r') as file:

        entries = file.readlines()

        for i in range(len(entries)):
            info = entries[i].split("|")
            for j in range(len(info)):
                info[j] = info[j].strip().lower()
                if j == 0:
                    saved_websites.append(info[j])
                elif j == 1:
                    pass
                else:
                    saved_passwords.append(info[j])


    if website in saved_websites:
        print("website already used")
        label.config(text="Website used!")
        return True

    for entry in saved_passwords:
        if str(password) == str(entry):
            print("password already used")
            label.config(text="Password used!")
            return True

    label.config(text="")
    return False

def save_password():

    website = Website_Input.get().strip()
    username = Usr_Input.get().strip()
    password = Password_Input.get().strip()

    if len(website) != 0 and len(password) != 0:
        data = [website, username, password]
        if not checkforduplicated(website, password):
            with open("ultra_top_secret.txt", 'a') as file:
                if messagebox.askokcancel(title=f"{website.capitalize()} Login Details Saved", message=f"Website: {website.capitalize()}\nUsername: {username}\nPassword: {password}\nAre you sure you want to save?"):
                    file.write(f"\n{website} | {username} | {password}")
                    print(data)
    else:
        messagebox.showwarning(title="Invalid entry", message="One or more fields are empty, please enter a valid entry.")






# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(bg="white", padx=20, pady=20)
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
bg = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg)
canvas.grid(row=0, column=1)

Website_Label = Label(text="Website:", bg="white", padx=15)
Website_Label.grid(row=1, column=0)

Website_Input = Entry(relief="groove", bg="white", width=35)
Website_Input.focus()
Website_Input.grid(row=1, column=1, columnspan=2, sticky="EW")

Usr_Label = Label(text="Username/Email:", bg="white", padx=15)
Usr_Label.grid(row=2, column=0)

Usr_Input = Entry(relief="groove", bg="white", width=35)
Usr_Input.insert(0, "sowerbutts.pg@hotmail.com")
Usr_Input.grid(row=2, column=1, columnspan=2, sticky="EW")

Password_Label = Label(text="Password:", bg="white", padx=15)
Password_Label.grid(row=3, column=0)

Password_Input = Entry(relief="groove",bg="white", width=21)
Password_Input.grid(row=3, column=1, sticky="EW")

Generate_Button = Button(text="Generate Password", bg="white", command=generate_password)
Generate_Button.grid(row=3, column=2, sticky="EW")

Save_Button = Button(text="Save", bg="white", width=36, command=save_password)
Save_Button.grid(row=4, column=1, columnspan=2, sticky="EW")

label = Label(text="", bg = "white")
label.grid(row=4, column=0, sticky="EW")

window.mainloop()
