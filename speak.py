from tkinter import *
import speech_recognition as sr
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile
window = Tk()
window.title("speech to text")
window.geometry("1000x400")

heading1 = Label(window,text="voice Notepad",font = ("arial",30,"bold"))
heading1.grid(row = 0 , column = 1, padx = 20,pady = 20)

output_text = Text(window,height=6,width = 40,font = ("arial",12))
output_text.grid(row = 1 , column = 1, padx = 20,pady = 20)

def Translate():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak anything...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)

        except:
            text = "sorry could not recognize your voice"
    output_text.delete(1.0,END)
    output_text.insert(END,text)

def save():
    fout =asksaveasfile(defaultextension=".txt")
    if fout :
        fout.write(output_text.get(1.0,END))
        fout.close()
        messagebox.showinfo("saved","File saved succesfully !")
    else :
        messagebox.showinfo("warning","text not saved")
trans_btn = Button(
    window,
    text = "click me ! Start Recording",
    font=("arial",15,"bold"),
    command = Translate,
    width = 20,
    bg="#4CAF50",
    fg = "white"
)
trans_btn.grid(row = 1,column = 0 ,pady = 20,padx = 20)

save_btn = Button(
    window,
    text = "save the text",
    font=("arial",12,"bold"),
    command = save,
    height = 4,
    width = 20,
    bg="#2196F3",
    fg = "white"
)
save_btn.grid(row = 1,column = 2,pady =10)
window.mainloop()