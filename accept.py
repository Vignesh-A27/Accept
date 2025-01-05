import tkinter as tk
import random

def show_popup():
    popup = tk.Toplevel(root)
    popup.title("I Knew It !!!!!!")
    label = tk.Label(popup, text="Thanks for Accepting ❤️💕")
    label.pack(padx=40, pady=40)

def move_button(event):
    x = random.randint(0, 650)
    y = random.randint(0, 650)
    no_button.place(x=x, y=y)
    
root = tk.Tk()

root.title("Hi nga 😃")
root.geometry("800x800")
question_label = tk.Label(root, text="Do you like me? 🥺")

question_label.pack(pady=20)

yes_button = tk.Button(root, text="Yes", command=show_popup)
yes_button.pack()

no_button = tk.Button(root, text="No")
no_button.pack()

no_button.bind("<Enter>", move_button)

root.mainloop()