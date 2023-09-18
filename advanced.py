import customtkinter as tk
import threading

root = tk.CTk()
tk.set_appearance_mode("Dark") 
tk.set_default_color_theme("blue")

root.title("Caesar Encryption")
root.geometry("600x350")

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
    count = str(int(slider.get()))

    print(count)
    print(type(count))

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
tk.CTkLabel(
    master = root,
    text="Welcome to the Caesar Encryption",
    font = ("Courier", 18)
).pack(pady= (20, 5))

# Description
tk.CTkLabel(
    master = root,
    text="Please enter the text you would like to encrypt and the offset."
).pack(pady = (0, 10))


# Frame
framing = tk.CTkFrame(root)
framing.pack(pady=10)

# User inputs
tk.CTkLabel(framing, text = "Text:   ").grid(
    row = 0, 
    column = 0, 
    padx=10, 
    pady=(20,5)
)

user_password = tk.CTkEntry(framing, width=200)
user_password.focus_set()
user_password.grid(
    row=0,
    column = 1,
    padx=10,
    pady=(20,5)
)

tk.CTkLabel(framing, text = "Offset: ").grid(
    row = 1, 
    column = 0, 
    padx=10, 
    pady=(20,5)
)

slider = tk.CTkSlider(
    framing, 
    from_=-26, 
    to=26, 
    width=200, 
    number_of_steps= 26*2
)
slider.grid(
    row = 1,
    column = 1,
    pady=(10,5)
)

# Submit button
submit = tk.CTkButton(
    master = root,
    text="Enter",
    command = on_click
)
submit.pack(pady=(0, 20))

# Results
initial_password = tk.CTkLabel(root, text = "", font=("Courier", 14))
initial_password.pack()

encrypted_password = tk.CTkLabel(root, text = "", font=("Courier", 14))
encrypted_password.pack()

root.bind("<Return>", on_click)

root.mainloop()
