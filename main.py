from tkinter import *
from tkinter import Canvas
from tkinter import Tk
from tkinter import PhotoImage
import random
import string

# --------------------- PASSWORD GENERATOR --------------------------------#


# ---------------------------- SAVE PASSWORD ------------------------------#
password = ""


def add():
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    with open("my_file.txt", mode="a+") as f:
        f.write(f"{website} | {user} | {password} \n")


def generate_password():
    global password
    password_entry.delete(0, END)
    password = []
    for i in range(4):
        password += random.choice(string.ascii_letters)
    for i in range(4):
        password += random.choice(string.digits)
    for i in range(4):
        password += random.choice(string.punctuation)

    random.shuffle(password)
    password = "".join(password)
    password_entry.insert(0, password)
    return password


# ---------------------------- UI SETUP -----------------------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="E")

email_lablel = Label(text="Email/Username:")
email_lablel.grid(column=0, row=2, sticky="E")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="E")

# entries

website_entry = Entry(width=36)
website_entry.grid(row=1, column=1, columnspan=2, sticky="WE")
website_entry.focus()

user_entry = Entry(width=36)
user_entry.grid(row=2, column=1, columnspan=2, sticky="W")
user_entry.insert(0, "jerrabomberra@gmail.com")

password_entry = Entry(text=password)
password_entry.grid(row=3, column=1, sticky="W")


# buttons
generate_password_button = Button(
    text="Generate Password",
    command=generate_password,
    fg="black",
)
generate_password_button.grid(column=2, row=3, sticky="E")

add_button = Button(text="Add", command=add, fg="black")
add_button.grid(column=1, row=4, columnspan=2, sticky="WE")


window.mainloop()
