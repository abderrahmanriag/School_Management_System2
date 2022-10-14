import math
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import mysql.connector as mc
import awesometkinter as atk
from tkcalendar import DateEntry


def set_dimensions(dim, per):
    return math.floor((per * dim) / 100)


class Student:
    def __init__(self, frame, win, background):
        self.frame = frame
        self.win = win
        self.BACKGROUND = background
        self.FONT = ('tahoma', 15)
        self.style = ttk.Style()
        self.style.configure('style1.TButton', background=self.BACKGROUND, font=self.FONT)
        self.width = self.win.winfo_screenwidth()
        self.height = self.win.winfo_screenheight()
        self.master = Tk
        self.std_info = Frame(self.frame, pady=10, padx=10)
        self.std_info.grid(row=0, column=1, sticky='snew')
        self.img1 = Image.open('icons/student200.png')
        self.img1.thumbnail((150, 150))
        self.new_img1 = ImageTk.PhotoImage(self.img1)
        self.univ_label = Label(self.std_info, image=self.new_img1)
        self.univ_label.pack()
        self.std_event = self.win.bind("<Alt_L>s", self.open_std_win)
        self.univ_button = ttk.Button(self.std_info, text='Students Management', style='style1.TButton',
                                      command=lambda: self.open_std_win(self.std_event))
        self.univ_button.pack()

    def open_std_win(self, event):
        StudentWindow(self.win)


def load_data():
    db = mc.connect(
        host='localhost',
        user='root',
        password='',
        database='school_ms'
    )
    cursor = db.cursor()
    cursor.execute('select * from students')
    return cursor.fetchall()


