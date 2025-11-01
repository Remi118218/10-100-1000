#Début


from tkinter import*
from time import*
from math import*
from random import*

fenetre = Tk()
fenetre.title("La multiplication par 10, 100, 1000, ...")

global value
global labelmincepacked
labelmincepacked=False

#Fonctions

def printok(event=None):
    print("ok")

def erreur(texte):
    erreurf=Toplevel(fenetre)
    erreurf.focus_set()
    erreurf.bind("<Return>",func=lambda x:Destroy(erreurf))
    erreurf.title("erreur")
    erreurf.geometry("400x100")
    erreurf.resizable(False,False)
    Label(erreurf,text=texte).pack(pady=10)
    Button(erreurf,text="Valider et Quitter",command=erreurf.destroy).pack()

def Destroy(win):
    win.destroy()

def quitter(event):
    quitterf=Toplevel(fenetre)
    quitterf.focus_set()
    quitterf.bind("<Return>",func=lambda x:Destroy(fenetre))
    quitterf.title("Voulez-vous vraiment quitter ?")
    quitterf.geometry("300x100")
    quitterf.resizable(False,False)
    Label(quitterf,text="Voulez-vous vraiment quitter ?").pack(pady=10)
    Button(quitterf,text="Valider et Quitter",command=fenetre.destroy).pack()

def multi(event=None):
    value3p2.set(valuep1.get())
    value2p2.set(str(float(value2p2.get())*10))
    if value%1==0.5 and float(value2p2.get())==0.0001:
        value3p2.set(10*ceil(value))
    elif value%1>0 and float(value2p2.get())==0.001:
        value3p2.set(10*round(10*value))
    if float(floor(float(value2p2.get()))) == float(value2p2.get()):
        value2p2.set(str(float(floor(float(value2p2.get())))))
    if float(value2p2.get()) > 10000:
        erreur("Ce jeu est limité à 10000")
        value2p2.set("10000")
    else:
        if value-value%1==0 and float(value2p2.get())>1:
            valuep1.set(valuep1.get().replace("0",""))
        value1p2.set(" x"+value2p2.get()+" ")
        pu.set(str(float(pu.get())-150))
        canvasp2.delete('number')
        pos=[]
        p.set(pu.get())
        pos.append(float(pu.get()))
        num=[0,0,0,0]
        for i in range (len(value3p2.get())):
            num[i]=canvasp2.create_text(float(p.get()),145,text=value3p2.get()[len(value3p2.get())-i-1],font="Arial 20",fill='black',tags='number')
            pos.append(float(p.get()))
            if float(p.get())<225:
                p.set(str(float(p.get())-15))
            else:
                p.set(str(float(p.get())-150))
        if 675 not in pos:
            p.set("675")
            if max(pos)<675:
                while float(p.get())>max(pos):
                    num.append(canvasp2.create_text(float(p.get()),145,text="0",font="Arial 20",fill='black',tags='number'))
                    p.set(str(float(p.get())-150))
            if min(pos)>675:
                while float(p.get())<min(pos):
                    num.append(canvasp2.create_text(float(p.get()),145,text="0",font="Arial 20",fill='black',tags='number'))
                    p.set(str(float(p.get())+150))

