#!/usr/bin/python
import time
import sys
import tkinter as tk
import tkinter.messagebox as tm
import os
import logging
from db_session import DB_engine, DB_session, Userquery, Userregister, Session_close, Query_table, Query_table2
"""
class Logger():
	def __init__(self):
		print('start')
		log_dir = r'/tmp'
		log_file = os.path.join(log_dir, 'err.log')
		logger_name = __name__
		print('logger_name: "%s"' % logger_name)
		logger = logging.getLogger(logger_name)
		logger.setLevel(logging.DEBUG)
		stream_handler = logging.StreamHandler()
		stream_handler.setLevel(logging.DEBUG)
		stream_handler.setFormatter(logging.Formatter('%(message)s'))
		logger.addHandler(stream_handler)
		file_handler = logging.FileHandler('err.log', mode='a', encoding='utf-8')
		file_handler.setLevel(logging.DEBUG)
		file_handler.setFormatter(logging.Formatter('%(message)s'))
		logger.debug('start logging')
		
"""

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
		self.login_button =  tk.Button(master, text='Logon', width=6, command=self._login_btn_clicked)
		self.login_button.place(x=20 , y=100)
		self.cancel_button =  tk.Button(master, text='Cancel', width=6, command=self._cancel_btn_clicked)
		self.cancel_button.place(x=110 , y=100)
		self.login_button =  tk.Button(master, text='Register', width=6, command=self._register_btn_clicked)
		self.login_button.place(x=200, y=100)

	def _login_btn_clicked(self):
		self.username = self.account_input.get()
		self.password = self.password_input.get()
		authcheck = Userquery()
		authcheck.auth_session(self.username, self.password)

	def _cancel_btn_clicked(self):
		cancel_session = Session_close()
		quit()

	def _register_btn_clicked(self):
		reg = tk.Tk()
		reg.title("Registration")
		reg.geometry('300x200')
		regwin = Regwindow(reg)
		regwin.mainloop()

class Regwindow(tk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		self.reg_account_label = tk.Label(parent, text='Registration Account')
		self.reg_password_label = tk.Label(parent, text='Registration Password')
		self.reg_email_label = tk.Label(parent, text='Registration email')
		self.reg_account_input = tk.Entry(parent)
		self.reg_password_input = tk.Entry(parent)
		self.reg_email_input = tk.Entry(parent)
		self.reg_account_label.place(x=5 , y=20)
		self.reg_password_label.place(x=5, y=50)
		self.reg_email_label.place(x=5, y=80)
		self.reg_account_input.place(x=80 , y=20)
		self.reg_password_input.place(x=80 , y=50) 
		self.reg_email_input.place(x=80, y=80) 
		self.reg_button = tk.Button(parent, text='Registration', width=5, command=self.reg_decision_btn_clicked)
		self.reg_button.place(x=20 , y=170)
		self.reg_cancel_button = tk.Button(parent, text='Cancel', width=5, command=self.reg_cancel_btn_clicked)
		self.reg_cancel_button.place(x=120 , y=170)

	def reg_decision_btn_clicked(self):
		reg_pass = Userregister()
		self.newuser = self.reg_account_input.get()
		self.newpassword = self.reg_password_input.get()
		self.newemail = self.reg_email_input.get()
		reg_pass.register(self.newuser,self.newpassword, self.newemail)

	def reg_cancel_btn_clicked(self):
		cancel_session = Session_close()
		quit()



if __name__=='__main__':
	root = tk.Tk()
	root.title("Welcome to Chat")
	root.geometry('300x200')
	app = Loginwindow(root)
	app.mainloop()

	
