import tkinter
from tkinter import*

window=Tk()
window.title("My first GUI")  #title
window.geometry("500x500") #sizeof window (width x height)
window.minsize(500,500) #minimum width X height
window.maxsize(500,500) #maximum width X height
window.config(bg='red') #configure bg color

window.mainloop()