def div(event=None):
    value3p2.set(valuep1.get())
    value2p2.set(str(float(value2p2.get())/10))
    if value%1==0.5 and float(value2p2.get())==0.0001:
        value3p2.set(ceil(value))
    elif value%1>0 and 10*value%1 and float(value2p2.get())==0.001:
        value3p2.set(10*round(10*value))
    if float(floor(float(value2p2.get()))) == float(value2p2.get()):
        value2p2.set(str(float(floor(float(value2p2.get())))))
    if float(value2p2.get()) < 0.0001:
        erreur("Ce jeu est limité à 0.0001")
        value2p2.set("0.0001")
    else:
        value1p2.set(" x"+value2p2.get()+" ")
        pu.set(str(float(pu.get())+150))
        canvasp2.delete('number')
        pos=[]
        p.set(pu.get())
        pos.append(float(pu.get()))
        num=[0,0,0,0]
        for i in range (len(value3p2.get())):
            print(p.get(), value3p2.get()[len(value3p2.get())-i-1])
            num[i]=canvasp2.create_text(float(p.get()),145,text=value3p2.get()[len(value3p2.get())-i-1],font="Arial 20",fill='black',tags='number')
            pos.append(float(p.get()))
            if float(p.get())<225:
                p.set(str(float(p.get())-15))
            else:
                p.set(str(float(p.get())-150))
        if 675 not in pos:
            p.set("675")
            if max(pos)<675:
                while float(p.get())>max(pos):
                    num.append(canvasp2.create_text(float(p.get()),145,text="0",font="Arial 20",fill='black',tags='number'))
                    p.set(str(float(p.get())-150))
            if min(pos)>675:
                while float(p.get())<min(pos):
                    num.append(canvasp2.create_text(float(p.get()),145,text="0",font="Arial 20",fill='black',tags='number'))
                    p.set(str(float(p.get())+150))

def Exo1(Event=None):
    value3p3.set(value1p3.get())
    print(value3p3.get(),",",value1p3.get())
    n=0
    while Po[n].get()!=',': n=n+1
    if n<3 : value3p3.set("0"+"."+"0"*(2-n)+value3p3.get())
    else:
        value3p3.set(value3p3.get()+"000")
        value3p3.set(value3p3.get()[:n-2]+"."+value3p3.get()[n-2:])
    if(float(value3p3.get())==float(str(value1p3.get()))*float(str(value2p3.get()))):
        labelmince.pack_forget()
        labelbravo.pack(pady=10)
        buttonbravo=Button(fenetre,text="Passer au suivant")
        buttonbravo.pack()
    else:
        labelmince.pack_forget()
        labelmince.pack(pady=10)

# Fonctions d'exercice

def entrer(n):
    if Po[n].get()!=',':
        Po[n].set('.')

def sortir(n):
    if Po[n].get()!=',':
        Po[n].set('\0')

def retour(n):
    if Po[n].get()==',':
        Po[n].set('\0')
    else:
        for i in range (len(Po)):
            if Po[i].get()==',':
                Po[i].set('\0')
        Po[n].set(',')

# Fonction de phases

def phase1():
    valuep1.set('\0')
    labelp1.pack(pady=5)
    entreep1.pack()
    buttonp1.pack(pady=10)
    framep1.pack(expand=True, anchor=CENTER)
    entreep1.focus_set()
    fenetre.bind("<Return>",phase2)
    fenetre.geometry("1200x200")
    fenetre.minsize(1200,150)

