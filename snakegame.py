'''
    Author: Karan Patel
    Snake Game
'''

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


'''
Things to do:
    Collisions
    GUI - boxes, window, etc.
    Set up tkinter window loop
    Add difficulty/increasing difficulty
Extra:
    An account system
    Database to store login information (per user)
    Each login will save high score
'''

def main(): # the game will go here
    root = tk.Tk()
    
    test = ttk.Button(root, text='test 1', bootstyle = SUCCESS)
    test.pack()
    
    root.mainloop()


if __name__ == "__main__": # makes sure that the main() function is not imported 
    main() # the game


