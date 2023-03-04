from tkinter import *
from tkinter import messagebox
import pyperclip
import generate


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pass():
    password = generate.password()
    generated_password = ""
    generated_password += password
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    global good
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        good = messagebox.askokcancel(title=website,
                                      message=f"These are the details that you have entered: \nEmail: {email},\nPassword: {password}\nIs t ok to save?")

    if good:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website}| {email} | {password}\n")
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("password manager")
window.config(padx=50, pady=50)

# adding the canvas image to the screen
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# adding labels to the window columns
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_Label = Label(text="Password")
password_Label.grid(row=3, column=0)

# adding entries
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", width=15, command=generate_pass)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=34, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