def phase2(event=None):
    if valuep1.get() and valuep1.get() != '\0' and float(valuep1.get()) >= 0.01 and float(valuep1.get()) < 1000 and divmod(100*float(valuep1.get()),1)[1]<0.01:
        ######### on enlève les 0 en trop #########
        L=[]
        for i in range (len(valuep1.get())):
            L.append(valuep1.get()[i])
        while L[0]=="0" and L[1]!="." and L[1]!=",":
            del L[0]
        valuep1.set(''.join(L))
        ###########################################
        if int(float(valuep1.get()))==float(valuep1.get()):
            valuep1.set(str(int(float(valuep1.get()))))
        global value
        value=float(valuep1.get())
        num=[]
        ############## fin de phase1 ##############
        framep1.pack_forget()
        labelp1.pack_forget()
        entreep1.pack_forget()
        buttonp1.pack_forget()
        frameEx.pack_forget()
        buttonEx.pack_forget()
        fenetre.unbind("<Return>")
        ###########################################
        fenetre.geometry("1350x400")
        fenetre.minsize(1350,400)
        if 10*float(value)%1>0: # si 0.01 #########
            pu.set(str(675+300))
            p.set(str(float(p.get())+300))
            valuep1.set(valuep1.get().replace(".",""))
            valuep1.set(valuep1.get().replace(",",""))
        elif float(value)%1>0: # si 0.1 ###########
            pu.set(str(675+150))
            p.set(str(float(p.get())+150))
            valuep1.set(valuep1.get().replace(".",""))
            valuep1.set(valuep1.get().replace(",",""))
        else: # si 1 ##############################
            pu.set("675")
        for i in range (len(valuep1.get())):
            num.append(canvasp2.create_text(float(p.get()),145,text=valuep1.get()[len(valuep1.get())-i-1],font="Arial 20",fill='black',tags='number'))
            p.set(str(float(p.get())-150))
        ############# pack de phase 2 #############
        canvasp2.pack()
        frame1p2.pack()
        button1p2.pack(side=LEFT)
        frame2p2.pack(side=LEFT)
        labelp2.pack(anchor=CENTER)
        button2p2.pack(side=RIGHT)
        frameEx.pack(side=RIGHT,pady=10)
        buttonEx.pack(padx=10)
        fenetre.bind("<Left>",multi)
        fenetre.bind("<Right>",div)
    else:
        erreur("Vous devez choisir un nombre plus grand que 0.1 et plus petit que 1000.\nLes nombres décimaux avec plus de deux chiffres après la virgule\nne sont pas acceptés non plus.")

