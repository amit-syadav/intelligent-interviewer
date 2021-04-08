import tkinter as tk
from tkinter import ttk

import startPage
import login
import greeting


LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
    
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # self is like window - dont ask how

        #getting screen width and height of display
        width= self.winfo_screenwidth() 
        height= self.winfo_screenheight()
        #setting tkinter window size to full screen
        self.geometry("%dx%d" % (width, height))
        # self.geometry
        
        # creating a container
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (startPage.StartPage,login.Login, greeting.Greeting):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(startPage.StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# first window frame startpage

        
# Driver Code
app = tkinterApp()
app.mainloop()
