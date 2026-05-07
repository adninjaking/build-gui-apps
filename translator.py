from tkinter import *
from gtts import gTTS
from deep_translator import GoogleTranslator
import os
root = Tk()
entry = Entry(root,width = 40,font =14)
entry.pack(pady = 20)
def speak():
    text =entry.get()
    outputtext = GoogleTranslator(source="en",target = "en").translate(text)
    reverse_text = outputtext[::-1]
    print("reversed:",reverse_text)
    speech = gTTS(text = reverse_text,lang = "en")
    speech.save("output.mp3")
    os.system("output.mp3")
btn = Button(root,text = "speak backwards",command = speak)
btn.pack(pady = 20)
root.mainloop()
