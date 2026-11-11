#Math quiz
from tkinter import *
import tkinter.messagebox
import random

#Setup
root = Tk()
root.title("Math Quiz")

#Products - Label
product_title = Label(root, text = "Products", fg = "black")
product_title.pack(pady = 10)

#Num1 and Num2 - Variables
num1 = random.randint(1, 10)
num2 = random.ramdint(1, 10)

#Num1 - Label
num1_label = Label(root, text = "Factor #1: "+str(num1), fg = "red")
num1_label.pack(padx = 10)

#Num2 - Label
num2_label = Label(root, text = "Factor #2: "+str(num2), fg = "red")
num2_label.pack(padx = 10)

#Product - Function
def product_calc():
    product = num1 * num2

#Answer Check - Button
check = Button(root, text = "Check Answer", command = product_calc)
check.pack(pady = 10)