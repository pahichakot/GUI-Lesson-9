#Even or Odd Number Guessing Game
from tkinter import *
import tkinter.messagebox
import random

#Set up
root = Tk()
root.geometry("500x300")
root.title("Even or Odd Number Guessing Game")

#Opening - Label
opening = Label(root, text = "I have picked a number. Is it Even or Odd?", fg = "blue", font = ("Helvetica", 12, "normal"))
opening.grid(row = 0, column = 1, pady = 10)

#Nums - List
num = random.randint(1, 100)

#Guess Num - Function
def check_num(user_guess):
    if num % 2 == 0 and user_guess == "Even":
        tkinter.messagebox.showinfo("Correct!", "You guessed correctly!")
    elif num % 2 != 0 and user_guess == "Odd":
        tkinter.messagebox.showinfo("Correct!", "You guessed correctly!")
    else:
        tkinter.messagebox.showinfo("Incorrect!", "Better luck next time!")

#Even - Button
even_btn = Button(root, text = "Even", bg = "pink", command = lambda: check_num("Even"))
even_btn.grid(row = 1, column = 0, pady = 30, padx = 20)

#Odd - Button
odd_btn = Button(root, text = "Odd", bg = "pink", command = lambda: check_num("Odd"))
odd_btn.grid(row = 1, column = 2, pady = 30)

root.mainloop()