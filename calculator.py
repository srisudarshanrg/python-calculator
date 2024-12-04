import customtkinter as c
import calculator_functions as cf
import keyboard as key

c.set_appearance_mode("dark")
c.set_default_color_theme("blue")

app = c.CTk()
app.title("RaptorCalc")
app.geometry("475x572")

# Entry for entering values needed for expression
expression_entry = c.CTkEntry(master=app, placeholder_text="Enter a mathematical expression", width=465, height=80, font=("Arial", 30))
expression_entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# button widgets
# digits
one = c.CTkButton(master=app, text="1", font=("Arial", 20), height=72, width=112, command=lambda: cf.EnterValues(1, expression_entry))
two = c.CTkButton(master=app, text="2", font=("Arial", 20), height=72, width=112, command=lambda: cf.EnterValues(2, expression_entry))
three = c.CTkButton(master=app, text="3", font=("Arial", 20), height=72, width=112, command=lambda: cf.EnterValues(3, expression_entry))
four = c.CTkButton(master=app, text="4", font=("Arial", 20), height=72, width=112, command=lambda: cf.EnterValues(4, expression_entry))
five = c.CTkButton(master=app, text="5", font=("Arial", 20), height=72, width=112, command=lambda: cf.EnterValues(5, expression_entry))
six = c.CTkButton(master=app, text="6", font=("Arial", 20), height=72, width=112, command=lambda: cf.EnterValues(6, expression_entry))
seven = c.CTkButton(master=app, text="7", font=("Arial", 20), height=72, width=112, command=lambda: cf.EnterValues(7, expression_entry))
eight = c.CTkButton(master=app, text="8", font=("Arial", 20), height=72, width=112, command=lambda: cf.EnterValues(8, expression_entry))
nine = c.CTkButton(master=app, text="9", font=("Arial", 20), height=72, width=112, command=lambda: cf.EnterValues(9, expression_entry))
zero = c.CTkButton(master=app, text="0", font=("Arial", 20), height=72, width=112, command=lambda: cf.EnterValues(0, expression_entry))

# positioning digits
one.grid(row=1, column=0, padx=2, pady=3)
two.grid(row=1, column=1, padx=2, pady=3)
three.grid(row=1, column=2, padx=2, pady=3)
four.grid(row=2, column=0, padx=2, pady=3)
five.grid(row=2, column=1, padx=2, pady=3)
six.grid(row=2, column=2, padx=2, pady=3)
seven.grid(row=3, column=0, padx=2, pady=3)
eight.grid(row=3, column=1, padx=2, pady=3)
nine.grid(row=3, column=2, padx=2, pady=3)
zero.grid(row=4, column=1, padx=2, pady=3)

# operators
plus = c.CTkButton(master=app, text="+", font=("Helvetica", 20), height=72, width=112, command=lambda: cf.EnterValues("+", expression_entry))
subtract = c.CTkButton(master=app, text="-", font=("Helvetica", 20), height=72, width=112, command=lambda: cf.EnterValues("-", expression_entry))
multiply = c.CTkButton(master=app, text="×", font=("Helvetica", 20), height=72, width=112, command=lambda: cf.EnterValues("*", expression_entry))
divide = c.CTkButton(master=app, text="÷", font=("Helvetica", 20), height=78, width=112, command=lambda: cf.EnterValues("/", expression_entry))
equal= c.CTkButton(master=app, text="=", font=("Helvetica", 20), height=72, width=112, command=lambda: cf.EvaluateValues(expression_entry))
key.on_press_key('enter', lambda x: cf.EvaluateValues(expression_entry))
square = c.CTkButton(master=app, text="x²", font=("Helvetica", 20), height=72, width=112, command=lambda: cf.Square(expression_entry))
sqrt = c.CTkButton(master=app, text="√", font=("Helvetica", 20), height=72, width=112, command=lambda: cf.SquareRoot(expression_entry))
backspace = c.CTkButton(master=app, text="🔙", font=("Helvetica", 40), height=72, width=112, command=lambda: cf.Backspace(expression_entry))

# position operators
plus.grid(row=1, column=3, padx=2, pady=3)
subtract.grid(row=2, column=3, padx=2, pady=3)
multiply.grid(row=3, column=3, padx=2, pady=3)
divide.grid(row=4, column=3, padx=2, pady=3)
equal.grid(row=5, column=3, padx=2)
backspace.grid(row=6, column=3, padx=2)
square.grid(row=5, column=0 ,padx=2)
sqrt.grid(row=5, column=1, padx=2)

# features
clear = c.CTkButton(master=app, text="Clear", font=("Helvetica", 20), height=72, width=112, command=lambda: cf.ClearValues(expression_entry))
exit_app = c.CTkButton(master=app, text="Exit", font=("Helvetica", 20), height=72, width=346, command=lambda: cf.ExitApp(app))
copy = c.CTkButton(master=app, text="Copy", font=("Helvetica", 20), height=72, width=112, command=lambda: cf.Copy(expression_entry))
paste = c.CTkButton(master=app, text="Paste", font=("Helvetica", 20), height=72, width=112, command=lambda: cf.Paste(expression_entry))

# positioning features
clear.grid(row=5, column=2, padx=2, pady=3)
exit_app.grid(row=6, column=0, columnspan=3, padx=2, pady=3)
copy.grid(row=4, column=0, padx=2, pady=3)
paste.grid(row=4, column=2, padx=2, pady=3)

app.mainloop()