#!/usr/bin/python
import tkinter
from tkinter import ttk

class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tkinter.Button(self)
        self.hi_there["text"] = "Hello World(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="center")

        self.quit = tkinter.Button(self, text="QUIT", command=self.master.destroy)
        self.quit.pack(side="center")

    def say_hi(self):
        print("hi there, everyone!")

root = tkinter.Tk()
root.geometry("400x300")
app = Application(master=root)
app.mainloop()

