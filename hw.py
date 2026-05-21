
import tkinter as tk
from gtts import gTTS
from playsound import playsound
import os




def speak(text, lang):
    filename = "voice.mp3"

    tts = gTTS(text=text, lang=lang)
    tts.save(filename)

    playsound(filename)

    os.remove(filename) 


def speak_yes():
    speak("Sí", "es")   

def speak_no():
    speak("Non", "fr")  

def speak_hello():
    speak("Hallo", "de")  

def speak_bye():
    speak("さようなら", "ja")  


root = tk.Tk()
root.title("Soundboard")
root.geometry("300x250")

for i in range(2):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)


btn1 = tk.Button(root, text="YES", font=("Arial", 16), command=speak_yes)
btn2 = tk.Button(root, text="NO", font=("Arial", 16), command=speak_no)
btn3 = tk.Button(root, text="HELLO", font=("Arial", 16), command=speak_hello)
btn4 = tk.Button(root, text="BYE", font=("Arial", 16), command=speak_bye)

btn1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
btn2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
btn3.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
btn4.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")


root.mainloop()

