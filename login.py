#!/usr/bin/python
import time
import sys
import tkinter as tk
import tkinter.messagebox as tm
from db_sessiion import *
from db_model import * 

class Loginwindow(tk.Frame):
	def __init__(self, windpw):
		super().__init__(window)
		self.title("Welcome to Chat")
		self.geometry('300x200')
		self.account_label = tk.Label(self, text='Account')
		self.password_label = tk.Label(self, text='Password')
		self.account_input = tk.Entry(self)
		self.password_input = tk.Entry(self)
		self.account_label.place(x=30 , y=50)
		self.password_label.place(x=30 , y=70)
		self.account_input.place(x=90 , y=50)
		self.password_input.place(x=90 , y=70) 
		self.login_button =  tk.Button(self, text='Logon', width=10, command=self.destroy)
		self.login_button.place(x=70 , y=100)
		self.cancel_button =  tk.Button(self text='Cancel', width=10, command=self.destroy)
		self.cancel_button.place(x=180 , y=100)

    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()

        # print(username, password)

        if username == "" and password == "":
            tm.showinfo("Login info", "Welcome")
        else:
            tm.showerror("Login error", "Incorrect username")


root = tk.Tk()
lf = Loginwindow(root)
root.mainloop()

#window = tk.Tk()
#window.title("Welcome to Chat")
#window.geometry('300x200')
#account_label = tk.Label(window, text='Account')
#password_label = tk.Label(window, text='Password')
#account_input = tk.Entry(window)
#password_input = tk.Entry(window)
#account_label.place(x=30 , y=50)
#password_label.place(x=30 , y=70)
#account_input.place(x=90 , y=50)
#password_input.place(x=90 , y=70) 
#login_button =  tk.Button(window, text='Logon', width=10, command=window.destroy)
#login_button.place(x=70 , y=100)
#cancel_button =  tk.Button(window, text='Cancel', width=10, command=window.destroy)
#cancel_button.place(x=180 , y=100)
#cancel_button = tk.Button(window, text='Logon', width=15, command=window.destroy)
#cancel_button.pack(padx=15, side=LEFT)
#window.mainloop()

