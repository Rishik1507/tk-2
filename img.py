from tkinter import *
from PIL import Image,ImageTk
w=Tk()
w.title("Images in Tkinter")
w.geometry("400x400")
up=Image.open("ima.jpg")
image=ImageTk.PhotoImage(up)
lb=Label(text="This is an image..", image=image, height=300, width=300)
l=Label(text="This is an image..")
l.pack()
lb.pack()
w.mainloop()
