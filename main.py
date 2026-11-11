#Number Guessing Game
from tkinter import *
import tkinter.messagebox
import random

#Set up
root = Tk()
root.geometry("500x300")
root.title("Number Guessing Game")

#Opening - Label
opening = Label(root, text = "Welcome to the Number Guessing Game!", fg = "blue", font = ("Helvetica", 12, "normal"))
opening.grid(row = 0, column = 1, pady = 10)

#Name - Label
name_label = Label(root, text = "What is your name ?", fg = "purple", font = ("Helvetica", 12, "normal"))
name_label.grid(row = 1, column = 0, padx = 20, pady = 10)

#Name - Entry
name_entry = Entry(root)
name_entry.grid(row = 2, column = 0, padx = 20)

#Name Display - Function
def name_display():
    name = name_entry.get()
    tkinter.messagebox.showinfo("Greeting", "Well, "+name+", I am thinking of a number from 1 to 20")

#Nums - List
num = random.randint(1, 20)

#Guess Num - Function
def guess_num():
    num_guess = int(num_entry.get())
    if num_guess == num:
        tkinter.messagebox.showinfo("Correct", "Congratulations ! The number was indeed "+str(num))
    elif num_guess < num:
        tkinter.messagebox.showinfo("Too Low", "Your number is too low... Try guessing higher.")
    elif num_guess > num:
        tkinter.messagebox.showinfo("Too High", "Your number is too high... Try guessing lower.")
    else:
        tkinter.messagebox.showerror("Error", "Input Invalid !")

#OK - Button
ok_btn = Button(root, text = "OK", bg = "pink", command = name_display)
ok_btn.grid(row = 2, column = 1, pady = 30)

#Num - Label
num_label = Label(root, text = "Guess a number : ", fg = "purple", font = ("Helvetica", 12, "normal"))
num_label.grid(row = 3, column = 0, padx = 20, pady = 30)

#Num - Entry
num_entry = Entry(root)
num_entry.grid(row = 4, column = 0, padx = 20, pady = 10)

#Guess - Button
guess_btn = Button(root, text = "Guess", bg = "pink", command = guess_num)
guess_btn.grid(row = 4, column = 1, pady = 10)

root.mainloop()