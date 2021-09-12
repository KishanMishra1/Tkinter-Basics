from tkinter import*
from tkinter import messagebox

window=Tk()

users={ 'user1':'pass1',
        'user2':'pass2',
        'user3':'pass3',
        'user4':'pass4'}

def log_in():
    user=UserEntry.get()
    password=PassEntry.get()
    c=0

    for k,v in users.items():
        if k==user and v== password:
            messagebox.showinfo("Congratulation","Welcome {}".format(k))
            c=1
            break
    if c==0:
        messagebox.showerror("Error","You dont have an accout")
        

Userlabel=Label(window,text='Enter Username:')
Userlabel.pack(anchor='w')
UserEntry=Entry(window)
UserEntry.pack(anchor='w')



Passlabel=Label(window,text='Enter Password:')
Passlabel.pack(anchor='w')
PassEntry=Entry(window)
PassEntry.pack(anchor='w')

button=Button(window,text='Log In',command=log_in)
button.pack()

window.mainloop()
