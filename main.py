from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website_entry.grid(row=4, column=3)

email_usr_label = Label(text="Email/Username:")
email_usr_label.grid(row=5, column=2)

email_usr_entry = Entry(width=35)
email_usr_entry.grid(row=5, column=3)



window.mainloop()
