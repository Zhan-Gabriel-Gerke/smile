from tkinter import *
def lisa_rot():
    if var_rot.get()=="rot":
        c.create_arc((100,-100,400,400),start=180,extent=180, style=ARC, fill="#ffffff",width=10, outline="#ffffff")
    elif var_rot.get()=="tühi":
        c.create_arc((100,-100,400,400),start=180,extent=180, style=ARC,   fill="#000000",width=10, outline="#000000")
def lisa_glaza():
    if var_glaza.get()=="Silmad":
        c.create_oval((125,100,175,150), fill="#000000", outline="#000000") #л
        c.create_oval((250,100,300,150), fill="#000000", outline="#000000") #п
    elif var_glaza.get()=="tühi":
        c.create_oval((250,100,300,150),  fill="#ffffff", outline="#ffffff") #п
        c.create_oval((125,100,175,150),  fill="#ffffff", outline="#ffffff") #л
def lisa_nos():
    if var_nos.get()=="nos":
        c.create_oval((180,200,250,250),width=3, fill="red", outline="red")
    elif var_nos.get()=="tühi":
        c.create_oval((180,200,250,250),width=3, fill="#ffffff", outline="#ffffff") 
def lisa_face():
    if var_face.get()=="Nägu":
        c.create_oval((15,15,450,500),width=5, fill="#ffffff", outline="#000000") 
    elif var_face.get()=="tühi":
        c.create_oval((15,15,450,500),width=5, fill="#ffffff", outline="#ffffff") 
aken=Tk()
aken.title("Face")
aken.geometry('1000x500')
aken.configure(bg="#ffffff")
aken.grab_set()  
c = Canvas(aken, width=500, height=500, bg="#ffffff")
var_nos=StringVar()
var_face=StringVar()
var_rot=StringVar()
var_glaza=StringVar()
ch_nos=Checkbutton(aken,text="nos", variable=var_nos, onvalue="nos", offvalue="tühi",bg="lightsteelblue",command=lisa_nos)
ch_rot=Checkbutton(aken,text="rot", variable=var_rot, onvalue="rot", offvalue="tühi",bg="lightsteelblue",command=lisa_rot)
ch_glaza=Checkbutton(aken,text="Silmad", variable=var_glaza, onvalue="Silmad", offvalue="tühi",bg="lightsteelblue",command=lisa_glaza)
ch_face=Checkbutton(aken,text="Nägu", variable=var_face, onvalue="Nägu", offvalue="tühi",bg="lightsteelblue",command=lisa_face)
ch_face.pack(side=LEFT)
c.pack(side=RIGHT)
ch_rot.pack(side=LEFT)
ch_nos.pack(side=LEFT)
ch_glaza.pack(side=LEFT)
aken.mainloop()