from tkinter import *
from tkinter import ttk
a=Tk()
a.geometry("1000x1000")
a.resizable(False,False)
a.title("First Code")
Label(a,text="User Form", font="Algerian 25",bg="dark red",fg="white").pack(fill="both")

Label(a,text="Name", font="Algerian 16",fg="black").place(x=120,y=125)
Label(a,text="Clas", font="algerian 16", fg="black").place(x=120, y=225)
Label(a,text="Session", font="algerian 16", fg="black").place(x=320, y=225)
Label(a,text="School Name", font="algerian 16", fg="black").place(x=570, y=225)
Label(a,text="Contact No.", font="algerian 16", fg="black").place(x=120, y=275)
Label(a,text="Blood Group", font="algerian 16", fg="black").place(x=450, y=275)


nm=StringVar()
nm1=StringVar()
cl=StringVar()
cl1=StringVar()
se=StringVar()
se1=StringVar()
scl=StringVar()
cn=StringVar()
bg=StringVar()
#Combobox

#Name
nm=StringVar()
name = ttk.Combobox(a, width = 10, textvariable = nm)
name['values'] = (' Mr'
                  ' Ms'
                  ' Mrs')

name.place(x=220,y=125)
name.current()

nm1=Entry(a,bd="2",textvariable=nm1)
nm1.place(x=400,y=125)

#Class
cl=StringVar()
clas = ttk.Combobox(a, width = 10, textvariable = cl)
clas['values'] = (' 10th'
                   ' 12th')

clas.place(x=210,y=225)
clas.current()

#Session
se=StringVar()
session = ttk.Combobox(a, width = 10, textvariable = se)
session['values'] = (' 1998'
                     ' 1999'
                     ' 2000'
                     ' 2001'
                     ' 2002'
                     ' 2003'
                     ' 2004'
                     ' 2005'
                     ' 2006'
                     ' 2007')
                     
session.place(x=460,y=225)
session.current()

#School Label
scl1=Entry(a,bd='3',textvariable=cn)
scl1.place(x=740,y=225)

#Contact N0.
cn1=Entry(a,bd="2",textvariable=cn)
cn1.place(x=300,y=275)

#Blood Group
bg=StringVar()
Blood  = ttk.Combobox(a, width = 10, textvariable = bg)
Blood ['values'] = (' A+'
                    ' B+'
                    ' O+'
                    ' O-'
                    ' AB+'
                    ' AB-')
                     
                     
Blood .place(x=630,y=275)
Blood.current()
mainloop()
