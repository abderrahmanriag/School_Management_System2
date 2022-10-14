import math
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk


def set_dimensions(dim, per):
    return math.floor((per * dim) / 100)


class Library:
    def __init__(self, frame, win, background):
        self.frame = frame
        self.win = win
        self.BACKGROUND = background
        self.width = self.win.winfo_screenwidth()
        self.height = self.win.winfo_screenheight()
        self.FONT = ('tahoma', 15)
        self.style = ttk.Style()
        self.style.configure('style1.TButton', background=self.BACKGROUND, font=self.FONT)
        self.master = Tk
        self.university_info = Frame(self.frame, pady=10, padx=10)
        self.university_info.grid(row=0, column=0)
        self.img1 = Image.open('icons/lib200.png')
        self.img1.thumbnail((150, 150))
        self.new_img1 = ImageTk.PhotoImage(self.img1)
        self.univ_label = Label(self.university_info, image=self.new_img1)
        self.univ_label.pack()
        self.univ_button=ttk.Button(self.university_info, text='Library Management', style='style1.TButton', command=self.open_lib_win)
        self.univ_button.pack()

    def open_lib_win(self):
        LibraryWindow(self.win)


class LibraryWindow:
    def __init__(self, win):
        self.win = win
        self.width = self.win.winfo_screenwidth()
        self.height = self.win.winfo_screenheight()
        self.master = Toplevel()
        self.master.geometry(
            '{w}x{h}+{x}+{y}'.format(w=set_dimensions(self.width, 73.20), h=set_dimensions(self.height, 65.10),
                                     x=set_dimensions(self.width, 13.17), y=set_dimensions(self.height, 13.02)))


"""
768 = 100
100 = x
x = 10000/768


768 = 100
x = 13
"""