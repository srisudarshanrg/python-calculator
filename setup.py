from cx_Freeze import setup, Executable

setup(
    name="Calculator",
    version="1.0",
    description="This is a simple calculator built using python library customtkinter. It performs all the basic functions.",
    executables=[Executable("calculator.py")]
)