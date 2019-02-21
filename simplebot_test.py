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


	def get_response(self):
		usr_input = self.usr_input.get()
		self.usr_input.delete(0, tk.END)

		## Reddit API
		self.r = praw.Reddit('chattest_bot')

		if len(usr_input) > 0:
			if "comment" in usr_input:
				self.subreddit = self.r.subreddit("all").comments(limit=100).search(usr_input, sort="new", limit=100)
				for submission in self.subreddit:
					output = submission
				self.conversation['state'] = 'normal'
				self.conversation.insert(tk.END, "\nHuman: " + str(usr_input) + "\n\n" + "ChatBotA: Title is " + str(output) + "\n\n" "ChatBotB: " + "Hi, sorry for the interruption" + "\n")
				self.conversation['state'] = 'disabled'
				time.sleep(1.5)

			elif "title" in usr_input:
				self.subreddit = self.r.subreddit("all").search(usr_input, sort="new", limit=100)
				for submission in self.subreddit:
					output = submission.title
				self.conversation['state'] = 'normal'
				self.conversation.insert(tk.END, "\nHuman: " + str(usr_input) + "\n\n" + "ChatBotA: The title is " + str(output) + "\n\n" "ChatBotB: " + "Hi, sorry for the interruption" + "\n")
				self.conversation['state'] = 'disabled'
				time.sleep(1.5)

			elif "author" in usr_input:
				self.subreddit = self.r.subreddit("all").search(usr_input, sort="new", limit=100)
				for submission in self.subreddit:
					output = submission.author
				self.conversation['state'] = 'normal'
				self.conversation.insert(tk.END, "\nHuman: " + str(usr_input) + "\n\n" + "ChatBotA: The author is " + str(output) + "\n\n" "ChatBotB: " + "Hi, sorry for the interruption" + "\n")
				self.conversation['state'] = 'disabled'
				time.sleep(1.5)
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

