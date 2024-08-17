from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)

    letters_in_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters_in_lowercase = "abcdefghijklmnopqrstuvwxyz"
    special_keywords = "!?@#$%&_~"
    numbers = "0123456789"

    string = list(letters_in_uppercase + letters_in_lowercase + special_keywords + numbers)
    pass_length = 12

    password = "".join(random.sample(string, pass_length))
    password_entry.insert(0, password)
    pyperclip.copy(password)
    print(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {website: {
        "email": email,
        "password": password
    }}

    if not all([website, password]):
        messagebox.showerror(title="Oops", message="Please make sure you haven't left any field empty")
    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(new_data, file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().title()

    if not website:
        messagebox.showerror(title="Oops",
                             message="Please make sure you haven't left the website field empty to search")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="Data file not found")
        else:
            website_data = data.get(website)
            if website_data:
                messagebox.showinfo(title=website,
                                    message=f"Email:{website_data['email']}\nPassword:{website_data['password']}")
            else:
                messagebox.showerror(title="Error", message="No details for the website exist")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=34)
website_entry.grid(row=1, column=1)
email_entry = Entry(width=34)
email_entry.insert(0, "demahomali01@gmail.com")
email_entry.grid(row=2, column=1)
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

# Buttons
generate_btn = Button(text="Generate", command=generate_password)
generate_btn.grid(row=3, column=2)

save_btn = Button(text="Add", width=37, command=save)
save_btn.grid(row=4, column=1, columnspan=3)

search_btn = Button(text="Search", padx=5, command=find_password)
search_btn.grid(row=1, column=2)

window.mainloop()
