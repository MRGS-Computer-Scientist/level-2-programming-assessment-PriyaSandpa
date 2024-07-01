from tkinter import *
import tkinter as tk
from tkinter.font import Font
from app_settings import *
import customtkinter as ctk
from os import *
from PIL import Image, ImageTk


class App:

    current_frame = 'Home'

    def __init__(self):
        self.window = Tk()
        self.window.geometry(str(w_width) + 'x' + str(w_height))
        self.window.title('My App')

# --Image Icons--------------------------------------------------------------------

        image_home = Image.open('images/Home.png')
        home_icon = ImageTk.PhotoImage(image_home.resize((30, 30)))
        image_list = Image.open('images/List.png')
        list_icon = ImageTk.PhotoImage(image_list.resize((30, 30)))
        image_settings = Image.open('images/Settings.png')
        settings_icon = ImageTk.PhotoImage(image_settings.resize((25, 25)))
        image_help = Image.open('images/Help.png')
        help_icon = ImageTk.PhotoImage(image_help.resize((45, 45)))
        image_add = Image.open('images/Add.png')
        add_icon = ImageTk.PhotoImage(image_add.resize((50, 50)))
        image_exit = Image.open('images/Exit.png')
        exit_icon = ImageTk.PhotoImage(image_exit.resize((40, 40)))

# --Font---------------------------------------------------------------------------

        app_font = Font(family='Josefin Sans', weight='normal',
                        size='30')

# --Home Screen--------------------------------------------------------------------
        # Home-Frame

        self.home_frame = Frame(background=main_bg_standard,
                                width=w_width, height=675)
        self.home_frame.pack()
        self.home_frame.pack_propagate(False)
        self.home_label = Label(self.home_frame, text='Home',
                                font=app_font,
                                background=main_bg_standard,
                                fg=text_colour)
        self.home_label.pack()

        # ProgressBar

        def clicker():
            self.progress_bar.step()
            self.progress.configure(text=(int(self.progress_bar.get()* 100), '%'))

        self.progress_bar = ctk.CTkProgressBar(
            self.home_frame,
            determinate_speed=5.01,
            width=w_width - 100,
            height=15,
            fg_color=help_bg_standard,
            progress_color=taskbar_bg_standard,
            )
        self.progress_bar.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.progress_bar.set(0)
        self.progress = Label(self.home_frame, text='',
                              font=('Josefin Sans semibold', 60),
                              background=main_bg_standard,
                              fg=text_colour)
        self.progress.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.test_button = Button(self.home_frame, text='Click Me',
                                  command=clicker)
        self.test_button.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

        # List

        self.list_frame = Frame(self.home_frame)
        self.list_frame.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
        self.task_list = Listbox(
            self.list_frame,
            font=('Josefin Sans', 20),
            width=15,
            height=3,
            bg=main_bg_standard,
            bd=0,
            foreground=text_colour,
            highlightthickness=0,
            selectbackground=main_bg_standard,
            selectforeground=taskbar_bg_standard,
            )
        self.task_list.pack()

# --View List (Dashboard) Screen------------------------------------------------------------------

        self.dashboard_frame = Frame(background=main_bg_standard,
                width=w_width, height=675)
        self.dashboard_frame.pack_forget()
        self.dashboard_frame.pack_propagate(False)
        self.dashboard_label = Label(self.dashboard_frame,
                text='Tasks/Habits', font=app_font,
                background=main_bg_standard)
        self.dashboard_label.pack()
        self.todo_label = Label(self.dashboard_frame, text='To-do:',
                                font=('Josefin Sans', 20, UNDERLINE),
                                background=main_bg_standard)
        self.todo_label.place(relx=0.1, rely=0.1)
        self.dbtask_list = Listbox(
            self.dashboard_frame,
            font=('Josefin Sans', 20),
            width=15,
            height=4,
            bg=main_bg_standard,
            bd=0,
            foreground=text_colour,
            highlightthickness=0,
            selectbackground=main_bg_standard,
            selectforeground=taskbar_bg_standard,
            )
        self.dbtask_list.place(relx=0.2, rely=0.2)
        self.completed_label = Label(self.dashboard_frame, text='Done:',
                font=('Josefin Sans', 20, UNDERLINE),
                background=main_bg_standard)
        self.completed_label.place(relx=0.1, rely=0.45)
        self.dbcompleted_list = Listbox(
            self.dashboard_frame,
            font=('Josefin Sans', 20),
            width=15,
            height=4,
            bg=main_bg_standard,
            bd=0,
            foreground='#878787',
            highlightthickness=0,
            selectbackground=main_bg_standard,
            selectforeground=taskbar_bg_standard,
            )
        self.dbcompleted_list.place(relx=0.2, rely=0.55)
        self.dbbutton_frame = Frame(self.dashboard_frame,
                                    background=main_bg_standard)
        self.dbbutton_frame.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
        self.complete_button = Button(self.dbbutton_frame,
                text='Completed!', command=lambda :
                self.switchList(self.dbtask_list, self.dbcompleted_list))
        self.complete_button.grid(row=0, column=0, padx=5)
        self.incomplete_button = Button(self.dbbutton_frame,
                text='Incomplete', command=lambda :
                self.switchList(self.dbcompleted_list, self.dbtask_list))
        self.incomplete_button.grid(row=0, column=1, padx=5)
        self.delete_completed = Button(self.dbbutton_frame,
                text='Delete', command=lambda :
                self.task_options('Delete Completed'))
        self.delete_completed.grid(row=0, column=2, padx=5)