def phase3exo1():'''
    framep1.pack_forget()
    labelp1.pack_forget()
    entreep1.pack_forget()
    buttonp1.pack_forget()
    canvasp2.delete('number')
    canvasp2.pack_forget()
    frame1p2.pack_forget()
    button1p2.pack_forget()
    frame2p2.pack_forget()
    labelp2.pack_forget()
    button2p2.pack_forget()
    frameEx.pack_forget()
    buttonEx.pack_forget()
    label1p3.pack(pady=5)
    label3p3.pack(pady=5)
    for i in range (len(label2p3)):
        label2p3[i].pack(side='left',expand='False')
    framep3.pack()
    value1p2.set(" x1 ")
    value2p2.set("1")
    pu.set("675")
    p.set("675")
    fenetre.unbind("<Return>")
    fenetre.unbind("<Left>")
    fenetre.unbind("<Right>")
    fenetre.bind("<Return>",Exo1)
    label2p3[1].bind("<Enter>",func=lambda x:entrer(0))
    label2p3[3].bind("<Enter>",func=lambda x:entrer(1))
    label2p3[5].bind("<Enter>",func=lambda x:entrer(2))
    label2p3[7].bind("<Enter>",func=lambda x:entrer(3))
    label2p3[9].bind("<Enter>",func=lambda x:entrer(4))
    label2p3[11].bind("<Enter>",func=lambda x:entrer(5))
    label2p3[13].bind("<Enter>",func=lambda x:entrer(6))
    label2p3[1].bind("<Leave>",func=lambda x:sortir(0))
    label2p3[3].bind("<Leave>",func=lambda x:sortir(1))
    label2p3[5].bind("<Leave>",func=lambda x:sortir(2))
    label2p3[7].bind("<Leave>",func=lambda x:sortir(3))
    label2p3[9].bind("<Leave>",func=lambda x:sortir(4))
    label2p3[11].bind("<Leave>",func=lambda x:sortir(5))
    label2p3[13].bind("<Leave>",func=lambda x:sortir(6))
    label2p3[1].bind("<Button>",func=lambda x:retour(0))
    label2p3[3].bind("<Button>",func=lambda x:retour(1))
    label2p3[5].bind("<Button>",func=lambda x:retour(2))
    label2p3[7].bind("<Button>",func=lambda x:retour(3))
    label2p3[9].bind("<Button>",func=lambda x:retour(4))
    label2p3[11].bind("<Button>",func=lambda x:retour(5))
    label2p3[13].bind("<Button>",func=lambda x:retour(6))
    if len(value3p3.get())>1:
        label2p3[15].bind("<Enter>",func=lambda x:entrer(7))
        label2p3[15].bind("<Leave>",func=lambda x:sortir(7))
        label2p3[15].bind("<Button>",func=lambda x:retour(7))
    if len(value3p3.get())>2:
        label2p3[17].bind("<Enter>",func=lambda x:entrer(8))
        label2p3[17].bind("<Leave>",func=lambda x:sortir(8))
        label2p3[17].bind("<Button>",func=lambda x:retour(8))
    if len(value3p3.get())>3:
        label2p3[19].bind("<Enter>",func=lambda x:entrer(9))
        label2p3[19].bind("<Leave>",func=lambda x:sortir(9))
        label2p3[19].bind("<Button>",func=lambda x:retour(9))
    if len(value3p3.get())>4:
        label2p3[21].bind("<Enter>",func=lambda x:entrer(10))
        label2p3[21].bind("<Leave>",func=lambda x:sortir(10))
        label2p3[21].bind("<Button>",func=lambda x:retour(10))
    if len(value3p3.get())>5:
        label2p3[23].bind("<Enter>",func=lambda x:entrer(11))
        label2p3[23].bind("<Leave>",func=lambda x:sortir(11))
        label2p3[23].bind("<Button>",func=lambda x:retour(11))
    if len(value3p3.get())>6:
        label2p3[25].bind("<Enter>",func=lambda x:entrer(12))
        label2p3[25].bind("<Leave>",func=lambda x:sortir(12))
        label2p3[25].bind("<Button>",func=lambda x:retour(12))
    if len(value3p3.get())>7:
        label2p3[27].bind("<Enter>",func=lambda x:entrer(13))
        label2p3[27].bind("<Leave>",func=lambda x:sortir(13))
        label2p3[27].bind("<Button>",func=lambda x:retour(13))
'''
def phase3exo2():'''
    framep1.pack_forget()
    labelp1.pack_forget()
    entreep1.pack_forget()
    buttonp1.pack_forget()
    canvasp2.delete('number')
    canvasp2.pack_forget()
    frame1p2.pack_forget()
    button1p2.pack_forget()
    frame2p2.pack_forget()
    labelp2.pack_forget()
    button2p2.pack_forget()
    frameEx.pack_forget()
    buttonEx.pack_forget()
    label1p3.pack_forget()
    label3p3.pack_forget()
    for i in range (len(label2p3)):
        label2p3[i].pack_forget()
    framep3.pack_forget()
    value1p2.set(" x1 ")
    value2p2.set("1")
    pu.set("675")
    p.set("675")
    fenetre.unbind("<Return>")
    fenetre.unbind("<Left>")
    fenetre.unbind("<Right>")
    fenetre.unbind("<Return>",Exo1)
    label2p3[1].unbind("<Enter>",func=lambda x:entrer(0))
    label2p3[3].unbind("<Enter>",func=lambda x:entrer(1))
    label2p3[5].unbind("<Enter>",func=lambda x:entrer(2))
    label2p3[7].unbind("<Enter>",func=lambda x:entrer(3))
    label2p3[9].unbind("<Enter>",func=lambda x:entrer(4))
    label2p3[11].unbind("<Enter>",func=lambda x:entrer(5))
    label2p3[13].unbind("<Enter>",func=lambda x:entrer(6))
    label2p3[1].unbind("<Leave>",func=lambda x:sortir(0))
    label2p3[3].unbind("<Leave>",func=lambda x:sortir(1))
    label2p3[5].unbind("<Leave>",func=lambda x:sortir(2))
    label2p3[7].unbind("<Leave>",func=lambda x:sortir(3))
    label2p3[9].unbind("<Leave>",func=lambda x:sortir(4))
    label2p3[11].unbind("<Leave>",func=lambda x:sortir(5))
    label2p3[13].unbind("<Leave>",func=lambda x:sortir(6))
    label2p3[1].unbind("<Button>",func=lambda x:retour(0))
    label2p3[3].unbind("<Button>",func=lambda x:retour(1))
    label2p3[5].unbind("<Button>",func=lambda x:retour(2))
    label2p3[7].unbind("<Button>",func=lambda x:retour(3))
    label2p3[9].unbind("<Button>",func=lambda x:retour(4))
    label2p3[11].unbind("<Button>",func=lambda x:retour(5))
    label2p3[13].unbind("<Button>",func=lambda x:retour(6))
    if len(value3p3.get())>1:
        label2p3[15].unbind("<Enter>",func=lambda x:entrer(7))
        label2p3[15].unbind("<Leave>",func=lambda x:sortir(7))
        label2p3[15].unbind("<Button>",func=lambda x:retour(7))
    if len(value3p3.get())>2:
        label2p3[17].unbind("<Enter>",func=lambda x:entrer(8))
        label2p3[17].unbind("<Leave>",func=lambda x:sortir(8))
        label2p3[17].unbind("<Button>",func=lambda x:retour(8))
    if len(value3p3.get())>3:
        label2p3[19].unbind("<Enter>",func=lambda x:entrer(9))
        label2p3[19].unbind("<Leave>",func=lambda x:sortir(9))
        label2p3[19].unbind("<Button>",func=lambda x:retour(9))
    if len(value3p3.get())>4:
        label2p3[21].unbind("<Enter>",func=lambda x:entrer(10))
        label2p3[21].unbind("<Leave>",func=lambda x:sortir(10))
        label2p3[21].unbind("<Button>",func=lambda x:retour(10))
    if len(value3p3.get())>5:
        label2p3[23].unbind("<Enter>",func=lambda x:entrer(11))
        label2p3[23].unbind("<Leave>",func=lambda x:sortir(11))
        label2p3[23].unbind("<Button>",func=lambda x:retour(11))
    if len(value3p3.get())>6:
        label2p3[25].unbind("<Enter>",func=lambda x:entrer(12))
        label2p3[25].unbind("<Leave>",func=lambda x:sortir(12))
        label2p3[25].unbind("<Button>",func=lambda x:retour(12))
    if len(value3p3.get())>7:
        label2p3[27].unbind("<Enter>",func=lambda x:entrer(13))
        label2p3[27].unbind("<Leave>",func=lambda x:sortir(13))
        label2p3[27].unbind("<Button>",func=lambda x:retour(13))
'''
#Phase1

