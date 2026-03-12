from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("tic tac toe")


window.configure(bg="lightblue")   

turn = 1
result = ""

def win ():
    global result
    if b1.cget("text")==b2.cget("text")==b3.cget("text")=="X":
        result="player1 wins !"
    elif b1.cget("text")==b2.cget("text")==b3.cget("text")=="O":
        result="player2 wins !"
    elif b4.cget("text")==b5.cget("text")==b6.cget("text")=="X":
        result="player1 wins !"
    elif b4.cget("text")==b5.cget("text")==b6.cget("text")=="O":
        result="player2 wins !"
    elif b7.cget("text")==b8.cget("text")==b9.cget("text")=="X":
        result="player1 wins !"
    elif b7.cget("text")==b8.cget("text")==b9.cget("text")=="O":
        result="player2 wins !"

    elif b1.cget("text")==b4.cget("text")==b7.cget("text")=="X":
        result="player1 wins !"
    elif b1.cget("text")==b4.cget("text")==b7.cget("text")=="O":
        result="player2 wins !"
    elif b2.cget("text")==b5.cget("text")==b8.cget("text")=="X":
        result="player1 wins !"
    elif b2.cget("text")==b5.cget("text")==b8.cget("text")=="O":
        result="player2 wins !"
    elif b3.cget("text")==b6.cget("text")==b9.cget("text")=="X":
        result="player1 wins !"
    elif b3.cget("text")==b6.cget("text")==b9.cget("text")=="O":
        result="player2 wins !"

    elif b1.cget("text")==b5.cget("text")==b9.cget("text")=="X":
        result="player1 wins !"
    elif b1.cget("text")==b5.cget("text")==b9.cget("text")=="O":
        result="player2 wins !"
    elif b3.cget("text")==b5.cget("text")==b7.cget("text")=="X":
        result="player1 wins !"
    elif b3.cget("text")==b5.cget("text")==b7.cget("text")=="O":
        result="player2 wins !"
    else:
        return

    messagebox.showinfo("result",str(result))
    window.destroy()


def b1click ():
    global turn
    mytext = b1.cget("text")
    if mytext==" ":
        if turn == 1:
            b1.configure(text = "X")
            turn = 2
        else:
            b1.configure(text = "O")
            turn = 1
        Lbl.configure(text = "player"+ str(turn) + "turn")
        win()


def b2click ():
    global turn
    mytext = b2.cget("text")
    if mytext==" ":
        if turn == 1:
            b2.configure(text = "X")
            turn = 2
        else:
            b2.configure(text = "O")
            turn = 1
        Lbl.configure(text = "player"+ str(turn) + "turn")
        win()


def b3click ():
    global turn
    mytext = b3.cget("text")
    if mytext==" ":
        if turn == 1:
            b3.configure(text = "X")
            turn = 2
        else:
            b3.configure(text = "O")
            turn = 1
        Lbl.configure(text = "player"+ str(turn) + "turn")
        win()


def b4click ():
    global turn
    mytext = b4.cget("text")
    if mytext==" ":
        if turn == 1:
            b4.configure(text = "X")
            turn = 2
        else:
            b4.configure(text = "O")
            turn = 1
        Lbl.configure(text = "player"+ str(turn) + "turn")
        win()


def b5click ():
    global turn
    mytext = b5.cget("text")
    if mytext==" ":
        if turn == 1:
            b5.configure(text = "X")
            turn = 2
        else:
            b5.configure(text = "O")
            turn = 1
        Lbl.configure(text = "player"+ str(turn) + "turn")
        win()


def b6click ():
    global turn
    mytext = b6.cget("text")
    if mytext==" ":
        if turn == 1:
            b6.configure(text = "X")
            turn = 2
        else:
            b6.configure(text = "O")
            turn = 1
        Lbl.configure(text = "player"+ str(turn) + "turn")
        win()


def b7click ():
    global turn
    mytext = b7.cget("text")
    if mytext==" ":
        if turn == 1:
            b7.configure(text = "X")
            turn = 2
        else:
            b7.configure(text = "O")
            turn = 1
        Lbl.configure(text = "player"+ str(turn) + "turn")
        win()


def b8click ():
    global turn
    mytext = b8.cget("text")
    if mytext==" ":
        if turn == 1:
            b8.configure(text = "X")
            turn = 2
        else:
            b8.configure(text = "O")
            turn = 1
        Lbl.configure(text = "player"+ str(turn) + "turn")
        win()


def b9click ():
    global turn
    mytext = b9.cget("text")
    if mytext==" ":
        if turn == 1:
            b9.configure(text = "X")
            turn = 2
        else:
            b9.configure(text = "O")
            turn = 1
        Lbl.configure(text = "player"+ str(turn) + "turn")
        win()


btn_colour = "lightgreen"  

b1 = Button(window, text=" ", width=5, bg=btn_colour, command=b1click)
b1.grid(row=0, column=0, padx=5, pady=5)

b2 = Button(window, text=" ", width=5, bg=btn_colour, command=b2click)
b2.grid(row=0, column=1, padx=5, pady=5)

b3 = Button(window, text=" ", width=5, bg=btn_colour, command=b3click)
b3.grid(row=0, column=2, padx=5, pady=5)

b4 = Button(window, text=" ", width=5, bg=btn_colour, command=b4click)
b4.grid(row=1, column=0, padx=5, pady=5)

b5 = Button(window, text=" ", width=5, bg=btn_colour, command=b5click)
b5.grid(row=1, column=1, padx=5, pady=5)

b6 = Button(window, text=" ", width=5, bg=btn_colour, command=b6click)
b6.grid(row=1, column=2, padx=5, pady=5)

b7 = Button(window, text=" ", width=5, bg=btn_colour, command=b7click)
b7.grid(row=2, column=0, padx=5, pady=5)

b8 = Button(window, text=" ", width=5, bg=btn_colour, command=b8click)
b8.grid(row=2, column=1, padx=5, pady=5)

b9 = Button(window, text=" ", width=5, bg=btn_colour, command=b9click)
b9.grid(row=2, column=2, padx=5, pady=5)


Lbl = Label(window, text='Player ' + str(turn) + ' Turn', bg="lightblue", fg="black")
Lbl.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()