#--- Lists -----------------------------------------------------------------------

        self.tasks=["Task 1"]
        self.completed=["Habit 1"]

        for item in self.tasks:
            self.task_list.insert(END, item)
            self.dbtask_list.insert(END, item)

        for item in self.completed:
                self.dbcompleted_list.insert(END, item)

# --Settings Screen---------------------------------------------------------------

        self.settings_frame = Frame(background=main_bg_standard,
                                    width=w_width, height=675)
        self.settings_frame.pack_forget()
        self.settings_frame.pack_propagate(False)
        self.settings_label = Label(self.settings_frame, text='Settings'
                                    , font=app_font,
                                    background=main_bg_standard)
        self.settings_label.pack()

# --Help Screen-------------------------------------------------------------------

        self.help_frame = Frame(background=help_bg_standard,
                                width=w_width, height=w_height)
        self.help_frame.pack_forget()
        self.help_frame.pack_propagate(False)
        self.help_label = Label(self.help_frame, text='Help',
                                font=app_font,
                                background=help_bg_standard)
        self.help_label.pack()

# --Taskbar-----------------------------------------------------------------------

        self.taskbar_frame = Frame(background=taskbar_bg_standard,
                                   width=w_width, height=50)
        self.taskbar_frame.place(relx=0.5, rely=0.9635,
                                 anchor=tk.CENTER)

        self.home_button = Button(
            self.taskbar_frame,
            image=home_icon,
            background=taskbar_bg_standard,
            width=30,
            height=30,
            highlightthickness=0,
            bd=0,
            command=lambda : self.go_to_frame('Home'),
            activebackground=taskbar_bg_standard,
            )
        self.home_button.place(x=165, y=10)

        self.dashboard_button = Button(
            self.taskbar_frame,
            image=list_icon,
            background=taskbar_bg_standard,
            width=30,
            height=30,
            highlightthickness=0,
            bd=0,
            command=lambda : self.go_to_frame('Dashboard'),
            activebackground=taskbar_bg_standard,
            )
        self.dashboard_button.place(x=55, y=10)

        self.settings_button = Button(
            self.taskbar_frame,
            image=settings_icon,
            background=taskbar_bg_standard,
            width=30,
            height=30,
            highlightthickness=0,
            bd=0,
            command=lambda : self.go_to_frame('Settings'),
            activebackground=taskbar_bg_standard,
            )
        self.settings_button.place(x=275, y=10)

# --Add Task Screen---------------------------------------------------------------
        # Frame for "Add Task" screen

        self.addtask_frame = Frame(background=help_bg_standard,
                                   width=w_width, height=w_height)
        self.addtask_frame.pack_forget()
        self.addtask_frame.pack_propagate(False)
        self.addtask_label = Label(self.addtask_frame, text='Add Task',
                                   font=app_font,
                                   background=help_bg_standard)
        self.addtask_label.pack()

        # Entry box for adding tasks:

        self.subquestion_1 = Label(self.addtask_frame,
                                   text='Enter the name of your task:',
                                   font=('Josefin Sans', 15),
                                   background=help_bg_standard)
        self.subquestion_1.place(relx=0.1, rely=0.2, anchor=tk.W)
        self.task_entry = Entry(self.addtask_frame, font='Verdana 12',
                                width=25, bd=0, borderwidth=0)
        self.task_entry.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

       # Confirm Task & Cancel buttons:

        self.button_frame = Frame(self.addtask_frame)
        self.button_frame.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
        self.confirm_button = Button(self.button_frame,
                text='Create Task', command=lambda :
                self.task_options('Create'))
        self.confirm_button.grid(row=0, column=0, padx=5)
        self.delete_button = Button(self.button_frame, text='Cancel',
                                    command=lambda :
                                    self.task_options('Clear'))
        self.delete_button.grid(row=0, column=1, padx=5)

       # Go to the add-task screen:

        self.plus_button = Button(
            self.home_frame,
            background=main_bg_standard,
            image=add_icon,
            width=50,
            height=50,
            highlightthickness=0,
            bd=0,
            border=0,
            activebackground=main_bg_standard,
            command=lambda : self.go_to_frame('Add'),
            )
        self.plus_button.place(x=295, y=w_height - 115)

