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
		user_input = self.usr_input.get()
		self.usr_input.delete(0, tk.END)

		## Reddit API
		self.r = praw.Reddit('chattest_bot')
		self.subreddit = self.r.subreddit("all").search(user_input, sort="new", limit=11)
		for submission in self.subreddit:
			pass

		#polite_users = set()   # to avoid duplicates

			
		"""
			#for submission in subreddit.hot(limit=5):
			#	print("Title: ", submission.title)
			#	print("Text: ", submission.selftext)
			#	print("Score: ", submission.score)
			#	print("---------------------------------\n")
		"""

			#response = self.get_response(user_input)
		self.conversation['state'] = 'normal'
		self.conversation.insert(tk.END, "Human: " + str(user_input) + "\n\n" + "ChatBotA: Title is " + str(submission.title) + " and the author is " + str(submission.author) + " and URL is " + str(submission.url) + " and Visited is " + str(submission.visited)  
			+ " and comments in this section says " + "\n\n" + "ChatBotB: " + "Hi, sorry for the interruption" + "\n")
		self.conversation['state'] = 'disabled'
		time.sleep(0.5)

if __name__ == '__main__':
	gui_example = TkinterGUIExample()
	gui_example.mainloop()

