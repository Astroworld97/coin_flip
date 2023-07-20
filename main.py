import numpy as np
from tkinter import *
from PIL import Image, ImageTk

#Source: https://www.askpython.com/python-modules/tkinter/coin-flip-gui

def coinFlip():
    result = np.random.binomial(1,0.5)
    tfield.delete("1.0", "end")

    if result==1:
        tfield.insert(INSERT, "It's ---> HEADS")
        i.config(image = heads)
    else:
        tfield.insert(INSERT, " It's ————> TAILS")
        i.config(image = tails)

root = Tk()
root.title("Python Coin Flip")

#load heads image
load = Image.open("head.png")
heads = ImageTk.PhotoImage(load)
 
#load tails image
load = Image.open("tail.jpg")
tails = ImageTk.PhotoImage(load)

i = Label(root, image=heads)
i.pack()

root.geometry("500x500")
#create the button
b1 = Button(root, text="Toss the Coin", font=("Arial", 10), command=coinFlip, bg='green', fg='white', activebackground="red", padx=10, pady=10)
b1.pack() #Note: We use the pack() method for every element we want to render on our main window.

#create the text field to show the result of the coin flip
tfield = Text(root, width=52, height=5) 
tfield.pack()#Note: We use the pack() method for every element we want to render on our main window.
tfield.insert(INSERT, "Click on the Button.. To Flip the Coin and get the result")

root.mainloop()
