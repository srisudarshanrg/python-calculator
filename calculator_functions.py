import customtkinter as c
import tkinter as t
import pyperclip as pc
from plyer import notification
import math

# Functions for the calculator

# EnterValues enters the values into the entry widget when a button is clicked
def EnterValues(val, entry_widget: c.CTkEntry):
    expression = str(entry_widget.get())
    new_char = str(val)
    new_expression = expression + new_char
    entry_widget.delete(0, t.END)
    entry_widget.insert(0, new_expression)

# EvaluateValues performs the operation entered in the entry box
def EvaluateValues(entry_widget: c.CTkEntry):
    try:
        solution = eval(str(entry_widget.get()))
        entry_widget.delete(0, t.END)
        entry_widget.insert(0, solution)
    except Exception:
        notification.notify(
            title="Invalid Expression",
            message="Enter a valid mathematical expression.",
            timeout=3
        )
        return           
        
# ClearValues clears the entry box
def ClearValues(entry_widget: c.CTkEntry):
    entry_widget.delete(0, t.END)

# ExitApp closes the application
def ExitApp(app: c.CTk):
    app.destroy()

# Square squares the expression entered in the entry box
def Square(entry_widget: c.CTkEntry):
    try:
        expression = str(entry_widget.get())
        solution = int(eval(expression))
    except Exception:
        notification.notify(
            title="Invalid Expression",
            message="Enter a valid mathematical expression to square.",
            timeout=3
        )
        return

    squared = int(solution ** 2)
    entry_widget.delete(0, t.END)
    entry_widget.insert(0, squared)

# SquareRoot calculates the square root of the expression in the entry box
def SquareRoot(entry_widget: c.CTkEntry):
    try:
        expression = str(entry_widget.get())
        solution = int(eval(expression))
    except Exception:
        notification.notify(
            title="Invalid Expression",
            message="Enter a valid mathematical expression to square root.",
            timeout=3
        )
        return

    sqrt =  math.sqrt(solution)
    sqrt_real = round(sqrt)
    entry_widget.delete(0, t.END)
    entry_widget.insert(0, sqrt_real)

# Copy copies the expression in the entry box
def Copy(entry_widget: c.CTkEntry):
    pc.copy(str(entry_widget.get()))
    notification.notify(
        title="Copy",
        message="Expression copied to clipboard.",
        timeout=3
    )

# Backspace deletes the previous character in the entry
def Backspace(entry_widget: c.CTkEntry):
    expression_list = []
    for i in entry_widget.get():
        expression_list.append(i)

    start_char = len(expression_list) - 1
    end_char = len(expression_list)
    
    entry_widget.delete(start_char, end_char)

# Paste pastes whatever is in the clipboard into the entry box
def Paste(entry_widget: c.CTkEntry):
    char = pc.paste()
    entry_widget.insert(t.END, char)