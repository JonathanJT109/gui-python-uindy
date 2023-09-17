import tkinter as tk
from tkinter import ttk

import sv_ttk


root = tk.Tk()

root.title("Caesar Encryption")
root.geometry("600x350")
# root.config(bg="blue")


# Caesay Encrypt Function
def caesarEncrypt(text: str, n: int = 0):
    for i in range(len(text)):
        s = ord(text[i])
        if text[i].isalpha():
            if text[i].islower():
                s = (((s + n) - ord('a')) % 26) + ord('a')
            else: 
                s = (((s + n) - ord('A')) % 26) + ord('A')
            text = text[:i] + chr(s) + text[i + 1:]
    return text


# on_click: Function called when user presses enter or clicks the enter button
def on_click(event=None):
    global user_password
    global user_offset
    
    string = user_password.get()
    count = user_offset.get()

    if len(string) == 0:
        initial_password.configure(text="Please enter a password")
        return

    if not count.strip('-').isdigit() or count == None:
        initial_password.configure(text="Please enter a number")
        return

    encrypted_string = caesarEncrypt(string, int(count))
    initial_password.configure(text=f'Initial String:   {string}')
    encrypted_password.configure(text=f'Encrypted String: {encrypted_string}')

# UI 

# Title
tk.Label(
    text="Welcome to the Caesar Encryption",
    font = ("Courier 18 bold")
).pack(pady= (20, 5))

# Description
tk.Label(
    text="Please enter the text you would like to encrypt and the offset."
).pack(pady = (0, 10))


# Frame
framing = tk.Frame(root)
framing.pack(pady=10)

# User inputs
tk.Label(framing, text = "Text:   ").grid(
    row = 0, 
    column = 0, 
    padx=10, 
    pady=(20,5)
)

user_password = tk.Entry(framing, width=20)
user_password.focus_set()
user_password.grid(
    row=0,
    column = 1,
    padx=10,
    pady=(20,5)
)

tk.Label(framing, text = "Offset: ").grid(
    row = 1, 
    column = 0, 
    padx=10, 
    pady=(20,5)
)

user_offset = tk.Entry(framing, width=5)
user_offset.grid(
    row=1,
    column = 1,
    padx=10,
    pady=(10,5)
)
user_offset.focus_set()

# Submit button
submit = tk.Button(
    text="Enter",
    width = 10,
    height = 1,
    command = on_click,
    bg = "#3861a8"
)
submit.pack(pady=(0, 20))

# Results
initial_password = tk.Label(root, text = "", font=("Courier"))
initial_password.pack()

encrypted_password = tk.Label(root, text = "", font=("Courier"))
encrypted_password.pack()

root.bind("<Return>", on_click)

sv_ttk.set_theme("dark")

root.mainloop()
