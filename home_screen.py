from tkinter import *
from app_settings import *
from os import *
from PIL import Image, ImageTk

class App():
    current_frame="Home"
    def __init__(self):
        self.window=Tk()
        self.window.geometry(str(w_width) +"x"+ str(w_height))
        self.window.title("My App")
#--Image Icons-------------------------------------------------------------------
        image_home=Image.open("images/Home.png")
        home_icon=ImageTk.PhotoImage(image_home.resize((30,30)))
        image_stats=Image.open("images/Stats.png")
        stats_icon=ImageTk.PhotoImage(image_stats.resize((25,25)))
        image_settings=Image.open("images/Settings.png")
        settings_icon=ImageTk.PhotoImage(image_settings.resize((25,25)))
        image_help=Image.open("images/Help.png")
        help_icon=ImageTk.PhotoImage(image_help.resize((40,40)))      
#--Home--------------------------------------------------------------------------
        self.home_frame = Frame(background=main_bg_standard, 
                                    width=w_width, 
                                    height=675)
        self.home_frame.pack()
        self.home_frame.pack_propagate(False)
        self.home_label=Label(self.home_frame,
                                  text="Home", 
                                  font="Verdana 30", 
                                  background=main_bg_standard)
        self.home_label.pack()
#--Stats-------------------------------------------------------------------------        
        self.stats_frame = Frame(background=main_bg_standard, 
                                    width=w_width, 
                                    height=675)
        self.stats_frame.pack_forget()
        self.stats_frame.pack_propagate(False)
        self.stats_label=Label(self.stats_frame,
                                  text="Stats", 
                                  font="Verdana 30", 
                                  background=main_bg_standard)
        self.stats_label.pack()
#--Settinga----------------------------------------------------------------------        
        self.settings_frame = Frame(background=main_bg_standard, 
                                    width=w_width, 
                                    height=675)
        self.settings_frame.pack_forget()
        self.settings_frame.pack_propagate(False)
        self.settings_label=Label(self.settings_frame,
                                  text="Settings", 
                                  font="Verdana 30", 
                                  background=main_bg_standard)
        self.settings_label.pack()
#--Taskbar-----------------------------------------------------------------------
        self.taskbar_frame=Frame(background=taskbar_bg_standard, 
                                 width=w_width, 
                                 height=50)
        self.taskbar_frame.place(x=0, y=w_height-50)

        self.home_button=Button(self.taskbar_frame, 
                                 image=home_icon, 
                                 background=taskbar_bg_standard, 
                                 width=30, height=30, 
                                 highlightthickness=0, 
                                 bd=0, 
                                 command=lambda: self.go_to_frame("Home"), 
                                 activebackground=taskbar_bg_standard)
        self.home_button.place(x=165, y=10)

        self.stats_button=Button(self.taskbar_frame, 
                                 image=stats_icon, 
                                 background=taskbar_bg_standard, 
                                 width=30, height=30, 
                                 highlightthickness=0, 
                                 bd=0, 
                                 command=lambda: self.go_to_frame("Stats"), 
                                 activebackground=taskbar_bg_standard)
        self.stats_button.place(x=55, y=10)

        self.settings_button=Button(self.taskbar_frame, 
                                    image=settings_icon, 
                                    background=taskbar_bg_standard, 
                                    width=30, height=30, 
                                    highlightthickness=0, 
                                    bd=0, 
                                    command=lambda: self.go_to_frame("Settings"), 
                                    activebackground=taskbar_bg_standard)
        self.settings_button.place(x=275, y=10)
#--Help Button-------------------------------------------------------------------
        self.help_button_1=Button(self.home_frame, 
                                image=help_icon, 
                                background=main_bg_standard, 
                                width=40, height=40, 
                                highlightthickness=0, 
                                bd=0, border=0, 
                                activebackground=main_bg_standard)
        self.help_button_1.place(x=310, y=15)

        self.help_button_2=Button(self.stats_frame, 
                                image=help_icon, 
                                background=main_bg_standard, 
                                width=40, height=40, 
                                highlightthickness=0, 
                                bd=0, border=0, 
                                activebackground=main_bg_standard)
        self.help_button_2.place(x=310, y=15)

        self.help_button_3=Button(self.settings_frame, 
                                image=help_icon, 
                                background=main_bg_standard, 
                                width=40, height=40, 
                                highlightthickness=0, 
                                bd=0, border=0, 
                                activebackground=main_bg_standard)
        self.help_button_3.place(x=310, y=15)
#--Mainloop----------------------------------------------------------------------
        self.window.mainloop()
    
    def go_to_frame(self, next_frame):

        if self.current_frame == "Home":
                self.home_frame.pack_forget()
        elif self.current_frame == "Stats":
                self.stats_frame.pack_forget()
        elif self.current_frame == "Settings":
                self.settings_frame.pack_forget()
        
        if next_frame == "Stats":
                self.stats_frame.pack()
                self.current_frame = "Stats"
        elif next_frame == "Settings":
                self.settings_frame.pack()
                self.current_frame = "Settings"
        elif next_frame == "Home":
                self.home_frame.pack()
                self.current_frame = "Home"

if __name__=="__main__":
    app=App()
