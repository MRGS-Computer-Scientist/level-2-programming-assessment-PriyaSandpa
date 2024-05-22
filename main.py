from tkinter import *

w_width= 360
w_height= 675

window=Tk()
window.geometry(str(w_width) +"x"+ str(w_height))
window.title("My App")

main_frame = Frame(background="#F7EDE2", width=w_width, height=625)
main_frame.pack()

taskbar_frame=Frame(background="#F6BD60", width=w_width, height=50)
taskbar_frame.pack()

home_button=Button(taskbar_frame, text="Home", width=4, height=1)
home_button.place(x=160, y=10)

stats_button=Button(taskbar_frame, text="Stats", width=4, height=1)
stats_button.place(x=60, y=10)

settings_button=Button(taskbar_frame, text="Settings", width=4, height=1)
settings_button.place(x=260, y=10)

window.mainloop()