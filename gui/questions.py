import tkinter as tk
from tkinter import ttk
import json
import os
import time

LARGEFONT =("Verdana", 15)


class Questions(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)

        label_heading = ttk.Label(self, text ="Questions", font = LARGEFONT)
        label_heading.grid(row = 0, column = 4, padx = 10, pady = 10)

        label_instruction = ttk.Label(self, text ="You  Will Be Proctored For Reading- Don'T Perform Any Suspicious Activity", font = LARGEFONT)
        label_instruction.grid(row = 1, column = 4, padx = 10, pady = 10)


        # get questions from json file
        # run loop for each question
        # update timer for each question

        # locating question file 
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)
        file_dir = os.path.join(dir_path,'resources')
        file_path = os.path.join(file_dir,"questions_testing.json")
        print(file_path)

        # loading question json file to python dictionary
        questions = open(file_path, 'r')
        question_dict = json.load(questions)
        # print(q,type(q))

        question_frame = tk.Frame(self, borderwidth = 10, bg="red")
        question_frame.grid(row = 3, column = 1)

        txt  = tk.StringVar()
        # timer  = tk.StringVar()

        # timer.set("100")

        label_question = ttk.Label(self, text="hii", font = LARGEFONT)
        label_question.grid(row = 2, column = 4, padx = 10, pady = 10)
        # txt.set("initial")

        # label_timer = ttk.Label(self, textvariable=timer, font = LARGEFONT)
        # label_timer.grid(row = 2, column = 5, padx = 10, pady = 10)

        # def update_question():
        #     txt.set("hi deer")
        #     # time.set("best time hai")

        # question_frame.after(2000, update_question)

            





        
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))
        button1.grid(row = 50, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Page 2",
                            command = lambda : controller.show_frame(Page2))
        button2.grid(row = 60, column = 1, padx = 10, pady = 10)



import helper.checker as chk
app =chk.Checker(Questions)
app.mainloop()