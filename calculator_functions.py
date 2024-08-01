import customtkinter as c
import tkinter as t
import pyperclip as pc
from plyer import notification

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
        
# ClearValues clears the entry box
def ClearValues(entry_widget: c.CTkEntry):
    entry_widget.delete(0, t.END)

# ExitApp closes the application
def ExitApp(app: c.CTk):
    app.destroy()

# Square squares the number entered in the entry box
def Square(entry_widget: c.CTkEntry):
    try:
        number = int(entry_widget.get())
    except TypeError:
        notification.notify(
            title="Invalid Expression",
            message="Enter a valid mathematical expression to square.",
            timeout=3
        )  

    solution = number ** 2
    entry_widget.delete(0, t.END)
    entry_widget.insert(0, solution)

# Copy copies the expression in the entry box
def Copy(entry_widget: c.CTkEntry):
    pc.copy(str(entry_widget.get()))

# Paste pastes whatever is in the clipboard into the entry box
def Paste(entry_widget: c.CTkEntry):
    char = pc.paste()
    entry_widget.insert(t.END, char)