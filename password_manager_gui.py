import tkinter as tk
from tkinter import messagebox
import random
import string

# ---------------- PASSWORD STORAGE ----------------

passwords = {}

try:
    with open("password.txt", "r") as file:
        for line in file:
            site, pwd = line.strip().split(":")
            passwords[site] = pwd
except:
    pass

# ---------------- FUNCTIONS ----------------

def save_password():
    site = website_entry.get()
    pwd = password_entry.get()

    if site == "" or pwd == "":
        messagebox.showerror("Error", "Fields cannot be empty!")
        return

    passwords[site] = pwd

    with open("password.txt", "a") as file:
        file.write(f"{site}:{pwd}\n")

    messagebox.showinfo("Success", "Password Saved Successfully ✅")

    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


def view_password():
    output.delete("1.0", tk.END)

    if not passwords:
        output.insert(tk.END, "No Passwords Saved ❌")
    else:
        for site, pwd in passwords.items():
            output.insert(tk.END, f"{site} --> {pwd}\n")


def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"

    pwd = "".join(random.choice(chars) for _ in range(8))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, pwd)


def check_strength():

    pwd = password_entry.get()

    if len(pwd) < 6:
        result = "Weak Password 😭"

    elif (
        len(pwd) >= 8
        and any(char.isupper() for char in pwd)
        and any(char.islower() for char in pwd)
        and any(char.isdigit() for char in pwd)
        and any(char in "!@#$%^&*" for char in pwd)
    ):

        result = "Strong Password 🔥"

    else:
        result = "Medium Password 🙂"

    messagebox.showinfo("Strength Checker", result)


def search_password():

    site = website_entry.get()

    output.delete("1.0", tk.END)

    if site in passwords:
        output.insert(tk.END, f"Website : {site}\n")
        output.insert(tk.END, f"Password : {passwords[site]}")
    else:
        output.insert(tk.END, "Website not found ❌")


def delete_password():

    site = website_entry.get()

    if site in passwords:

        del passwords[site]

        with open("password.txt", "w") as file:
            for s, p in passwords.items():
                file.write(f"{s}:{p}\n")

        messagebox.showinfo("Deleted", "Password Deleted ☠️")

    else:
        messagebox.showerror("Error", "Website not found!")


# ---------------- GUI ----------------

root = tk.Tk()

root.title("Personal Password Manager")
root.geometry("500x500")
root.config(bg="black")

# TITLE

title = tk.Label(
    root,
    text="🔐 PASSWORD MANAGER",
    font=("Arial", 20, "bold"),
    bg="black",
    fg="cyan"
)

title.pack(pady=10)

# WEBSITE

website_label = tk.Label(
    root,
    text="Website",
    font=("Arial", 12),
    bg="black",
    fg="white"
)

website_label.pack()

website_entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 12)
)

website_entry.pack(pady=5)

# PASSWORD

password_label = tk.Label(
    root,
    text="Password",
    font=("Arial", 12),
    bg="black",
    fg="white"
)

password_label.pack()

password_entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 12)
)

password_entry.pack(pady=5)

#OUTPUT BOX
output = tk.Text(
    root,
    height=8,
    width=45,
    font=("Arial", 10)
)
output.pack(pady=10)

# BUTTONS

save_btn = tk.Button(
    root,
    text="Save Password",
    command=save_password,
    bg="cyan",
    fg="black",
    width=20
)

save_btn.pack(pady=5)

view_btn = tk.Button(
    root,
    text="View Passwords",
    command=view_password,
    bg="cyan",
    fg="black",
    width=20
)

view_btn.pack(pady=5)

generate_btn = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    bg="cyan",
    fg="black",
    width=20
)

generate_btn.pack(pady=5)

strength_btn = tk.Button(
    root,
    text="Check Strength",
    command=check_strength,
    bg="cyan",
    fg="black",
    width=20
)

strength_btn.pack(pady=5)

search_btn = tk.Button(
    root,
    text="Search Password",
    command=search_password,
    bg="cyan",
    fg="black",
    width=20
)

search_btn.pack

root.mainloop()