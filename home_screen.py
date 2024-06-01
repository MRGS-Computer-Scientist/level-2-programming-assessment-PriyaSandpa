from tkinter import *
from app_settings import *

class App():
    def __init__(self):
        self.window=Tk()
        self.window.geometry(str(w_width) +"x"+ str(w_height))
        self.window.title("My App")

        home=PhotoImage(file="images/Home.png")

        self.main_frame = Frame(background="#F7EDE2", width=w_width, height=625)
        self.main_frame.pack()

        self.taskbar_frame=Frame(background="#F6BD60", width=w_width, height=50)
        self.taskbar_frame.pack()

        self.home_button=Button(self.taskbar_frame, image=home, width=4, height=1)
        self.home_button.place(x=160, y=10)

        self.stats_button=Button(self.taskbar_frame, text="Stats", width=4, height=1,command=exit)
        self.stats_button.place(x=60, y=10)

        self.settings_button=Button(self.taskbar_frame, text="Settings", width=4, height=1, command=exit)
        self.settings_button.place(x=260, y=10)

        self.window.mainloop()