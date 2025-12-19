import os
from style import style, Ansi

def clear():
    os.system('cls||clear')

def get_input(text, color=Ansi.FG_CYAN):
    return input(style(text + " ", color=color))