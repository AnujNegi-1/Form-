#from tkinter import *
import tkinter as tk
from tkinter import ttk
a=tk.Tk()
a.geometry("1000x1000")
a.resizable(False,False)
a.title("First Code")
tk.Label(a,text="User Form", font="Algerian 25",bg="dark red",fg="white").pack(fill="both")

tk.Label(a,text="Name", font="Algerian 16",fg="black").place(x=120,y=125)
tk.Label(a,text="Class", font="algerian 16", fg="black").place(x=120, y=225)
tk.Label(a,text="Session", font="algerian 16", fg="black").place(x=320, y=225)
tk.Label(a,text="School Name", font="algerian 16", fg="black").place(x=570, y=225)
tk.Label(a,text="Contact No.", font="algerian 16", fg="black").place(x=120, y=275)
tk.Label(a,text="Blood Group", font="algerian 16", fg="black").place(x=450, y=275)
tk.Label(a,text='Mail', font='algerian 16', fg='black').place(x=120,y=325)


#checkbutton

def cbb():
    if(m.get()==1):
        x='Math'
    if(e.get()==1):
        x='English'
    if(h.get()==1):
        x='Hindi'
    if(x==' '):
        print('Select one')
    else:
        print(x)


nm=tk.StringVar()
nm1=tk.StringVar()
cl=tk.StringVar()
cl1=tk.StringVar()
se=tk.StringVar()
se1=tk.StringVar()
scl=tk.StringVar()
cn=tk.StringVar()
bg=tk.StringVar()
mai=tk.StringVar()
m = tk.IntVar()
e = tk.IntVar()
h = tk.IntVar()

#checkbutton
cb = tk.Checkbutton(a,text='Math',font='algerian 16',fg='black',variable=m, command=cbb).place(x=120,y=375)
cb1 = tk.Checkbutton(a,text='English',font='algerian 16',fg='black',variable=e, command=cbb).place(x=120,y=405)
cb2 = tk.Checkbutton(a,text='Hindi',font='algerian 16',fg='black',variable=h, command=cbb).place(x=120,y=430)


#Combobox

#Name
nm=tk.StringVar()
name = ttk.Combobox(a, width = 10, textvariable = nm)
name['values'] = (' Mr'
                  ' Ms'
                  ' Mrs')

name.place(x=220,y=125)
name.current()

nm1=tk.Entry(a,bd="2",textvariable=nm1)
nm1.place(x=400,y=125)

#Class
cl=tk.StringVar()
clas = ttk.Combobox(a, width = 10, textvariable = cl)
clas['values'] = (' 10th'
                   ' 12th')

clas.place(x=210,y=225)
clas.current()

#Session
se=tk.StringVar()
session = ttk.Combobox(a, width = 10, textvariable = se)
session['values'] = (' 1998-1999'
                     ' 1999-2000'
                     ' 2000-2001'
                     ' 2001-2002'
                     ' 2002-2003'
                     ' 2003-2004'
                     ' 2004-2005'
                     ' 2005-2006'
                     ' 2006-2007'
                     ' 2007-2008')
                     
session.place(x=460,y=225)
session.current()

#School Label
scl1=tk.Entry(a,bd='3',textvariable=cn)
scl1.place(x=740,y=225)

#Contact N0.
cn1=tk.Entry(a,bd="2",textvariable=cn)
cn1.place(x=300,y=275)

#Blood Group
bg=tk.StringVar()
Blood  = ttk.Combobox(a, width = 10, textvariable = bg)
Blood ['values'] = (' A+'
                    ' B+'
                    ' O+'
                    ' O-'
                    ' AB+'
                    ' AB-')
                     
                     
Blood .place(x=630,y=275)
Blood.current()

#Mail
mai1=tk.Entry(a,bd='2',textvariable=mai)
mai1.place(x=300,y=325)

mainloop()
