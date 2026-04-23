from tkinter import *
from gtts import gTTS 
import os

root = Tk()
frame1 = Frame(root,bg="light pink",height = 150)
frame1.pack(fill = X)

frame2 = Frame(root,bg="light green",height = 350)
frame2.pack(fill = X)

label = Label(frame1,text = "click the button to hear a greeting",font = ("arial",20,"bold"),bg = "light pink")
label.place(x= 120,y = 60)
def play ():
    text = "good morning , have a nice day "
    language = "en"
    myobj = gTTS(text = text,lang = language,slow = False)
    myobj.save("greeting.wav")
    os.system("greeting.wav")
btn  =Button(frame2,text = "say goodmorning",width = 20,pady = 10,font = ("arial",15,"bold"),bg = "yellow",command = play)
btn.place(x = 220,y = 120)
root.title("greeter")
root.geometry("650x400+350+200")
root.mainloop()