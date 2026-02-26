import tkinter
import tkinter.messagebox
import random


root = tkinter.Tk()
root.title("guess the number")

root.minsize(350,260)
number = random.randint(1,20)

def send_low ():
    tkinter.messagebox.showinfo("messagebox","your gess is too low!")

def check_num ():
    guess = text_guess.get()
    guess = int(guess)
    if guess > number:
        tkinter.messagebox.showinfo("high","your guess is too high!")
    if guess < number:
        tkinter.messagebox.showinfo("low","your guess is too low!")
    if guess == number:
        tkinter.messagebox.showinfo("correct","your guess is correct!")

def btn_confirm():
    myname = text_name.get()
    tkinter.messagebox.showinfo(
        "name",
        "well"+ myname + ",i am thinking of a number between 1 and 20"
    )

 
label = tkinter.Label(root,text = "welcome to our game")
label.pack()
label_name = tkinter.Label(root,text = "what's your name?")
label_name.place(x = 10,y= 60)
text_name = tkinter.Entry(root,width=20)
text_name.place(x=10,y=90)
btnok = tkinter.Button(root,text = "OK",command = btn_confirm)
btnok.place(x = 200,y=90,height=28)

label_guess=tkinter.Label(root,text ="take a guess :")
label_guess.place(x =10,y=150)
text_guess = tkinter.Entry(root,width=10)
text_guess.place(x = 90,y = 150)
btncheck = tkinter.Button(root,text = "guess",command = check_num)
btncheck.place(x = 200, y= 150,width=45,height=28)
root.mainloop()

    
    
