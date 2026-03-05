
import tkinter as tk
from tkinter import messagebox
import random



class EvenOddGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Even or Odd")
        self.root.geometry("420x220")
        self.root.resizable(False, False)

        self.num = random.randint(1, 100)

        
        self.label = tk.Label(
            root,
            text="I have picked a number. Is it Even or Odd?",
            font=("Arial", 12)
        )
        self.label.place(x=30, y=30)

       
        self.even_btn = tk.Button(
            root,
            text="Even",
            width=12,
            font=("Arial", 11),
            command=lambda: self.check_answer("Even")
        )
        self.even_btn.place(x=90, y=90)

        self.odd_btn = tk.Button(
            root,
            text="Odd",
            width=12,
            font=("Arial", 11),
            command=lambda: self.check_answer("Odd")
        )
        self.odd_btn.place(x=230, y=90)

        
        self.play_again_btn = None

    def check_answer(self, guess):
      
        if guess == "Even" and self.num % 2 == 0:
            messagebox.showinfo("Result", f"You win! The number was {self.num} (Even).")
        elif guess == "Odd" and self.num % 2 != 0:
            messagebox.showinfo("Result", f"You win! The number was {self.num} (Odd).")
        else:
            kind = "Even" if self.num % 2 == 0 else "Odd"
            messagebox.showinfo("Result", f"Sorry, you lose! The number was {self.num} ({kind}).")

       
        self.even_btn.config(state="disabled")
        self.odd_btn.config(state="disabled")

      
        if self.play_again_btn is None:
            self.play_again_btn = tk.Button(
                self.root,
                text="Play Again",
                width=12,
                font=("Arial", 11),
                command=self.play_again
            )
            self.play_again_btn.place(x=155, y=150)

    def play_again(self):
        self.num = random.randint(1, 100)
        self.even_btn.config(state="normal")
        self.odd_btn.config(state="normal")
        self.play_again_btn.destroy()
        self.play_again_btn = None



if __name__ == "__main__":
    root = tk.Tk()
    app = EvenOddGame(root)
    root.mainloop()
