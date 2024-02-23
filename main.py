
# TASK:03 - PASSWORD GENERATOR USING TKINTER IN PYTHON

from tkinter import *
import random
import string

root = Tk()

def generator():
    special_character = string.punctuation
    numbers = string.digits
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase

    all=special_character+numbers+small_alphabets+capital_alphabets
    password_length = int(length_Box.get())

    if choice.get() == 1:
        password_value.insert(0, random.sample(small_alphabets, password_length))

    if choice.get() == 2:
        password_value.insert(0, random.sample(small_alphabets+capital_alphabets, password_length))

    if choice.get() == 3:
        password_value.insert(0, random.sample(all, password_length))

root.geometry("300x400")
root.config(background="black")
Font =("times new roman", 15, "bold")
choice = IntVar()

root.title("Password Generator")
label =Label(root, text="Password Generator", font=("times new roman", 20, "bold"), foreground="white", background="black", borderwidth=3)
label.grid(pady=8)

checkbutton1 =Radiobutton(root,text="weak", font=Font,background="red", variable=choice, value=1, borderwidth=3)
checkbutton1.grid(pady=5)

checkbutton2 =Radiobutton(root,text="Medium", font=Font,background="light green", variable=choice, value=2, borderwidth=3)
checkbutton2.grid(pady=5)

checkbutton3 =Radiobutton(root,text="Strong", font=Font,background="dark green", variable=choice, value=3, borderwidth=3)
checkbutton3.grid(pady=5)

length_label =Label(root, text="Password length", font=("times new roman", 20, "bold"), foreground="white", background="black", borderwidth=3)
length_label.grid(pady=5)

length_Box = Spinbox(root,from_=4,to=10,width=5,font=("times new roman", 15, "bold"))
length_Box.grid(pady=5)

Button(root,text="generate", font=Font, command=generator).grid(pady=5)

password_value = Entry(root, width=30, borderwidth=3)
password_value.grid(pady=5)

root.mainloop()