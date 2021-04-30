import tkinter as tk
from tkinter import ttk

# import gui.startPage
# import gui.questions

from gui import startPage
from gui import questions
LARGEFONT = ("Verdana", 25)

# second window frame page1


class Greeting(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Welcome", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        welcome_speech = """
        I am 'robo', your AI interviewer
        I will ask you questions and you will have 15secs to read each question
        After which you will have to answer in given stipulated time
        I will judge you on the basis of soft skills and hard skills
        You will get your report on your mail
        BEST OF LUCK
        """
        label = ttk.Label(self, text=welcome_speech, font=LARGEFONT)
        label.grid(row=1, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="StartPage",
                             command=lambda: controller.show_frame(startPage.StartPage))

        # putting the button in its place
        # by using grid
        button1.grid(row=2, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Questions",
                             command=lambda: controller.show_frame(questions.Questions))

        # putting the button in its place
        # by using grid
        button2.grid(row=2, column=1, padx=10, pady=10)

# import helper.checker as chk
# app =chk.Checker(Greeting)
# app.mainloop()
