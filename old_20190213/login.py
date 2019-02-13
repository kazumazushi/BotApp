#!/usr/bin/python
import time
import sys
import tkinter as tk
import tkinter.messagebox as tm
#import db_session

class Loginwindow(tk.Frame):
	def __init__(self, master):
		super().__init__(master)
#		self.title("Welcome to Chat")
#   	self.geometry('300x200')
		self.account_label = tk.Label(master, text='Account')
		self.password_label = tk.Label(master, text='Password')
		self.account_input = tk.Entry(master)
		self.password_input = tk.Entry(master)
		self.account_label.place(x=30 , y=50)
		self.password_label.place(x=30 , y=70)
		self.account_input.place(x=90 , y=50)
		self.password_input.place(x=90 , y=70) 
		self.login_button =  tk.Button(master, text='Logon', width=10, command=self._login_btn_clicked)
		self.login_button.place(x=70 , y=100)
		self.cancel_button =  tk.Button(master, text='Cancel', width=10, command=self._cancel_btn_clicked)
		self.cancel_button.place(x=180 , y=100)

	def _login_btn_clicked(self):
		username = self.account_input.get()
		password = self.password_input.get()

		if username == "" and password == "":
			tm.showinfo("Login info", " Welcome")
		else:
			tm.showerror("Login error", "Incorrect username")	

	def _cancel_btn_clicked(self):
		quit()

if __name__=='__main__':
	root = tk.Tk()
	root.title("Welcome to Chat")
	root.geometry('300x200')
	app = Loginwindow(root)
	app.mainloop()
	
