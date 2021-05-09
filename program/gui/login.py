import tkinter as tk
from tkinter import ttk
import sqlite3 as sql
import os
# import gui.startPage
# import gui.greeting
from gui import startPage
from gui import greeting

LARGEFONT = ("Verdana", 35)
# login details 'boss','1234'
# second window frame page1


class Login(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Login page", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # this wil create a label widget
        l1 = ttk.Label(self, text="Email Id:")
        l2 = ttk.Label(self, text="Password:")

        # grid method to arrange labels in respective
        # rows and columns as specified
        l1.grid(row=1, column=0, sticky="W", pady=2)
        l2.grid(row=2, column=0, sticky="W", pady=2)

        email_val = tk.StringVar()
        password_val = tk.StringVar()

        # entry widgets, used to take entry from user
        email = ttk.Entry(self, textvariable=email_val)
        password = ttk.Entry(self, textvariable=password_val)

        # this will arrange entry widgets
        email.grid(row=1, column=1, pady=2)
        password.grid(row=2, column=1, pady=2)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="StartPage",
                             command=lambda: controller.show_frame(startPage.StartPage))

        # putting the button in its place
        # by using grid
        button1.grid(row=3, column=1, padx=10, pady=10)

        def checkcred():
            username = email_val.get()
            password = password_val.get()
            local_path = os.path.realpath(__file__)
            parent_path = os.path.dirname(local_path)
            # filename = os.path.join(str(local_path), "data.db")
            filename = os.path.join(str(parent_path),"data.db")
            print(filename)
            con = sql.connect(filename)
            print(con)
            cur = con.cursor()
            # statement = "SELECT username from users WHERE username=" + \
            str(username)+" AND Password = "+str(password)+";"
            statement = "SELECT username from users WHERE username='{}' AND Password = '{}';".format(
                username, password)
            cur.execute(statement)
            if not cur.fetchone():  # An empty result evaluates to False.
                print("Login failed")
            else:
                print("Login Passed")
            controller.show_frame(greeting.Greeting)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Greeting page",
                             command=checkcred)
        # putting the button in its place by
        # using grid
        button2.grid(row=4, column=1, padx=10, pady=10)


# import helper.checker as chk
# app =chk.Checker(Login)
# app.mainloop()
