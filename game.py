import tkinter
from tkinter import *
import random
from tkinter import messagebox
root = tkinter.Tk()

words = {
    "plpea": "apple",
    "gnoma": "mango",
    "annaba": "banana",
    "hveeica": "achieve",
    "lkaatko": "kolkata",
    "egvnine": "evening",
    "aestnrv": "servant",
    "iceever": "receiver",
    "lndono": "london",
    "rrreifa": "ferrari",
    "wllhoo": "hollow",
    "oohrr": "horror",
    "rtemsa": "master",
    "nnrgimo": "morning",
    "ltbtoe": "bottle",
    "enp": "pen",
    "ourrte": "router",
    "ypco": "copy",
    "rraonw": "narrow",
    "wdie": "wide",
    "ievd": "dive",
    "elov": "love",
    "klboc": "block",
    "ightr": "right",
    "plmsie": "simple",
    "dfea": "deaf",
    "glneis": "single",
    "ghtkni": "knight",
    "opeh": "hope",
}

question_words = list(words.keys())
question = random.choice(question_words)
c= 0
d = 0
s = ""

l = Label(root)

def reset():
    global question
    label.config(text = question)
    e1.delete(0,END)

def default():
    global question
    label.config(text = question)
    def checkans():
        global question,c,d,s,l
        d = d+1
        var =e1.get()
        var = var.lower()
        if var == words[question]:
            messagebox.showinfo("congratulations","it's the correct answer .")
            s = "score:"+ str(c)+"/"+str(d)
            l.forget()
            l = Label(root,font=("verdana",20),text = s,bg = "#000000",fg = "#fff")
            l.pack(side = LEFT)
            reset()