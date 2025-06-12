import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip  # Install with: pip install pyperclip

def generate_password():
    length = int(length_slider.get())
    use_upper = var_upper.get()
    use_lower = var_lower.get()
    use_digits = var_digits.get()
    use_symbols = var_symbols.get()

    pool = ""
    if use_upper:
        pool += string.ascii_uppercase
    if use_lower:
        pool += string.ascii_lowercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation

    if not pool:
        messagebox.showwarning("Warning", "Please select at least one character type!")
        return

    password = ''.join(random.choice(pool) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x320")
root.resizable(False, False)

# Variables
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=False)

# Widgets
tk.Label(root, text="Password Length", font=("Helvetica", 12)).pack(pady=5)
length_slider = tk.Scale(root, from_=4, to=32, orient=tk.HORIZONTAL)
length_slider.set(12)
length_slider.pack()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_upper).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lower).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Numbers", variable=var_digits).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols).pack(anchor='w', padx=20)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

password_entry = tk.Entry(root, font=("Helvetica", 14), justify="center", width=30)
password_entry.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack()

# Run GUI
root.mainloop()
