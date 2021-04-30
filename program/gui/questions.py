import gui.helper.checker as chk
import tkinter as tk
from tkinter import ttk
import json
import os
import time
import threading
# import mcq_main
from gui.helper.time_manager import run, create_directory, this_student_directory_create
from gui import mcq_main
"""
todo:
add gif of recording when recording in progress
get student directory name from login .py 
video preview window is shown only for the first question, why so?
question frames are getting overlap because of different size -- one solutions is fix the width and height of all question frame
make button of end test RED in color
show stopwatch timer in screen if possible 
"""

LARGEFONT = ("Verdana", 15)
FRAME_BG_COLOR = "#957DAD"
FRAME_BORDER_SIZE = 5


class Questions(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.create_student_folder()

        label_heading = ttk.Label(self, text="Questions", font=LARGEFONT)
        label_heading.grid(row=0, column=0, padx=10, pady=10)

        label_instruction = tk.Label(
            self, text="You  Will Be Proctored For Reading- Don'T Perform Any Suspicious Activity", font=LARGEFONT)
        label_instruction.grid(row=1, column=0, padx=10, pady=10)

        # get questions from json file
        questions = open(self.get_file_path(), 'r')
        self.question_dict = json.load(questions)
        print("\nquestion dict ---", self.question_dict)

        sorted_questions_keys = sorted(self.question_dict.keys())
        print("\nsorted question keys ---", sorted_questions_keys)

        self.question_read_time = 5

        # storing each frame on a list
        self.question_list = []

        for q_id in sorted_questions_keys:
            question_frame = tk.Frame(
                self, bg=FRAME_BG_COLOR, border=FRAME_BORDER_SIZE, highlightcolor="blue")
            question_frame.grid(row=2, column=0)

            label_question = tk.Label(
                question_frame, text=self.question_dict[q_id]["text"], font=LARGEFONT)
            label_question.grid(row=0, column=0, padx=10, pady=10)

            label_timer = tk.Label(question_frame, text="Time allocated:\t" +
                                   str(self.question_dict[q_id]["time"])+"secs", font=LARGEFONT)
            label_timer.grid(row=1, column=0, padx=10, pady=10)

            self.question_list.append(question_frame)

        print("question list is", self.question_list)
        self.current_question_number = 0

        # first frame
        self.first_question_frame = tk.Frame(
            self, bg=FRAME_BG_COLOR, border=FRAME_BORDER_SIZE, highlightcolor="blue")
        self.first_question_frame.grid(row=2, column=0)

        first_label_question = tk.Label(
            self.first_question_frame, text="Click on the next button when you are ready for", font=LARGEFONT)
        first_label_question.grid(row=0, column=0, padx=10, pady=10)


# last frame
        self.last_question_frame = tk.Frame(
            self, bg=FRAME_BG_COLOR, border=FRAME_BORDER_SIZE, highlightcolor="blue")
        self.last_question_frame.grid(row=2, column=0)

        last_label_question = tk.Label(
            self.last_question_frame, text="All questions done", font=LARGEFONT)
        last_label_question.grid(row=0, column=0, padx=10, pady=10)

# initially show the first question
        self.first_question_frame.tkraise()

        self.buttonNext = ttk.Button(self, text="Next",
                                     command=self.next_question)
        # putting the button in its place
        # by using grid
        self.buttonNext.grid(row=3, column=0, padx=10, pady=10)

    def next_question(self):
        print("current question number is", self.current_question_number)

        # all questions done, show the end screen
        if self.current_question_number == len(self.question_dict):
            self.show_last_frame()
            return

        def update_question_on_screen():
            self.question_list[self.current_question_number].tkraise()

        question_thread = threading.Thread(
            target=update_question_on_screen, daemon=True)
        question_thread.start()

        self.current_question_number += 1

        def start_recording():
            run(str(self.current_question_number) + "_reading",
                self.this_student_folder_directory_path, self.question_read_time)
            print("inside start recording")

            ans_time = self.question_dict[str(
                self.current_question_number)]["time"]
            current_frame = self.question_list[self.current_question_number - 1]
            label_question = tk.Label(
                current_frame, text="Start answering, time allocated for answering is " + str(ans_time), font=LARGEFONT)
            label_question.grid(row=2, column=0, padx=10, pady=10)

            run(str(self.current_question_number) + "_answering",
                self.this_student_folder_directory_path, ans_time)

        recording_thread = threading.Thread(
            target=start_recording, daemon=True)
        recording_thread.start()

        # Makes sure the threads have finished
        print("active threads in question.py", threading.active_count())
        # time.sleep(1)
        print("all thread completed")

        # recording_thread.join()

    def show_last_frame(self):
        self.last_question_frame.tkraise()
        self.buttonNext.configure(
            text="End test", command=lambda: self.controller.show_frame(mcq_main.Quiz))
        # self.quit()

    def create_student_folder(self):
        # this part should be in login file after login is successful
        self.student_folder_directory_path = create_directory("keval909")
        self.this_student_folder_directory_path = this_student_directory_create(
            self.student_folder_directory_path)
        print("this stud folder directory path",
              self.this_student_folder_directory_path)

    def get_file_path(self):
        os.getcwd()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)
        file_dir = os.path.join(dir_path, 'resources')
        file_path = os.path.join(file_dir, "questions_testing.json")
        return (file_path)

    def quit(self):
        self.controller.destroy()

    # def __del__(self):
    #     if self.video.isOpened():
    #         self.video.release()
    #         self.out.release()


#app = chk.Checker(Questions)
# app.mainloop()
