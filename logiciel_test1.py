from tkinter import*
from time import*

fenetre = Tk()

fenetre.title("La multiplication par 10, 100, 1000, ...")

fenetre.geometry('300x200')

def changestate1(win,i,event=None):
    if P[i] == 0:
        if win['text'] == "":
            win['text'] = ","
            win['relief'] = FLAT
        elif win['text'] == ",":
            win['text'] = ""
            win['relief'] = RIDGE

def changestate(win,i,event=None):
    if win['text'] == ",":
        win['relief'] = FLAT
        for n in wins:
            if n != win:
                n['relief'] = RIDGE
                n['text'] = ""
        P[i]=1
        for j in range (len(P)):
            if j != i :
                P[j]=0
    elif win['text'] == "":
        win['relief'] = RIDGE
        P[i]=0

P=[0,0,0]
frame1=Frame(fenetre)
frame1.pack()
Frame(fenetre).pack()
frame2=Frame(frame1,borderwidth=3,relief=RIDGE)
frame2.pack(side=RIGHT)
frame3=Frame(frame1,borderwidth=3,relief=GROOVE)
frame3.pack(side=LEFT)
Label(frame2,text="oui").pack(padx=10,pady=10)
Label(frame3,text="non").pack(padx=10,pady=10)
label=Label(fenetre,text="",borderwidth=3,relief=RIDGE,width=2,height=1)
label.pack()
label2=Label(fenetre,text="",borderwidth=3,relief=RIDGE,width=2,height=1)
label2.pack()
label3=Label(fenetre,text="",borderwidth=3,relief=RIDGE,width=2,height=1)
label3.pack()

label.bind("<Enter>",func=lambda x:changestate1(label,0))
label.bind("<Leave>",func=lambda x:changestate1(label,0))
label.bind("<Button>",func=lambda x:changestate(label,0))
label2.bind("<Enter>",func=lambda x:changestate1(label2,1))
label2.bind("<Leave>",func=lambda x:changestate1(label2,1))
label2.bind("<Button>",func=lambda x:changestate(label2,1))
label3.bind("<Enter>",func=lambda x:changestate1(label3,2))
label3.bind("<Leave>",func=lambda x:changestate1(label3,2))
label3.bind("<Button>",func=lambda x:changestate(label3,2))
wins=[label,label2,label3]

fenetre.mainloop()
