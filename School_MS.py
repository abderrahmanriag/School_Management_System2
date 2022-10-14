from tkinter import *

from PIL import Image, ImageTk

from EXM import Exam
from LIB import Library
from std import Student
from stf import Staff
from univ import Univ


class School_Management_System:
    def __init__(self, win):
        self.master = win
        self.master.title('School Management System')
        self.width = win.winfo_screenwidth()
        self.height = win.winfo_screenheight()
        self.master.geometry('{w}x{h}'.format(w=self.width, h=self.height))
        self.master.state('zoomed')
        self.BACKGROUND = '#0090c0'
        # Blank Frame
        self.blank_frame = Frame(win, height=50).pack(side='top', fill=X)
        self.red_frame1 = Frame(win, height=5, bg='orange')
        self.red_frame1.pack(side='top', fill=X)
        # Top Frame Start Here
        self.frame_top = Frame(win, bg=self.BACKGROUND, height=80)
        self.frame_top.pack(fill=X)
        Label(self.frame_top, text='School Management System',
              bg=self.BACKGROUND, pady=50, font=('tah-oma', 30), fg='white').pack()
        # Top Frame End Here
        self.red_frame2 = Frame(win, height=5, bg='orange')
        self.red_frame2.pack(side='top', fill=X)
        # Center Frame Start Here
        self.center_frame = Frame(win, height=200, padx=100, pady=10)
        self.center_frame.pack(fill=X)
        self.center_frame.grid_columnconfigure(0, weight=1)
        self.center_frame.grid_columnconfigure(1, weight=1)
        self.center_frame.grid_columnconfigure(2, weight=1)
        # Center Frame End Here

        # University Object
        Univ(self.center_frame, win, self.BACKGROUND)

        # Student Object
        Student(self.center_frame, win, self.BACKGROUND)

        # Staff Object
        Staff(self.center_frame, win, self.BACKGROUND)

        # Bottom Frame Start Here
        self.bottom_frame = Frame(win, height=200, padx=100, pady=10)
        self.bottom_frame.pack(fill=X)
        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(1, weight=1)
        # Bottom Frame End Here

        # Library Object
        Library(self.bottom_frame, win, self.BACKGROUND)

        # Exam Object
        Exam(self.bottom_frame, win, self.BACKGROUND)
