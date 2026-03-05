import tkinter
import tkinter.messagebox#
import random

root = tkinter.Tk()
root.minsize(350,250)
root.title("math quiz")
num1 = random.randint(1,20)
num2 = random.randint(1,20)
answer = num1 * num2

def start_game():
    tkinter.messagebox.showinfo(
        "math whiz",
        "guess the product of"+str(num1)+"and"+str(num2)+"!"
    )


def check_answer():
    user_input = entry_answer.get()
    user_input = int(user_input)
    if user_input == answer:
        tkinter.messagebox.showinfo("correct","correct you are a math whiz !")
    else:
        tkinter.messagebox.showerror("wrong","wrong the awnser was"+str(answer))

def refresh_game():
    global num1,num2,answer
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)
    answer = num1 * num2
    entry_answer.delete(0,tkinter.END)
    tkinter.messagebox.showinfo(
        "new question",
        "guess the product of "+str(num1)+"and "+str(num2)+"!"
    )

    


label_title = tkinter.Label(root,text = "welcome to math whiz!",font=("arial",14))
label_title.pack(pady = 10)
btn_start = tkinter.Button(root,text="start game!",command = start_game)
btn_start.pack(pady = 5)
label_question = tkinter.Label(root,text = "enter your answer:")
label_question.pack()
entry_answer = tkinter.Entry(root,width = 15)
entry_answer.pack(pady = 5)
btn_check = tkinter.Button(root,text = "submit answer",command=check_answer)
btn_check.pack(pady = 10)
btn_refresh = tkinter.Button(root,text = "refresh",command=refresh_game)
btn_refresh.pack(pady = 5)
root.mainloop()


