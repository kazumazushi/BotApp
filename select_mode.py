#!/usr/bin/python
# from chatterbot import ChatBot
import tkinter as tk
try:
	import ttk as ttk
	import ScrolledText
except ImportError:
	import tkinter.ttk as ttk
	import tkinter.scrolledtext as ScrolledText
import time
import datetime
from simplebot_test import TkinterGUIExample
from chat_usr import Chat_usr


class Select_which(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.title("Please select which one is")
		self.geometry('150x200')
		self.initialize()
		

	def initialize(self):
		self.tlk_chat = ttk.Button(self, text='Talk to Bot', command=self.chatbot_clicked)
		self.tlk_chat.place(x=5, y=45)

		self.tlk_usr = ttk.Button(self, text='Talk to User', command=self.talk_usr_clicked)
		self.tlk_usr.place(x=120, y=45)

	def registered_name(self, registered):
		self.registered = registered


	def chatbot_clicked(self):
		self.to_bot = TkinterGUIExample()
		self.to_bot.display_inbot(self.registered)
		self.to_bot.greeting_msg() 

	def talk_usr_clicked(self):
		self.to_usr = Chat_usr()
		self.to_usr.display_inusr(self.registered)


if __name__ == '__main__':
	launch_select = Select_which()
	launch_select.mainloop()

