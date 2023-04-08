from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title="copied", message="Password copied to clipboard")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_pass():
    website = website_entry.get()
    nick = nick_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty boxes", message="You've left some empty boxes")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"You've entered:\n\nUsername: {nick} \n"
                                                              f"Password: {password}\n\nIs it ok?")
        if is_ok:
            with open("saved_passwords.txt", mode="a") as file:
                file.write(f"\n{website}\n{nick} | {password}\n")
                website_entry.delete(0, END)
                pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=80, pady=80)

# Canvas
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

nick_label = Label(text="Email/Username:")
nick_label.grid(row=2, column=0)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

# Entry
website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

nick_entry = Entry(width=50)
nick_entry.grid(row=2, column=1, columnspan=2)
nick_entry.insert(0, "e-mail@website.com")
pass_entry = Entry(width=31)
pass_entry.grid(row=3, column=1)


# Button
pass_button = Button(text="Generate Password", width=15, command=password_generator)
pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=add_pass)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
