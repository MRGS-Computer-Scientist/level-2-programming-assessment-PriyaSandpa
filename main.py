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

hello_label=Label(text="Hello World!")
window.mainloop()