class StudentWindow:
    def __init__(self, win):
        self.win = win
        self.master = Toplevel()
        self.master.title('Students Management')
        self.width = self.win.winfo_screenwidth()
        self.height = self.win.winfo_screenheight()
        self.FONT = ('tahoma', 15)
        self.FONT1 = ('tahoma', 10)
        self.master.geometry(
            '{w}x{h}+{x}+{y}'.format(w=set_dimensions(self.width, 73.20), h=set_dimensions(self.height, 65.10),
                                     x=set_dimensions(self.width, 13.17), y=set_dimensions(self.height, 13.02)))
        # Left Frame Start Here
        self.left_frame = Frame(self.master)
        self.left_frame.place(relwidth=0.4, relheight=1)

        self.name = StringVar()
        self.last = StringVar()
        self.birth = StringVar()
        self.emailvar = StringVar()
        Label(self.left_frame, text='First Name:', font=self.FONT).grid(row=0, column=0, padx=2, pady=2)
        self.first_name = ttk.Entry(self.left_frame, font=self.FONT, textvariable=self.name)
        self.first_name.grid(row=0, column=1, pady=10, padx=2)
        Label(self.left_frame, text='Last Name:', font=self.FONT).grid(row=1, column=0, pady=10, padx=2)
        self.last_name = ttk.Entry(self.left_frame, font=self.FONT, textvariable=self.last)
        self.last_name.grid(row=1, column=1, pady=10, padx=2)
        Label(self.left_frame, text='Birth Date:', font=self.FONT).grid(row=2, column=0, pady=10, padx=2)
        self.birth_date = DateEntry(self.left_frame, selectmode='day', date_pattern="yyyy-mm-dd", font=self.FONT,
                                    textvariable=self.birth)
        self.birth_date.grid(row=2, column=1, pady=10, padx=2)
        Label(self.left_frame, text='Email:', font=self.FONT).grid(row=3, column=0, pady=10, padx=2)
        self.email = ttk.Entry(self.left_frame, font=self.FONT, textvariable=self.emailvar)
        self.email.grid(row=3, column=1, pady=10, padx=2)

        self.style = ttk.Style()
        self.style.configure('sb.TButton', background='orange', font=self.FONT1)

        self.add_event = self.master.bind("<Alt_L>s", self.add_std)
        self.s = Image.open('icons/diskette.png')
        self.s = ImageTk.PhotoImage(self.s)
        self.add_button = ttk.Button(self.left_frame, text='ADD', image=self.s, compound='left', style='sb.TButton',
                                     command=lambda: self.add_std(self.add_event))
        # self.add_button = atk.Button3d(self.left_frame, text='ADD', image=self.s, compound='left', command=self.add_std)
        self.add_button.place(relx=0.07, rely=0.45)

        self.delete_event = self.master.bind("<Alt_L>d", self.delete_btn)
        self.eraser = Image.open('icons/erase.png')
        self.eraser = ImageTk.PhotoImage(self.eraser)
        self.erasing = ttk.Button(self.left_frame, text='DELETE', image=self.eraser, compound='left',
                                  style='sb.TButton', command=lambda: self.delete_btn(self.delete_event))
        self.erasing.place(relx=0.37, rely=0.45)

        self.upadte_event = self.master.bind("<Alt_L>u", self.update_btn)
        self.u = Image.open('icons/pencil.png')
        self.u = ImageTk.PhotoImage(self.u)
        self.up_button = ttk.Button(self.left_frame, text='UPDATE',
                                    image=self.u,
                                    compound='left', style='sb.TButton',
                                    command=lambda: self.update_btn(self.upadte_event))
        self.up_button.place(relx=0.67, rely=0.45)

        self.reset_logo = Image.open('icons/reset.png')
        self.reset_logo = ImageTk.PhotoImage(self.reset_logo)
        self.reset_button = ttk.Button(self.left_frame, text='RESET',
                                       image=self.reset_logo,
                                       compound='left', style='sb.TButton', command=self.reset)
        self.reset_button.place(relx=0.37, rely=0.55)

        # Middle Frame Start Here
        Frame(self.master, bg='orange').place(relx=0.4, relwidth=0.2, relheight=0.8, rely=0.1)

        # Right Frame Start Here
        self.right_frame = Frame(self.master)
        self.right_frame.place(relx=0.401, relwidth=0.6, relheight=1)

        # Search Frame Start Here
        self.search_frame = Frame(self.right_frame)
        self.search_frame.place(relx=0, rely=0, relwidth=1, relheight=0.09)

        self.search_var = StringVar()
        self.search_entry = ttk.Entry(self.search_frame, font=self.FONT,
                                      textvariable=self.search_var)
        self.search_entry.place(relx=0.05, rely=0.2, relwidth=0.7)
        self.search_event = self.search_entry.bind('<Return>', self.search_func)

        self.search_logo = Image.open('icons/search.png')
        self.search_logo = ImageTk.PhotoImage(self.search_logo)
        self.search_button = ttk.Button(self.search_frame, image=self.search_logo,
                                        style='sb.TButton',
                                        command=lambda: self.search_func(self.search_event))
        self.search_button.place(relx=0.8, rely=0.2)

        # Tree Frame Start Here
        self.view_frame = Frame(self.right_frame)
        self.view_frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

        # Tree View
        self.tree = ttk.Treeview(self.view_frame,
                                 columns=('ID', 'First Name', 'Last Name', 'Birth Date', 'Email'),
                                 show='headings')
        self.tree.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

        self.scrollbar = Scrollbar(self.view_frame, orient=VERTICAL, command=self.tree.yview)
        self.scrollbar.place(relx=0.95, rely=0.05, relheight=0.9)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.tree.heading('ID', text='ID')
        self.tree.heading('First Name', text='First Name')
        self.tree.heading('Last Name', text='Last Name')
        self.tree.heading('Birth Date', text='Birth Date')
        self.tree.heading('Email', text='Email')

        self.tree.column('ID', width=7)
        self.tree.column('First Name', width=100)
        self.tree.column('Last Name', width=100)
        self.tree.column('Birth Date', width=70)
        self.tree.column('Email', width=200)
        self.fill_up(load_data())
        self.tree.bind('<ButtonRelease>', self.show)
        self.master.bind("<Escape>", self.close_win)
        self.iid = int(0)

    def close_win(self, event):
        self.master.destroy()

    def add_std(self, event):
        choose = messagebox.askyesno("ADD", "Add New Student", parent=self.master)
        if choose > 0:
            mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='school_ms'
            )
            cursor = mydb.cursor()
            sql = 'insert into students (FirstName, LastName, BirthDate, Email) values (%s, %s, %s, %s)'
            val = (self.first_name.get(),
                   self.last_name.get(),
                   self.birth_date.get(),
                   self.email.get())
            print(val)
            cursor.execute(sql, val)
            self.fill_up(load_data())
            mydb.commit()
            mydb.close()
            self.reset()

    def fill_up(self, results):
        self.tree.delete(*self.tree.get_children())
        for result in results:
            self.iid = result[0]
            result = list(result)
            result[0] = len(self.tree.get_children()) + 1
            self.tree.insert('', 'end', iid=self.iid, values=result)

    def show(self, event):
        self.iid = self.tree.focus()
        alldata = self.tree.item(self.iid)
        val = alldata['values']
        self.name.set(val[1])
        self.last.set(val[2])
        self.birth.set(val[3])
        self.emailvar.set(val[4])

    def reset(self):
        self.first_name.delete(0, 'end')
        self.last_name.delete(0, 'end')
        self.birth_date.delete(0, 'end')
        self.email.delete(0, 'end')

    def delete_btn(self, event):
        choose = messagebox.askyesno("DELETE", "Delete This Student", parent=self.master)
        if choose > 0:
            mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='school_ms'
            )
            cursor = mydb.cursor()
            sql = ('delete from students where id=' + self.iid)
            cursor.execute(sql)
            mydb.commit()
            mydb.close()
            results = load_data()
            self.fill_up(results)
            self.reset()

    def update_btn(self, event):
        choose = messagebox.askyesno("UPDATE", "Update This Student", parent=self.master)
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='school_ms'
        )
        cursor = mydb.cursor()
        sql = ('update students set FirstName=%s, LastName=%s, BirthDate=%s, Email=%s where id=%s')
        val = (self.name.get(), self.last.get(), self.birth.get(), self.emailvar.get(), self.iid)
        cursor.execute(sql, val)
        mydb.commit()
        mydb.close()
        item = self.tree.selection()
        for i in item:
            self.tree.item(i, values=(self.tree.item(i, 'values')[0],
                                      self.name.get(),
                                      self.last.get(),
                                      self.birth.get(),
                                      self.emailvar.get()))
        self.reset()

    def search_func(self, event):
        if self.search_entry.get() == '':
            self.fill_up(load_data())
        else:
            db = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='school_ms'
            )
            cursor = db.cursor()
            variable = str(self.search_var.get())
            sql = 'SELECT * FROM students WHERE FirstName LIKE "%s" OR LastName LIKE "%s"'
            val = (variable, variable)
            cursor.execute(sql)
            print(variable)
            print(cursor.fetchall())
            self.fill_up(cursor.fetchall())


"""
768 = 100
100 = x
x = 10000/768


768 = 100
x = 13
"""
