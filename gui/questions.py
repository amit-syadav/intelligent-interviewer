import tkinter as tk
from tkinter import ttk
import json
import os
import time
import threading

from helper.time_manager import run, create_directory, this_student_directory_create


LARGEFONT =("Verdana", 15)
FRAME_BG_COLOR = "#957DAD"
FRAME_BORDER_SIZE = 5

class Questions(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)

        self.create_student_folder()

        label_heading = ttk.Label(self, text ="Questions", font = LARGEFONT)
        label_heading.grid(row = 0, column = 0, padx = 10, pady = 10)

        label_instruction = tk.Label(self, text ="You  Will Be Proctored For Reading- Don'T Perform Any Suspicious Activity", font = LARGEFONT)
        label_instruction.grid(row = 1, column = 0, padx = 10, pady = 10)

        # get questions from json file
        questions = open(self.get_file_path(), 'r')
        self.question_dict = json.load(questions)

        self.question_read_time = 5

        # storing each frame on a list
        self.question_list = []

        for q_id in self.question_dict:
            question_frame = tk.Frame(self, bg=FRAME_BG_COLOR,border=FRAME_BORDER_SIZE, highlightcolor="blue")
            question_frame.grid(row = 2, column = 0)

            label_question = tk.Label(question_frame, text =self.question_dict[q_id]["text"], font = LARGEFONT)
            label_question.grid(row = 0, column = 0, padx = 10, pady = 10)

            label_timer = tk.Label(question_frame, text = "Time allocated:\t"+str(self.question_dict[q_id]["time"])+"secs", font = LARGEFONT)
            label_timer.grid(row = 1, column = 0, padx = 10, pady = 10)

            self.question_list.append(question_frame)
        
        print("question list is", self.question_list)
        self.current_question_number = 0


        # first frame
        self.first_question_frame = tk.Frame(self, bg=FRAME_BG_COLOR ,border=FRAME_BORDER_SIZE, highlightcolor="blue")
        self.first_question_frame.grid(row = 2, column = 0)

        first_label_question = tk.Label(self.first_question_frame, text ="Click on the next button when you are ready for", font = LARGEFONT)
        first_label_question.grid(row = 0, column = 0, padx = 10, pady = 10)



# last frame
        self.last_question_frame = tk.Frame(self, bg=FRAME_BG_COLOR ,border=FRAME_BORDER_SIZE, highlightcolor="blue")
        self.last_question_frame.grid(row = 2, column = 0)

        last_label_question = tk.Label(self.last_question_frame, text ="All questions done", font = LARGEFONT)
        last_label_question.grid(row = 0, column = 0, padx = 10, pady = 10)

# initially show the first question
        self.first_question_frame.tkraise()


        



        # run loop for each question
        # save_and_show timer for each question




        buttonNext = ttk.Button(self, text ="Next Question",
                            command = self.next_question )
    
        # putting the button in its place
        # by using grid
        buttonNext.grid(row = 3, column = 0, padx = 10, pady = 10)


    def next_question(self):
        print("current question number is", self.current_question_number)

        if self.current_question_number == len(self.question_dict): #all questions done, show the end screen
            self.last_question_frame.tkraise()
            return

        def update_question_on_screen():
            self.question_list[ self.current_question_number ].tkraise()

        question_thread = threading.Thread(target=update_question_on_screen,daemon = True)
        question_thread.start()
        # end question thread by join 
        # question_thread.join()
        # ques
        
        self.current_question_number += 1

        def start_recording():
            run(str(self.current_question_number) +"_reading",self.this_student_folder_directory_path, self.question_read_time )
        
        recording_thread = threading.Thread(target=start_recording, daemon = True)
        recording_thread.start()

          # Makes sure the threads have finished
        print( "active threads in question.py",threading.active_count() )
            # time.sleep(1)
        print("all thread completed")


        # recording_thread.join()




        
    def create_student_folder(self):
        self.student_folder_directory_path = create_directory("keval909") # this part should be in login file after login is successful
        self.this_student_folder_directory_path = this_student_directory_create(self.student_folder_directory_path)
        print("this stud folder directory path", self.this_student_folder_directory_path)

        
            
    # def update_question(self):
    #     # global q_id
    #     # self.q_id  = str( int(self.q_id) + 1)


    #     time_allocated = self.question_dict[self.q_id]["time"]

        

    #     print(self.q_id,self.q_id in self.question_dict)

    #     if self.q_id in self.question_dict: # checking presence in txt file


    #         time.sleep(2)
    #         from helper.time_manager import run


    #         run(self.q_id +"_reading",self.this_student_folder_directory_path, self.question_read_time )
    #         print("question read time complete")
    #         time.sleep(2)
    #         # run(self.q_id +"_answering",self.this_student_folder_directory_path, time_allocated )
    #         print("question answer time complete")
    #         # file_path = self.q_id +"_reading.avi"


    #     else:
    #         variable_question_text.set( "Congratulations, all questions done!" )
    #         variable_time_allocated.set( 0 )

    

    # self.question_frame.after(5000,update_question)
        # self.show_questions()
        # update_question()

    
    # def show_questions(self):
    #     # loading question json file to python dictionary
        
    #     self.question_read_time = 5
    #     self.buffer_time = 3 # extra time for which the frame will be shown even after the question recording is complete
    #     print("questions are",self.question_dict)
    #     self.q_id = "1"
    #     # MAKE SURE ALL ENTRIES IN QUESTION.TXT ARE ORDER WISE STARTING FROM 1
    #     # print(q,type(q))
    #     self.set_question()
    #     self.update_question()
        
    # def set_question(self):
    #     question_text = self.question_dict[self.q_id]["text"]
    #     time_allocated = self.question_dict[self.q_id]["time"]
    #     # print( "print save_and_show question", question_text, time_allocated )
    #     self.label_question["text"] = question_text 
    #     self.label_timer["text"]  = time_allocated 
           


    #         # iterate each ques
    #         # print ques in label
    #         # start its timer
    #         # record
    #         # move to next question after its time




    #         # self.question_frame.after(1000, save_and_show_question)

    def get_file_path(self):
        os.getcwd()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)
        file_dir = os.path.join(dir_path,'resources')
        file_path = os.path.join(file_dir,"questions_testing.json")
        return (file_path)
        


  
    # def __del__(self):
    #     if self.video.isOpened():
    #         self.video.release()
    #         self.out.release()

        



import helper.checker as chk
app =chk.Checker(Questions)
app.mainloop()