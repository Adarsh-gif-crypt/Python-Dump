from tkinter import *
import random
import string

root = Tk()
root.title('Random Password Generator')
root.geometry('300x200')

lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbols = string.punctuation
num = string.digits

all = lower + upper + num + symbols

label_chars = Label(root, text='Number of Characters', font = ('Arial',12)).pack(padx=10)
char_len = Entry(root, font = 'Arial 14')
char_len.pack(padx = 10)

def passgen():
    length = char_len.get()
    password = "".join(random.sample(all, int(length)))
    label_password.config(text='Generated Password: ' + password)

Button(root, text="Generate Password", command=passgen, font=('Arial', 12)).pack(padx=10)
label_password = Label(root, font=('Arial', 12))
label_password.pack()

root.mainloop()