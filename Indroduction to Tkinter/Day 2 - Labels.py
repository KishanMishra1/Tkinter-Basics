import tkinter
from tkinter import *

window=Tk()
window.title('My first GUI')
window.geometry("250x250")

#Adding a label
#Features=Background,foreground,borderwidth,relief,font

label1=Label(window,text="Hello",font=("Helvetica",20,"bold"),
             fg="red",bg="black",width=250,height=250,relief='solid')

#position

#label1.pack(anchor='w','e','nw','ne'..) #direction
#label1.pack(padx=100) #padd 100 both sides
#lable.pack(fill=X)#fill entire horizontal axis y- vertical axis
label1.pack()

#Features=Background,foreground,borderwidth,relief,font


window.mainloop()
