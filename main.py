from tkinter import *

w_width= 360
w_height= 675

window=Tk()
window.geometry(str(w_width) +"x"+ str(w_height))
window.title("My App")

main_frame = Frame(background="#F7EDE2", width=w_width, height=w_height)
main_frame.pack()

hello_label=Label(text="Hello World!")
window.mainloop()