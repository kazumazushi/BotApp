#!/usr/bin/python
import tkinter
from tkinter import Tk, Label, Button

class GUI_window:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

#if name == '__main__':
	#inheritance from Tk module
root = Tk()
	#widgets called from the class
my_gui = GUI_window(root)
	#user action
root.mainloop()

