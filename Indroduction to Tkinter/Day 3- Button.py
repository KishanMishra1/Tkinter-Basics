from tkinter import *

window=Tk()
window.title(" Interface 01")
window.geometry("250x250")

def do():
    Name=name_entry.get()
    Sic=sic_entry.get()
    PhoneNo=phone_entry.get()

    window2=Tk()
    l1=Label(window2,text=("Name:"+Name))
    l1.pack()
    l2=Label(window2,text=("Sic No:"+Sic))
    l2.pack()
    l3=Label(window2,text=("Phone No:"+"+91-"+PhoneNo))
    l3.pack()
    

    window.destroy()
    window2.mainloop()

#************Name***********

name_label=Label(window,text="Name:")
name_label.pack(anchor="w")

name_entry=Entry(window)
name_entry.pack(anchor="w")

#************SIC***********

sic_label=Label(window,text="SIC No:")
sic_label.pack(anchor="w")

sic_entry=Entry(window)
sic_entry.pack(anchor="w")

#************Phone***********

phone_label=Label(window,text="Phone No:")
phone_label.pack(anchor="w")

phone_entry=Entry(window)
phone_entry.pack(anchor="w")

#Adding Button

Button1=Button(window,text="Submit",command=do)
Button1.pack()

window.mainloop()
