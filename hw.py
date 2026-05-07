
from tkinter import *
from gtts import gTTS
import os


window = Tk()
window.title("Slow Mo Voice")
window.geometry("650x550+350+200")


frame1 = Frame(window, bg="light pink", height=150)
frame1.pack(fill=X)

frame2 = Frame(window, bg="light green", height=750)
frame2.pack(fill=X)

label = Label(
    frame1,
    text="Slow Motion Speaker",
    font="bold,30",
    bg="light pink"
)
label.place(x=170, y=70)


entry = Entry(frame2, width=45, bd=4, font=14)
entry.place(x=50, y=52)


def play():
    text = entry.get()
    if text.strip() == "":
        return

    language = "en"
    myobj = gTTS(
        text=text,
        lang=language,
        slow=True,      
        tld="co.uk"
    )

    filename = "slow_voice.mp3"
    myobj.save(filename)
    os.startfile(filename) 


btn = Button(
    frame2,
    text="Speak Slowly",
    width=15,
    pady=10,
    font="bold,15",
    command=play,
    bg="yellow"
)
btn.place(x=250, y=130)

window.mainloop()
