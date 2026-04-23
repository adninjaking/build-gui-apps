
from tkinter import *
from gtts import gTTS
import os
import time

window = Tk()


frame1 = Frame(window, bg="light pink", height="150")
frame1.pack(fill=X)

frame2 = Frame(window, bg="light green", height="750")
frame2.pack(fill=X)


label = Label(frame1, text="Soundboard", font="bold,30", bg="light pink")
label.place(x=220, y=70)

def speak(word):
    language = "en"

    
    filename = f"{word}_{int(time.time() * 1000)}.mp3"

    myobj = gTTS(text=word, lang=language, slow=False, tld="co.uk")
    myobj.save(filename)

    os.startfile(filename)
    time.sleep(2)

    try:
        os.remove(filename)
    except:
        pass

btn1 = Button(frame2, text="YES", width="15", pady=10, font="bold,15",
              command=lambda: speak("Yes"), bg="yellow")
btn1.place(x=120, y=80)

btn2 = Button(frame2, text="NO", width="15", pady=10, font="bold,15",
              command=lambda: speak("No"), bg="yellow")
btn2.place(x=340, y=80)

btn3 = Button(frame2, text="HELLO", width="15", pady=10, font="bold,15",
              command=lambda: speak("Hello"), bg="yellow")
btn3.place(x=120, y=170)

btn4 = Button(frame2, text="BYE", width="15", pady=10, font="bold,15",
              command=lambda: speak("Bye"), bg="yellow")
btn4.place(x=340, y=170)



window.title("Soundboard")
window.geometry("650x550+350+200")
window.mainloop()

