#!/usr/bin/python
import time
import sys
import tkinter as tk
import tkinter.messagebox as tm
import os
import logging
from db_session import DB_commu

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

logging.basicConfig(filename="/tmp/simple_err.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
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
		self.login_button =  tk.Button(master, text='Logon', width=10, command=self._login_btn_clicked)
		self.login_button.place(x=70 , y=100)
		self.cancel_button =  tk.Button(master, text='Cancel', width=10, command=self._cancel_btn_clicked)
		self.cancel_button.place(x=180 , y=100)

	def _login_btn_clicked(self, account_input, password_input):
		username = account_input.get()
		password = password_input.get()
		db = DB_commu()
		db.auth_query(username, password)
		

	def _cancel_btn_clicked(self):
		quit()

if __name__=='__main__':
	output = Logger()
	root = tk.Tk()
	root.title("Welcome to Chat")
	root.geometry('300x200')
	app = Loginwindow(root)
	app.mainloop()