valuep1=StringVar()
framep1=Frame(fenetre)
labelp1=Label(framep1,text="Quel nombre proposez-vous pour la démonstration (entre 0.1 et 1000) ?",font="Arial 20")
entreep1=Entry(framep1, textvariable=valuep1, width=30,font="Arial 10")
valuep1.set(entreep1.get())
entreep1.focus_set()
buttonp1=Button(framep1, text="Valider",command=phase2,font="Arial 15")

#Phase2

L=[]
value1p2=StringVar()
value1p2.set(" x1.0 ")
value2p2=StringVar()
value2p2.set("1")
value3p2=StringVar()
canvasp2 = Canvas(fenetre, width=1350, height=200)
canvasp2.create_text(75,45,text="dix-\nmilliers",font="Arial 20",fill='black')
canvasp2.create_line((150, 0), (150, 200), width=2, fill='black')
canvasp2.create_text(225,45,text="milliers",font="Arial 20",fill='black')
canvasp2.create_line((300, 0), (300, 200), width=2, fill='black')
canvasp2.create_text(375,45,text="centaines",font="Arial 20",fill='black')
canvasp2.create_line((450, 0), (450, 200), width=2, fill='black')
canvasp2.create_text(525,45,text="dizaines",font="Arial 20",fill='black')
canvasp2.create_line((600, 0), (600, 200), width=2, fill='black')
canvasp2.create_text(675,45,text="unité",font="Arial 20",fill='black')
canvasp2.create_line((750, 0), (750, 200), width=2, fill='black')
canvasp2.create_text(825,45,text="dixièmes",font="Arial 20",fill='black')
canvasp2.create_line((900, 0), (900, 200), width=2, fill='black')
canvasp2.create_text(975,45,text="centièmes",font="Arial 20",fill='black')
canvasp2.create_line((1050, 0), (1050, 200), width=2, fill='black')
canvasp2.create_text(1125,45,text="millièmes",font="Arial 20",fill='black')
canvasp2.create_line((1200, 0), (1200, 200), width=2, fill='black')
canvasp2.create_text(1275,45,text="dix-\nmillièmes",font="Arial 20",fill='black')
canvasp2.create_line((0,100), (1350,100), width=2, fill='black')
num=[0,0,0,0]
pos=[]
p=StringVar()
p.set("675")
pu=StringVar()
frame1p2=Frame(fenetre)
photo1=PhotoImage(file = "flechegauche.png")
photo1=photo1.subsample(20, 20)
button1p2=Button(frame1p2, image=photo1,command=multi)
photo2=PhotoImage(file = "flechedroite.png")
photo2=photo2.subsample(20, 20)
button2p2=Button(frame1p2, image=photo2,command=div)
frame2p2=Frame(frame1p2)
frame2p2.pack_propagate(0)
frame2p2.config(width=200,height=50)
labelp2=Label(frame2p2,textvariable=value1p2,font="Arial 40")

