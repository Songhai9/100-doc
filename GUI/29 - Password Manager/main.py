from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(index=0, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()

    is_ok = messagebox.askokcancel(
        title=f"{website}",
        message=f"These are the details entered\nEmail: {email}\nPassword: {password}\nIs it ok to save?",
    )
    if is_ok:
        if len(website) == 0:
            messagebox.showerror(
                title="Email missing", message="Please write an email/username"
            )
        elif len(password) == 0:
            messagebox.showerror(
                title="Password missing", message="Please write a password"
            )
        else:
            with open("passwords.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200, highlightthickness=0)
pic = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pic)


website_label = Label(text="Website")
username_label = Label(text="Email/Username")
password_label = Label(text="Password")

website_entry = Entry(width=35)
username_entry = Entry(width=35)
password_entry = Entry(width=21)

add_btn = Button(text="Add", width=36, command=save_password)
generate_btn = Button(text="Generate password", command=generate_password)

canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
username_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)
website_entry.grid(row=1, column=1, columnspan=2)
username_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)
add_btn.grid(row=4, column=1, columnspan=2)
generate_btn.grid(row=3, column=2)

website_entry.focus()
username_entry.insert(index=0, string="doosix@outlook.fr")

window.mainloop()
