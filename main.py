from tkinter import *
from tkinter import messagebox
from random import choice, randint
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_list + symbol_list + number_list
    generated_password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    site = website_entry.get()
    email = email_usr_entry.get()
    password = password_entry.get()
    new_data = {
        site: {
            "email": email,
            "password": password
        }
                }

    if len(password) == 0 or len(password) == 0:
        messagebox.showinfo(title="ERROR", message="You cannot leave the email or password fields blank!")

    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("MyPass Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=3, column=3)


website_label = Label(text="Website:")
website_label.grid(row=4, column=2)

website_entry = Entry(width=35)
website_entry.grid(row=4, column=3, columnspan=2)
website_entry.focus()

email_usr_label = Label(text="Email/Username:")
email_usr_label.grid(row=5, column=2)

email_usr_entry = Entry(width=35)
email_usr_entry.grid(row=5, column=3, columnspan=2)
email_usr_entry.insert(0, "user@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=6, column=2)

password_entry = Entry(width=21)
password_entry.grid(row=6, column=3, columnspan=2, sticky="W")

generate_button = Button(text="Generate", command=generate_password)
generate_button.grid(row=6, column=4)

add_button = Button(text="Add", width=32, command=add_password)
add_button.grid(row=7, column=3, columnspan=5)

window.mainloop()
