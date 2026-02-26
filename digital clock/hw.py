
import time
from tkinter import *
from tkinter.ttk import *
from time import strftime
import random

root = Tk()
root.title("Party Clock")


colours = ["red", "blue", "green", "purple", "orange", "pink"]

def update_time():
    current_time = strftime("%I:%M:%S %p")
    lbl.config(text=current_time)
    colour = random.choice(colours)
    root.config(bg=colour)
    lbl.config(background=colour)
    lbl.after(1000, update_time)

lbl = Label(root, font=("calibri", 40, "bold"), foreground="white", background="black")
lbl.pack(anchor="center", padx=20, pady=20)

update_time()
root.mainloop()





