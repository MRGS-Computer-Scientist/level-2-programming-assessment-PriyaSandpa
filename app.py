from tkinter import *
import tkinter as tk
from app_settings import *
import customtkinter as ctk
from os import *
from PIL import Image, ImageTk

class App():
    current_frame="Home"
    def __init__(self):
        self.window=Tk()
        self.window.geometry(str(w_width) +"x"+ str(w_height))
        self.window.title("My App")
#--Image Icons--------------------------------------------------------------------
        image_home=Image.open("images/Home.png")
        home_icon=ImageTk.PhotoImage(image_home.resize((30,30)))
        image_stats=Image.open("images/Stats.png")
        stats_icon=ImageTk.PhotoImage(image_stats.resize((25,25)))
        image_settings=Image.open("images/Settings.png")
        settings_icon=ImageTk.PhotoImage(image_settings.resize((25,25)))
        image_help=Image.open("images/Help.png")
        help_icon=ImageTk.PhotoImage(image_help.resize((40,40))) 
        image_add=Image.open("images/Add.png")
        add_icon=ImageTk.PhotoImage(image_add.resize((50,50)))
        image_exit=Image.open("images/Exit.png")
        exit_icon=ImageTk.PhotoImage(image_exit.resize((40,40)))     
#--Home Screen--------------------------------------------------------------------
        #Home-Frame
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
        
        #ProgressBar
        def clicker():
               self.progress_bar.step()
               self.progress.configure(text=(int(self.progress_bar.get()*100),"%"))

        self.progress_bar=ctk.CTkProgressBar(self.home_frame,
                                             determinate_speed=5.01,
                                             width=w_width-100,
                                             height=15,
                                             fg_color=help_bg_standard,
                                             progress_color="#84A59D",
                                             border_color="#D9D9D9",
                                             border_width=1)
        self.progress_bar.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.progress_bar.set(0)
        self.progress=Label(self.home_frame, text="", font=("Helvetica", 45))
        self.progress.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.test_button=Button(self.home_frame, text="Click Me", command=clicker)
        self.test_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        
#--Stats Screen------------------------------------------------------------------       
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
#--Settings Screen---------------------------------------------------------------       
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
#--Help Screen-------------------------------------------------------------------
        self.help_frame=Frame(background=help_bg_standard,
                              width=w_width,
                              height=w_height)
        self.help_frame.pack_forget()
        self.help_frame.pack_propagate(False)
        self.help_label=Label(self.help_frame,
                              text="Help",
                              font="Verdana 30",
                              background=help_bg_standard)
        self.help_label.pack()
#--Taskbar-----------------------------------------------------------------------
        self.taskbar_frame=Frame(background=taskbar_bg_standard, 
                                 width=w_width, 
                                 height=50)
        self.taskbar_frame.place(relx=0.5, rely=0.9635, anchor=tk.CENTER)

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
#--Add Task Screen---------------------------------------------------------------
        self.addtask_frame=Frame(background=help_bg_standard,
                                 width=w_width,
                                 height=w_height)
        self.addtask_frame.pack_forget()
        self.addtask_frame.pack_propagate(False)
        self.addtask_label=Label(self.addtask_frame,
                                 text="Add Task",
                                 font="Verdana 30",
                                 background=help_bg_standard)
        self.addtask_label.pack()
        self.add_task=Entry(self.addtask_frame,
                            background="#D3D3D3",
                            bd=0,
                            width=45,
                            highlightthickness=0)
        self.add_task.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        self.addtask_button=Button(self.home_frame,
                                   background=main_bg_standard, 
                                   image=add_icon,
                                   width=50, height=50, 
                                   highlightthickness=0, 
                                   bd=0, border=0, 
                                   activebackground=main_bg_standard,   
                                   command=lambda: self.go_to_frame("Add"))
        self.addtask_button.place(x=295, y=w_height-115)
#--Help Buttons-------------------------------------------------------------------
        self.help_button_1=Button(self.home_frame, 
                                  image=help_icon, 
                                  background=main_bg_standard, 
                                  width=40, height=40, 
                                  highlightthickness=0, 
                                  bd=0, border=0, 
                                  activebackground=main_bg_standard,
                                  command=lambda: self.go_to_frame("Help"))
        self.help_button_1.place(x=310, y=15)

        self.help_button_2=Button(self.stats_frame, 
                                  image=help_icon, 
                                  background=main_bg_standard, 
                                  width=40, height=40, 
                                  highlightthickness=0, 
                                  bd=0, border=0, 
                                  activebackground=main_bg_standard,
                                  command=lambda: self.go_to_frame("Help"))
        self.help_button_2.place(x=310, y=15)

        self.help_button_3=Button(self.settings_frame, 
                                  image=help_icon, 
                                  background=main_bg_standard, 
                                  width=40, height=40, 
                                  highlightthickness=0, 
                                  bd=0, border=0, 
                                  activebackground=main_bg_standard,
                                  command=lambda: self.go_to_frame("Help"))
        self.help_button_3.place(x=310, y=15)
#--Exit Button-------------------------------------------------------------------
        self.exit_button_help=Button(self.help_frame,
                                image=exit_icon, 
                                background=help_bg_standard, 
                                width=40, height=40, 
                                highlightthickness=0, 
                                bd=0, border=0, 
                                activebackground=help_bg_standard,
                                command=lambda: self.go_to_frame("Home"))
        self.exit_button_help.place(x=30, y=15)
        self.exit_button_add=Button(self.addtask_frame,
                                image=exit_icon, 
                                background=help_bg_standard, 
                                width=40, height=40, 
                                highlightthickness=0, 
                                bd=0, border=0, 
                                activebackground=help_bg_standard,
                                command=lambda: self.go_to_frame("Home"))
        self.exit_button_add.place(x=30, y=15)
#--Mainloop----------------------------------------------------------------------
        self.window.mainloop()
#--Go to frame function----------------------------------------------------------  
    def go_to_frame(self, next_frame):

        if self.current_frame == "Home":
                self.home_frame.pack_forget()
        elif self.current_frame == "Stats":
                self.stats_frame.pack_forget()
        elif self.current_frame == "Settings":
                self.settings_frame.pack_forget()
        elif self.current_frame == "Help":
              self.help_frame.pack_forget()
              self.taskbar_frame.place(relx=0.5, rely=0.9635, anchor=tk.CENTER)
        elif self.current_frame == "Add":
              self.addtask_frame.pack_forget()
              self.taskbar_frame.place(relx=0.5, rely=0.9635, anchor=tk.CENTER)
        
        if next_frame == "Stats":
                self.stats_frame.pack()
                self.current_frame = "Stats"
        elif next_frame == "Settings":
                self.settings_frame.pack()
                self.current_frame = "Settings"
        elif next_frame == "Home":
                self.home_frame.pack()
                self.current_frame = "Home"
        elif next_frame == "Help":
                self.help_frame.pack()
                self.current_frame="Help"
                self.taskbar_frame.place_forget()
        elif next_frame == "Add":
                self.addtask_frame.pack()
                self.current_frame="Add"
                self.taskbar_frame.place_forget()

if __name__=="__main__":
    app=App()
