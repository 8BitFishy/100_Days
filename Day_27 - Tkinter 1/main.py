from  tkinter import *



window = Tk()

window.title("GUI Program")

window.minsize(width=500, height=500)
window.config(padx=200, pady=200)


#label
my_label = Label(text = "Label 1", font = ("Arial", 24, "bold"))
my_label.config(text="New Label")
my_label.grid(column=0, row=0)


#button
def buttonfunction():
    my_label["text"] = input.get()

button = Button(text="Click me", command=buttonfunction)
button.grid(column=1, row=1)

#entry
input = Entry(width=10, )
input.insert(END, string="Type here...")
input.grid(column=3, row=2)

'''
#Text
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Some example text for you to look at here")
print(text.get("1.0", END))
text.pack()


#Spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width = 5, command=spinbox_used)
spinbox.pack()


#scale
def scale_used(value):
    print(value)

scale = Scale(from_=0, to =100, command=scale_used)
scale.pack()


#check button
def checkbutton_used():
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable = checked_state, command = checkbutton_used)
checked_state.get()
checkbutton.pack()


#radio button
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()



#listbox

def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits=["Apple", "Orange", "Pear", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

'''




window.mainloop()


