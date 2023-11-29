import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength(password):
    messages = []

    # Check if password is at least 12 characters long
    if len(password) < 12:
        messages.append("Password should be at least 12 characters long.")

    # Check if password has a mix of uppercase and lowercase letters
    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password):
        messages.append("Password should include a mix of uppercase and lowercase letters.")

    # Check if password has numbers and special symbols
    if not any(char.isdigit() for char in password) or not any(char in r'!@#$%^&*(),.?":{}|<>' for char in password):
        messages.append("Password should include numbers and special symbols.")

    # Check if password contains memorable keyboard paths
    keyboard_paths = ['qwerty', 'asdfgh', 'zxcvbn', '123456']
    for path in keyboard_paths:
        if path in password.lower():
            messages.append("Password should not contain memorable keyboard paths.")

    # Check if password is based on personal information
    personal_info = ['name', 'birthdate', 'password', 'admin']
    for info in personal_info:
        if info in password.lower():
            messages.append("Password should not be based on personal information.")

    # Check if password is unique for each account
    # You might implement additional logic for this, such as checking against a stored list of previous passwords

    if not messages:
        return "Password is strong!"
    else:
        return "\n".join(messages)

def check_password(event=None):
    password = entry.get()
    strength_result = check_password_strength(password)
    result_label.config(text=strength_result, fg='#61dafb')

# Cooler theme
root = tk.Tk()
root.title("Cool Password Strength Checker")

# Set background color
root.configure(bg='#282c34')

# Change label and button colors
label = tk.Label(root, text="Enter your password:", fg='#61dafb', bg='#282c34', font=('Helvetica', 14))
label.pack(pady=10)

entry = tk.Entry(root, show="*", font=('Helvetica', 12))
entry.pack(pady=10)

check_button = tk.Button(root, text="Check Password", command=check_password, bg='#61dafb', fg='#282c34', font=('Helvetica', 12, 'bold'))
check_button.pack(pady=10)

# Display password strength result
result_label = tk.Label(root, text="", fg='#61dafb', bg='#282c34', font=('Helvetica', 12))
result_label.pack(pady=10)

# Change window size and add padding
root.geometry("600x400")
root.resizable(False, False)

# Bind the Enter key to the check_password function
root.bind("<Return>", check_password)

root.mainloop()
