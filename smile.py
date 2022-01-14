from tkinter import *

def lisa_nina():
    if var_nina.get()=="Nina":
        c.create_oval((135, 147, 165, 183),width=3, fill="#000000", outline="#ffffff") #нос
    elif var_nina.get()=="tühi":
        c.create_oval((135, 135, 165, 165),width=3, fill="#000000", outline="#ffffff") #нос
def lisa_suu():
    if var_suu.get()=="Suu":
        c.create_arc((100, 50, 400,400),start=180,extent=180, style=ARC, fill="#000000",width=10, outline="#000000")
    elif var_suu.get()=="tühi":
        c.create_arc((100, 50, 400,400),start=180,extent=180, style=ARC,   fill="#ffffff",width=10, outline="#ffffff")
def lisa_eyes():
    if var_eyes.get()=="Silmad":
        c.create_oval((240, 140, 260, 100), fill="#000000", outline="#000000") #првый 
        c.create_oval((100, 125, 175, 175), fill="#000000", outline="#000000") #првый 
    elif var_eyes.get()=="tühi":
        c.create_oval((250, 125, 400, 200),  fill="#ffffff", outline="#ffffff") #првый 
        c.create_oval((200, 200, 100, 100),  fill="#ffffff", outline="#ffffff") #левый 
def lisa_nao():
    if var_nao.get()=="Nägu":
        c.create_oval((20, 100, 392, 392),width=5, fill="#ffffff", outline="#000000") #лицо
    elif var_nao.get()=="tühi":
        c.create_oval((20, 100, 392, 392),width=5, fill="#ffffff", outline="#000000") #лицо
aken=Tk()
aken.title("Face")
aken.geometry('1000x500')
aken.configure(bg="#ffffff")
aken.grab_set()  
c = Canvas(aken, width=500, height=500, bg="#ffffff")
var_nina=StringVar()
ch_nina=Checkbutton(aken,text="Nina", variable=var_nina, onvalue="Nina", offvalue="tühi",bg="lightsteelblue",command=lisa_nina)
ch_nina.pack(side=LEFT)
var_suu=StringVar()
ch_suu=Checkbutton(aken,text="Suu", variable=var_suu, onvalue="Suu", offvalue="tühi",bg="lightsteelblue",command=lisa_suu)
ch_suu.pack(side=LEFT)
var_eyes=StringVar()
ch_eyes=Checkbutton(aken,text="Silmad", variable=var_eyes, onvalue="Silmad", offvalue="tühi",bg="lightsteelblue",command=lisa_eyes)
ch_eyes.pack(side=LEFT)
var_nao=StringVar()
ch_nao=Checkbutton(aken,text="Nägu", variable=var_nao, onvalue="Nägu", offvalue="tühi",bg="lightsteelblue",command=lisa_nao)
ch_nao.pack(side=LEFT)
c.pack(side=RIGHT)
aken.mainloop()