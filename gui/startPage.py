import tkinter as tk
from tkinter import ttk

import greeting
import login

LARGEFONT =("Verdana", 65)


# todo
# its like the banner page of our app
# add images

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # label of frame Layout 2
        label = ttk.Label(self, text ="Intelligent Interviewer System", font = LARGEFONT)
        
        # putting the grid in its place by using
        # grid 
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        button1 = ttk.Button(self, text ="Login page",
        command = lambda : controller.show_frame(login.Login))
    
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)