#Phase3exo1

label1p3=Label(fenetre,text="Voici un exercice :",font="Arial 20")
value1p3=StringVar()
value1p3.set(str(randint(0,1000)))
value2p3=StringVar()
value2p3.set(str(10**(randint(-3,3))))
value3p3=StringVar()
value3p3.set(value1p3.get())
value4p3=StringVar()
value4p3.set(value1p3.get()+"*"+value2p3.get()+"=")
i=StringVar()
i.set("0")
framep3=Frame(fenetre)

Po=[]
for i in range (int((3*2+len(value3p3.get())*2+3*2)/2)):
    Po.append('0')
label2p3=[]
for i in range (3):
    label2p3.append(Label(framep3,text='0'))
    Po[i]=StringVar()
    Po[i].set('\0')
    label2p3.append(Label(framep3,textvariable=Po[i]))
for i in range(len(value3p3.get())):
    label2p3.append(Label(framep3,text=value3p3.get()[i]))
    Po[i+3]=StringVar()
    Po[i+3].set('\0')
    label2p3.append(Label(framep3,textvariable=Po[i+3]))
for i in range(3):
    label2p3.append(Label(framep3,text='0'))
    Po[i+3+len(value3p3.get())]=StringVar()
    Po[i+3+len(value3p3.get())].set('\0')
    label2p3.append(Label(framep3,textvariable=Po[i+3+len(value3p3.get())]))
label2p3.append(Label(framep3,text='0'))

label3p3=Label(fenetre,textvariable=value4p3,font="Arial 25")

labelmince=Label(fenetre,text="Malheureusement ce n'est pas la bonne réponse, retentez ou demandez un nouvel exercice")
labelbravo=Label(fenetre,text="Bravo vous avez complété cet exercice")

#Menu

menubar=Menu(fenetre)
menu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Explications",command=phase1)
menubar.add_cascade(label="Exercices", command=phase3exo1)
fenetre.config(menu=menubar)

#Erreur

valerr=StringVar()

#Loop

valf=StringVar()
fenetre.bind("<Escape>",quitter)
frameEx=Frame(fenetre)
buttonEx=Button(frameEx,text="Passer aux exercices",font="Arial 15",width=20,height=1,command=phase3exo1)
frameEx.pack(side=BOTTOM,pady=10)
buttonEx.pack(side=RIGHT,padx=10)

phase1()
fenetre.mainloop()