# --Help Buttons-------------------------------------------------------------------

        self.help_button_1 = Button(
            self.home_frame,
            image=help_icon,
            background=main_bg_standard,
            width=45,
            height=45,
            highlightthickness=0,
            bd=0,
            border=0,
            activebackground=main_bg_standard,
            command=lambda : self.go_to_frame('Help'),
            )
        self.help_button_1.place(x=310, y=15)

        self.help_button_2 = Button(
            self.dashboard_frame,
            image=help_icon,
            background=main_bg_standard,
            width=45,
            height=45,
            highlightthickness=0,
            bd=0,
            border=0,
            activebackground=main_bg_standard,
            command=lambda : self.go_to_frame('Help'),
            )
        self.help_button_2.place(x=310, y=15)

        self.help_button_3 = Button(
            self.settings_frame,
            image=help_icon,
            background=main_bg_standard,
            width=45,
            height=45,
            highlightthickness=0,
            bd=0,
            border=0,
            activebackground=main_bg_standard,
            command=lambda : self.go_to_frame('Help'),
            )
        self.help_button_3.place(x=310, y=15)

# --Exit Button-------------------------------------------------------------------

        self.exit_button_help = Button(
            self.help_frame,
            image=exit_icon,
            background=help_bg_standard,
            width=40,
            height=40,
            highlightthickness=0,
            bd=0,
            border=0,
            activebackground=help_bg_standard,
            command=lambda : self.go_to_frame('Home'),
            )
        self.exit_button_help.place(x=30, y=15)
        self.exit_button_add = Button(
            self.addtask_frame,
            image=exit_icon,
            background=help_bg_standard,
            width=40,
            height=40,
            highlightthickness=0,
            bd=0,
            border=0,
            activebackground=help_bg_standard,
            command=lambda : self.go_to_frame('Home'),
            )
        self.exit_button_add.place(x=30, y=15)

# --Mainloop----------------------------------------------------------------------

        self.window.mainloop()

# --Go to frame function----------------------------------------------------------

#Method that switches the screen depending on what screen the user wants to go to. 

    def go_to_frame(self, next_frame):

#This part of the method determines which screen should be hidden when user switches screens.

        if self.current_frame == 'Home':
            self.home_frame.pack_forget()
        elif self.current_frame == 'Dashboard':
            self.dashboard_frame.pack_forget()
        elif self.current_frame == 'Settings':
            self.settings_frame.pack_forget()
        elif self.current_frame == 'Help':
            self.help_frame.pack_forget()
            self.taskbar_frame.place(relx=0.5, rely=0.9635,
                    anchor=tk.CENTER)
        elif self.current_frame == 'Add':
            self.addtask_frame.pack_forget()
            self.taskbar_frame.place(relx=0.5, rely=0.9635,
                    anchor=tk.CENTER)

#This part of the method determines which screen should be displayed when the user switches screens.

        if next_frame == 'Dashboard':
            self.dashboard_frame.pack()
            self.current_frame = 'Dashboard'
        elif next_frame == 'Settings':
            self.settings_frame.pack()
            self.current_frame = 'Settings'
        elif next_frame == 'Home':
            self.home_frame.pack()
            self.current_frame = 'Home'
        elif next_frame == 'Help':
            self.help_frame.pack()
            self.current_frame = 'Help'
            self.taskbar_frame.place_forget()
        elif next_frame == 'Add':
            self.addtask_frame.pack()
            self.current_frame = 'Add'
            self.taskbar_frame.place_forget()

    def task_options(self, option):

        # Add task to list.

        if option == 'Create':
            self.tasks.append(self.task_entry.get())
            print (self.tasks)
            self.task_list.insert(END, self.tasks[-1])
            self.dbtask_list.insert(END, self.tasks[-1])
            self.task_entry.delete(0,END)

        elif option == 'Clear':

        # Clear input box

            self.task_entry.delete(0, END)
            self.go_to_frame('Home')
       
    def switchList(self, current, next):
        indexList=current.curselection()
        if indexList:
            index=indexList[0]
            val=current.get(index)
            current.delete(index)
            next.insert(END, val)
            #pass
        if current==self.dbtask_list:
            self.task_list.delete(index)
        if next==self.dbtask_list:
            self.task_list.insert(END, val)

        # cross off item





            #self.dbcompleted_list.insert(END,
            #        self.dbtask_list.get(ANCHOR))
            #self.dbtask_list.selection_clear(0, END)
            #self.dbtask_list.delete(ANCHOR)
        #elif option == 'Incomplete':
        #    pass
        # uncross item

            #self.dbtask_list.insert(END, self.dbcompleted_list.get(ANCHOR))
            #self.dbcompleted_list.selection_clear(0, END)
            #self.dbcompleted_list.delete(ANCHOR)
        #elif option == 'Delete Completed':

        # delete completed and unneeded tasks



              # count = 0
              # while count < self.dbtask_list.size():
              #      if self.dbtask_list.itemcget(count, "fg") == "#dedede":
              #            self.dbtask_list.delete(self.dbtask_list.index(count))
              #      count += 1


if __name__ == '__main__':
    app = App()
