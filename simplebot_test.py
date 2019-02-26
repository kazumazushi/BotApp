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
import praw
import re
import pdb
import sys
import random
import datetime


class TkinterGUIExample(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.title("Chatterbot")
		self.initialize()
		

	def initialize(self):
		self.grid()
		self.respond = ttk.Button(self, text='Get Response', command=self.get_response)
		self.respond.grid(column=0, row=0, sticky='nesw', padx=3, pady=3)

		self.usr_input = ttk.Entry(self, state='normal')
		self.usr_input.grid(column=1, row=0, sticky='nesw', padx=3, pady=3)

		self.conversation_lbl = ttk.Label(self, anchor=tk.E, text='Conversation:')
		self.conversation_lbl.grid(column=0, row=1, sticky='nesw', padx=3, pady=3)

		self.conversation = ScrolledText.ScrolledText(self, state='disabled')
		self.conversation.grid(column=0, row=2, columnspan=2, sticky='nesw', padx=3, pady=3)


	def display_usr(self, display):
		self.display = display


	def greeting_msg(self):
		time.sleep(4.0)
		today = datetime.datetime.today()
		bot_greeting = random.choice(["Hi today is {}".format(today), "Hello. today is {}. Thank you for comming today.".format(today),
		"Yeah, I missed you. but glad to meet you again."
		])
		self.conversation['state'] = 'normal'
		self.conversation.insert(tk.END, "ChatBotA & B: " + str(bot_greeting) + "\n\n" )
		self.conversation['state'] = 'disabled'


	def get_response(self):

		self.actual_input = self.usr_input.get()
		self.actual_delete = self.usr_input.delete(0, tk.END)

		## Reddit API
		self.r = praw.Reddit('chattest_bot')

		farewell = ["bye", "exit", "q", "quit"] 

		if len(self.actual_input) > 0:
			self.recomment = re.compile(r'comment', re.I)
			self.retitle = re.compile(r'title', re.I)
			self.reauthor = re.compile(r'author', re.I)
			if self.recomment.findall(self.actual_input):
				self.subreddit = self.r.subreddit("all").search(self.actual_input, sort="new", limit=100)
				for submission in self.subreddit:
					output = submission.comments
				self.conversation['state'] = 'normal'
				self.conversation.insert(tk.END, "\n{}: ".format(self.display) + str(self.actual_input) + "\n\n" + "ChatBotA: Title is " + str(output) + "\n\n" "ChatBotB: " + "Hi, sorry for the interruption" + "\n")
				self.conversation['state'] = 'disabled'
				time.sleep(1.5)

			elif self.retitle.findall(self.actual_input):
				self.subreddit = self.r.subreddit("all").search(self.actual_input, sort="new", limit=100)
				for submission in self.subreddit:
					output = submission.title
				self.conversation['state'] = 'normal'
				self.conversation.insert(tk.END, "\n{}: ".format(self.display) + str(self.actual_input) + "\n\n" + "ChatBotA: The title is " + str(output) + "\n\n" "ChatBotB: " + "Hi, sorry for the interruption" + "\n")
				self.conversation['state'] = 'disabled'
				time.sleep(1.5)

			elif self.reauthor.findall(self.actual_input):
				self.subreddit = self.r.subreddit("all").search(self.actual_input, sort="new", limit=100)
				for submission in self.subreddit:
					output = submission.author
				self.conversation['state'] = 'normal'
				self.conversation.insert(tk.END, "\n{}: ".format(self.display) + str(self.actual_input) + "\n\n" + "ChatBotA: The author is " + str(output) + "\n\n" "ChatBotB: " + "Hi, sorry for the interruption" + "\n")
				self.conversation['state'] = 'disabled'
				time.sleep(1.5)

			elif self.actual_input.lower() in farewell:
				self.conversation['state'] = 'normal'
				self.conversation.insert(tk.END, "\n{}: ".format(self.display) + str(self.actual_input) + "\n\n" + "ChatBotA and B: Good bye!! I miss you" + "\n\n")
				self.conversation['state'] = 'disabled'
				time.sleep(4.0)
				
			else:
				self.conversation['state'] = 'normal'
				self.conversation.insert(tk.END, "\n{}: ".format(self.display) + str(self.usr_input) + "\n\n" + "ChatBotA: I don't have any idea on " + str(usr_input) + "\n\n" + "ChatBotB: " + "Yes me neither" + "\n")
				self.conversation['state'] = 'disabled'
				time.sleep(2.0)

		else:
			self.conversation['state'] = 'normal'
			self.conversation.insert(tk.END, "ChatBotA and B: Please please please input something.\n")
			self.conversation['state'] = 'disabled'

			#polite_users = set()   # to avoid duplicates

				
			"""
				#for submission in subreddit.hot(limit=5):
				#	print("Title: ", submission.title)
				#	print("Text: ", submission.selftext)
				#	print("Score: ", submission.score)
				#	print("---------------------------------\n")
			"""

				#response = self.get_response(user_input)

if __name__ == '__main__':
	gui_example = TkinterGUIExample()
	gui_example.mainloop()

