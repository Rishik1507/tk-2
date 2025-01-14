from tkinter import *
from tkinter import messagebox
w=Tk()
w.title("Images in Tkinter")
w.geometry("400x400")
def msg():
    messagebox.showwarning("Alert!","Virus Detected")
def top():
    t=Toplevel()
    t.geometry("400x300")
    t.title("New Window")
    lb=Label(t,text="This is the new window..", fg="cyan")
    lb.pack()
    t.mainloop()
button=Button(w,text="Virus Detector",  command=msg)
btn=Button(w,text="Click for new window", command=top)
btn.pack()
button.place(x=40,y=40)

w.mainloop()
