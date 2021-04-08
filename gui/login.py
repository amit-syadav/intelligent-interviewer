import tkinter as tk
from tkinter import ttk

import startPage
import greeting

LARGEFONT =("Verdana", 35)

# second window frame page1
class Login(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Login page", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

                
        # this wil create a label widget
        l1 = ttk.Label(self, text = "Email Id:")
        l2 = ttk.Label(self, text = "Password:")
        
        # grid method to arrange labels in respective
        # rows and columns as specified
        l1.grid(row = 1, column = 0, sticky = "W", pady = 2)
        l2.grid(row = 2, column = 0, sticky = "W", pady = 2)
        
        # entry widgets, used to take entry from user
        e1 = ttk.Entry(self)
        e2 = ttk.Entry(self)
        
        # this will arrange entry widgets
        e1.grid(row = 1, column = 1, pady = 2)
        e2.grid(row = 2, column = 1, pady = 2)
        

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(startPage.StartPage))
    
        # putting the button in its place
        # by using grid
        button1.grid(row = 3, column = 1, padx = 10, pady = 10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Greeting page",
                            command = lambda : controller.show_frame(greeting.Greeting))
    
        # putting the button in its place by
        # using grid
        button2.grid(row = 4, column = 1, padx = 10, pady = 10)



