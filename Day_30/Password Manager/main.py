import json
from tkinter import *
from random import randrange, choice
from tkinter import messagebox
import pyperclip


# ---------------------------- Save Data ------------------------------- #

def Save_Data(new_data):
    with open("ultra_top_secret.json", 'w') as file:
        json.dump(new_data, file, indent=4)


# ---------------------------- Search Data ------------------------------- #

def Search():
    website = Website_Input.get().strip().lower()

    try:
        with open("ultra_top_secret.json", 'r') as file:
            entries = json.load(file)
            for entry in entries:
                if website == entry.lower():
                    username = entries[entry]["username"]
                    password = entries[entry]["password"]
                    Password_Input.delete(0, "end")
                    Usr_Input.delete(0, "end")
                    Password_Input.insert(0, password)
                    Usr_Input.insert(0, username)
                    pyperclip.copy(password)
                    return

            label.config(text="Not found")


    except FileNotFoundError:
        label.config(text="No datafile found")

    except ValueError:
        label.config(text="No data found")


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
    website = website.lower()
    password = password.lower()

    try:
        with open("ultra_top_secret.json", 'r') as file:
            entries = json.load(file)

        for entry in entries:
            if website == entry.lower():
                print("website already used!")
                label.config(text="Website used!")
                return True

        for entry in entries.values():
            if password == entry["password"].lower():
                print("password already used!")
                label.config(text="Password used!")
                return True

        label.config(text="")
        return False

    except FileNotFoundError:
        return False

    except ValueError:
        return False


def save_password():
    website = Website_Input.get().strip()
    username = Usr_Input.get().strip()
    password = Password_Input.get().strip()
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }
    if len(website) != 0 and len(password) != 0:
        if not checkforduplicated(website, password):
            if messagebox.askokcancel(title=f"{website.capitalize()} Login Details Saved",
                                      message=f"Website: {website.capitalize()}\nUsername: {username}\nPassword: {password}\nAre you sure you want to save?"):
                try:
                    with open("ultra_top_secret.json", 'r') as file:
                        data = json.load(file)

                except FileNotFoundError:
                    Save_Data(new_data)

                except ValueError:
                    Save_Data(new_data)

                else:
                    data.update(new_data)
                    Save_Data(data)
    else:
        messagebox.showwarning(title="Invalid entry",
                               message="One or more fields are empty, please enter a valid entry.")


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
Website_Input.grid(row=1, column=1, sticky="EW")

Search_Button = Button(text="Search", bg="white", command=Search)
Search_Button.grid(row=1, column=2, sticky="EW")

Usr_Label = Label(text="Username/Email:", bg="white", padx=15)
Usr_Label.grid(row=2, column=0)

Usr_Input = Entry(relief="groove", bg="white", width=35)
Usr_Input.insert(0, "sowerbutts.pg@hotmail.com")
Usr_Input.grid(row=2, column=1, columnspan=2, sticky="EW")

Password_Label = Label(text="Password:", bg="white", padx=15)
Password_Label.grid(row=3, column=0)

Password_Input = Entry(relief="groove", bg="white", width=21)
Password_Input.grid(row=3, column=1, sticky="EW")

Generate_Button = Button(text="Generate Password", bg="white", command=generate_password)
Generate_Button.grid(row=3, column=2, sticky="EW")

Save_Button = Button(text="Save", bg="white", width=36, command=save_password)
Save_Button.grid(row=4, column=1, columnspan=2, sticky="EW")

label = Label(text="", bg="white")
label.grid(row=4, column=0, sticky="EW")

window.mainloop()
