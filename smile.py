from tkinter import *
def lisa_nina():
    if var_nina.get()=="nina":
        lbl.configure(text="")
    elif var_nina.get()=="tühi":
        lbl.configure(text="On vaja nina kustutada ära")
def lisa_s():
    if var_suu.get()=="suu":
        vastus.configure(text="Lisame suu canva peale")
    else:
        vastus.configure(text="On vaja suu kunstutada ära")
def lisa_nao():
    if var_nao.get()=="Nägu":
        c.create_oval((10, 10, 490, 490), fill="#cc99cc", outline="black") #лицо
    elif var_nao.get()=="tühi":
        c.create_oval((10, 10, 490, 490), fill="#cc99cc", outline="#cc99cc") #лицо
tk = Tk()
tk.title("ruuvõrrend")
var_nina=StringVar()
f1=Frame(tk,width=500,height=500)
f1.pack(side=TOP)
f2=Frame(tk,width=500,height=500)
f2.pack(side=BOTTOM)
c=Canvas(tk, width=500, height=500, bg="white")
c.pack()
nina=Checkbutton(f1,text = "нос", variable=var_nina,onvalue="nina",offvalue="tühi",command=lisa_nina)
nina.pack()
var_s=StringVar()
suu=Checkbutton(f1,text = "suu",font="Arial 20",command=lisa_s)
suu.pack()
c3=Checkbutton(f1,text = "глаза",font="Arial 20",command=...)
c3.pack()
c4=Checkbutton(f1,text = "нос",font="Arial 20",command=...)
c4.pack()
c5=Checkbutton(f1,text = "рот",font="Arial 20",command=...)
c5.pack()
var=IntVar
c.create_oval((0,0,250,250))
c.create_oval((0,40,100,100))
c.create_oval((0,40,100,100))
tk.mainloop()