from tkinter import *
from app_settings import *
from os import *
from PIL import Image, ImageTk

class App():
    def __init__(self):
        self.window=Tk()
        self.window.geometry(str(w_width) +"x"+ str(w_height))
        self.window.title("My App")
        
        image_home=Image.open("images/Home.png")
        home_icon=ImageTk.PhotoImage(image_home.resize((30,30)))
        image_stats=Image.open("images/Stats.png")
        stats_icon=ImageTk.PhotoImage(image_stats.resize((25,25)))
        image_settings=Image.open("images/Settings.png")
        settings_icon=ImageTk.PhotoImage(image_settings.resize((25,25)))


        self.main_frame = Frame(background="#F7EDE2", width=w_width, height=625)
        self.main_frame.pack()
        self.main_frame.pack_propagate(False)

        self.taskbar_frame=Frame(background="#F6BD60", width=w_width, height=50)
        self.taskbar_frame.pack()
        self.taskbar_frame.pack_propagate(False)

        self.home_button=Button(self.taskbar_frame, image=home_icon, background="#F6BD60", width=30, height=30)
        self.home_button.place(x=160, y=7)

        self.stats_button=Button(self.taskbar_frame, image=stats_icon, background="#F6BD60", width=30, height=30, command=exit)
        self.stats_button.place(x=60, y=7)

        self.settings_button=Button(self.taskbar_frame, image=settings_icon, background="#F6BD60", width=30, height=30, command=exit)
        self.settings_button.place(x=260, y=7)

        self.window.mainloop()

if __name__=="__main__":
    app=App()