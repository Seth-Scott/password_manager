from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    site = website_entry.get()
    email = email_usr_entry.get()
    password = password_entry.get()
    passwords = {site: email}

    is_ok = messagebox.askokcancel(title=site, message=f"These are the details entered:\nEmail: {email}\n"
                                               f" Password: {password}\n Okay to save?")

    if is_ok:
        if len(password) == 0 or len(password) == 0:
            messagebox.showinfo(title="ERROR", message="You cannot leave the email or password fields blank!")

        else:
            with open("passwords.txt", mode="a") as file:
                file.write(f"{site} | {email} | {password}\n")
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

generate_button = Button(text="Generate")
generate_button.grid(row=6, column=4)

add_button = Button(text="Add", width=32, command=add_password)
add_button.grid(row=7, column=3, columnspan=5)

window.mainloop()
