from tkinter import *
import sqlite3

base = sqlite3.connect('Programmes.db')
with base:
    c = base.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS ndp (id INTEGER PRIMARY KEY, nom TEXT)")
Exoskelist=[]
modifieur=0
fen = Tk()
def Base():
    fen.title("AltéroToto Ma Musculation Perso")
    def PMSC():
        global fen
        fen.destroy()
        fen = Tk()
        fen.title("AltéroToto Ma Musculation Perso")
        def Retour():
            global fen
            fen.destroy()
            fen = Tk()
            Base()
        fen_1=Frame(fen)
        fen_1.grid(row=0, column=0)
        fen_2=Frame(fen)
        fen_2.grid(row=0, column=1)
        fen_3=Frame(fen)
        fen_3.grid(row=0, column=2)
        fen_4=Frame(fen)
        fen_4.grid(row=0, column=3)
        ABS = PhotoImage(file='image/Abdos.gif', master=fen_1)
        DOS = PhotoImage(file='image/Dos.gif', master=fen_3)
        PEC = PhotoImage(file='image/Pec.gif', master=fen_2)
        EPAULES = PhotoImage(file='image/Epaules.gif', master=fen_4)
        BCPS = PhotoImage(file='image/Biceps.gif', master=fen_1)
        TCPS = PhotoImage(file='image/Triceps.gif', master=fen_3)
        CNFS = PhotoImage(file='image/Cnfs.gif', master=fen_2)
        MLTS = PhotoImage(file='image/Mollets.gif', master=fen_4)
        BACKI = PhotoImage(file='image/Retour2.gif', master=fen_4)
        BABS=Button(fen_1,text="Abdominaux",command="", image=ABS, bd=0, highlightbackground="black")
        BABS.image = ABS
        BABS.pack()
        BPEC=Button(fen_2,text="Pectoraux",command="", image=PEC, bd=0, highlightbackground="black")
        BPEC.image = PEC
        BPEC.pack()
        BDOS=Button(fen_3,text="Dos",command="", image=DOS, bd=0, highlightbackground="black")
        BDOS.image = DOS
        BDOS.pack()
        BEPAULES=Button(fen_4,text="Epaules",command="", image=EPAULES, bd=0, highlightbackground="black")
        BEPAULES.image = EPAULES
        BEPAULES.pack()
        BBCPS=Button(fen_1,text="Biceps",command="", image=BCPS, bd=0, highlightbackground="black")
        BBCPS.image = BCPS
        BBCPS.pack()
        BTCPS=Button(fen_2,text="Triceps",command="", image=TCPS, bd=0, highlightbackground="black")
        BTCPS.image = TCPS
        BTCPS.pack()
        BCNFS=Button(fen_3,text="Cuisses & Fessiers",command="", image=CNFS, bd=0, highlightbackground="black")
        BCNFS.image = CNFS
        BCNFS.pack()
        BMLTS=Button(fen_4,text="Mollets",command="", image=MLTS, bd=0, highlightbackground="black")
        BMLTS.image = MLTS
        BMLTS.pack()
        BACK=Button(fen_4,text="Mollets",command=Retour, image=BACKI, bd=0, highlightbackground="black")
        BACK.image = BACKI
        BACK.pack()
        VIDE=Label(fen_1, text="")
        VIDE.pack()
        VIDE=Label(fen_2, text="")
        VIDE.pack()
        VIDE=Label(fen_3, text="")
        VIDE.pack()
        
    def PLVL():
        global fen
        fen.destroy()
        fen = Tk()
        fen.title("AltéroToto Ma Musculation Perso")
        def Débutant():
            global fen
            fen.destroy()
            fen = Tk()
            fen.title("AltéroToto Ma Musculation Perso")
            def Ouvrir():
                def Retour():
                    global fen
                    fen.destroy()
                    fen = Tk()
                    Base()
                def Modifier():
                    j=1
                    global Exoskelist
                    Exoskelist=[]
                    while listexos.get(j)!="":
                        Exoskelist.append(listexos.get(j))
                        j=j+1
                    global modifieur
                    modifieur=1
                    global fen
                    fen.destroy()
                    fen = Tk()
                    Base()
                    NPRG()

                PRGN=str(listprg.get(ACTIVE))
                PRGN=PRGN.split()
                PRGN=PRGN[1]
                PRGN2=""
                for j in range(len(PRGN)-1):
                    PRGN2=PRGN2+PRGN[j]
                global fen
                Prgl.destroy()
                listprg.destroy()
                Open.destroy()
                Back.destroy()
                listexos = Listbox(fen_1, width=50, bg="#f0f0f0", borderwidth=0, highlightcolor="#f0f0f0", selectbackground="#f0f0f0", selectforeground="#000000", activestyle="none")
                listexos.pack()
                listexos2 = Listbox(fen_2, bg="#f0f0f0", borderwidth=0, highlightcolor="#f0f0f0", selectbackground="#f0f0f0", selectforeground="#000000", activestyle="none")
                listexos2.pack()
                listexos.insert(END, "N°: Exercices:")
                listexos2.insert(END, "Nr,Ns,Ts,Te")
                Ret = PhotoImage(file='image/Retour2.gif', master=fen_1)
                Mod =  PhotoImage(file='image/Modifier.gif', master=fen_1)
                Modifier=Button(fen_4,text="Modifier",command=Modifier, image=Mod, bd=0)
                Modifier.image = Mod
                Modifier.pack()
                Retour=Button(fen_4,text="Retour",command=Retour, image=Ret, bd=0)
                Retour.image= Ret
                Retour.pack()
                Legend1=Label(fen_3,text="Nr = Nombre de répétition", anchor=W, justify="left")
                Legend1.pack()
                Legend2=Label(fen_3,text="Ns = Nombre de série", anchor=W, justify="left")
                Legend2.pack()
                Legend3=Label(fen_3,text="Ts = Nombre de temps entre chaque séries (en sec)", anchor=W, justify="left", compound="left")
                Legend3.pack()
                Legend4=Label(fen_3,text="Ts = Nombre de temps entre chaque exercices (en sec)", anchor=W, justify="left", compound="left")
                Legend4.pack()
                with base:
                    c = base.cursor()
                    c.execute("SELECT * FROM "+PRGN2)
                    rows = c.fetchall()
                    for row in rows:
                        j=0
                        EXO=str(row)
                        EXO2=""
                        while EXO[j+1]!=",":
                            EXO2=EXO2+EXO[j+1]
                            j=j+1
                        k=j
                        while k<5:
                            EXO2=EXO2+""
                            k=k+1
                        j=j+2
                        while EXO[j]!=",":
                            EXO2=EXO2+EXO[j]
                            j=j+1
                        print(EXO2)
                        EXO3=""
                        j=j+1
                        while j<(len(EXO)-1):
                            EXO3=EXO3+EXO[j]
                            j=j+1
                        print(EXO3)
                        listexos.insert(END, EXO2)
                        listexos2.insert(END, EXO3)
            def Retour():
                global fen
                fen.destroy()
                fen = Tk()
                fen.title("AltéroToto Ma Musculation Perso")
                Base()
                PLVL()
                    
                PRGN=str(listprg.get(ACTIVE))
                PRGN=PRGN.split()
                PRGN=PRGN[1]
                PRGN2=""
                for j in range(len(PRGN)-1):
                    PRGN2=PRGN2+PRGN[j]

                Prgl.destroy()
                listprg.destroy()
                Open.destroy()
                Back.destroy()
                listexos = Listbox(fen_1, width=50, bg="#f0f0f0", borderwidth=0, highlightcolor="#f0f0f0", selectbackground="#f0f0f0", selectforeground="#000000", activestyle="none")
                listexos.pack()
                listexos2 = Listbox(fen_2, bg="#f0f0f0", borderwidth=0, highlightcolor="#f0f0f0", selectbackground="#f0f0f0", selectforeground="#000000", activestyle="none")
                listexos2.pack()
                listexos.insert(END, "N°: Exercices:")
                listexos2.insert(END, "Nr,Ns,Ts,Te")
                Ret = PhotoImage(file='image/Retour2.gif', master=fen_1)
                Mod =  PhotoImage(file='image/Modifier.gif', master=fen_1)
                Modifier=Button(fen_4,text="Modifier",command=Modifier, image=Mod, bd=0)
                Modifier.image = Mod
                Modifier.pack()
                Retour=Button(fen_4,text="Retour",command=Retour, image=Ret, bd=0)
                Retour.image= Ret
                Retour.pack()
                Legend1=Label(fen_3,text="Nr = Nombre de répétition", anchor=W, justify="left")
                Legend1.pack()
                Legend2=Label(fen_3,text="Ns = Nombre de série", anchor=W, justify="left")
                Legend2.pack()
                Legend3=Label(fen_3,text="Ts = Nombre de temps entre chaque séries (en sec)", anchor=W, justify="left", compound="left")
                Legend3.pack()
                Legend4=Label(fen_3,text="Ts = Nombre de temps entre chaque exercices (en sec)", anchor=W, justify="left", compound="left")
                Legend4.pack()
                with base:
                    c = base.cursor()
                    c.execute("SELECT * FROM "+PRGN2)
                    rows = c.fetchall()
                    for row in rows:
                        j=0
                        EXO=str(row)
                        EXO2=""
                        while EXO[j+1]!=",":
                            EXO2=EXO2+EXO[j+1]
                            j=j+1
                        k=j
                        while k<5:
                            EXO2=EXO2+""
                            k=k+1
                        j=j+2
                        while EXO[j]!=",":
                            EXO2=EXO2+EXO[j]
                            j=j+1
                        print(EXO2)
                        EXO3=""
                        j=j+1
                        while j<(len(EXO)-1):
                            EXO3=EXO3+EXO[j]
                            j=j+1
                        print(EXO3)
                        listexos.insert(END, EXO2)
                        listexos2.insert(END, EXO3)
                            
                            
                
            fen_1=Frame(fen)
            fen_1.grid(row=0, column=0)
            fen_2=Frame(fen)
            fen_2.grid(row=0, column=1)
            fen_3=Frame(fen)
            fen_3.grid(row=0, column=2)
            fen_4=Frame(fen)
            fen_4.grid(row=0, column=3)
            fen_5=Frame(fen)
            fen_5.grid(row=0, column=4)
            Prgl=Label(fen_1,text="Liste des programmes")
            Prgl.pack()
            listprg = Listbox(fen_1)
            listprg.pack()
            op = PhotoImage(file='image/Ouvrir.gif', master=fen_1)
            bck = PhotoImage(file='image/Retour2.gif', master=fen_1)
            Open=Button(fen_1,text="Ouvrir",command=Ouvrir, image=op, bd=0)
            Open.image = op
            Open.pack()
            Back=Button(fen_1,text="Retour",command=Retour, image=bck, bd=0)
            Back.image = bck
            Back.pack()
            with base:
                c = base.cursor()
                c.execute("SELECT * FROM pdeblist")
                rows = c.fetchall()
                for row in rows:
                    listprg.insert(END, row)
        def Retour():
            global fen
            fen.destroy()
            fen = Tk()
            Base()
            
        fen_d=Frame(fen)
        fen_d.grid(row=0, column=0)
        fen_g=Frame(fen, highlightbackground="black")
        fen_g.grid(row=0, column=1)
        PBI = PhotoImage(file='image/PB.gif', master=fen_d)
        PII = PhotoImage(file='image/PI.gif', master=fen_g)
        PEI = PhotoImage(file='image/PE.gif', master=fen_d)
        Retouri = PhotoImage(file='image/Retour.gif', master=fen_g)
        PB=Button(fen_d,text="Programmes Débutant",command=Débutant, image=PBI, bd=0, highlightbackground="black")
        PB.pack()
        PB.image = PBI
        PI=Button(fen_g,text="Programmes Intermédiaire",command="", image=PII, bd=0, highlightbackground="black")
        PI.pack()
        PI.image = PII
        PE=Button(fen_d,text="Programme Expert",command="", image=PEI, bd=0, highlightbackground="black")
        PE.pack()
        PE.image = PEI
        Retour=Button(fen_g,text="Retour",command=Retour, image=Retouri, bd=0, highlightbackground="black")
        Retour.pack()
        Retour.image = Retouri

    def MyPRG():
        global fen
        fen.destroy()
        fen = Tk()
        fen.title("AltéroToto Ma Musculation Perso")
        def Ouvrir():
            def Retour():
                global fen
                fen.destroy()
                fen = Tk()
                Base()
            def Modifier():
                j=1
                global Exoskelist
                Exoskelist=[]
                while listexos.get(j)!="":
                    Exoskelist.append(listexos.get(j))
                    j=j+1
                global modifieur
                modifieur=1
                global fen
                fen.destroy()
                fen = Tk()
                Base()
                NPRG()
                    
            PRGN=str(listprg.get(ACTIVE))
            PRGN=PRGN.split()
            PRGN=PRGN[1]
            PRGN2=""
            for j in range(len(PRGN)-1):
                PRGN2=PRGN2+PRGN[j]
            global fen
            Prgl.destroy()
            listprg.destroy()
            Open.destroy()
            Del.destroy()
            Back.destroy()
            listexos = Listbox(fen_1, width=50, bg="#f0f0f0", borderwidth=0, highlightcolor="#f0f0f0", selectbackground="#f0f0f0", selectforeground="#000000", activestyle="none")
            listexos.pack()
            listexos2 = Listbox(fen_2, bg="#f0f0f0", borderwidth=0, highlightcolor="#f0f0f0", selectbackground="#f0f0f0", selectforeground="#000000", activestyle="none")
            listexos2.pack()
            listexos.insert(END, "N°: Exercices:")
            listexos2.insert(END, "Nr,Ns,Ts,Te")
            Ret = PhotoImage(file='image/Retour2.gif', master=fen_1)
            Mod =  PhotoImage(file='image/Modifier.gif', master=fen_1)
            Modifier=Button(fen_4,text="Modifier",command=Modifier, image=Mod, bd=0)
            Modifier.image = Mod
            Modifier.pack()
            Retour=Button(fen_4,text="Retour",command=Retour, image=Ret, bd=0)
            Retour.image= Ret
            Retour.pack()
            Legend1=Label(fen_3,text="Nr = Nombre de répétition", anchor=W, justify="left")
            Legend1.pack()
            Legend2=Label(fen_3,text="Ns = Nombre de série", anchor=W, justify="left")
            Legend2.pack()
            Legend3=Label(fen_3,text="Ts = Nombre de temps entre chaque séries (en sec)", anchor=W, justify="left", compound="left")
            Legend3.pack()
            Legend4=Label(fen_3,text="Ts = Nombre de temps entre chaque exercices (en sec)", anchor=W, justify="left", compound="left")
            Legend4.pack()
            with base:
                c = base.cursor()
                c.execute("SELECT * FROM "+PRGN2)
                rows = c.fetchall()
                for row in rows:
                    j=0
                    EXO=str(row)
                    EXO2=""
                    while EXO[j+1]!=",":
                        EXO2=EXO2+EXO[j+1]
                        j=j+1
                    k=j
                    while k<5:
                        EXO2=EXO2+""
                        k=k+1
                    j=j+2
                    while EXO[j]!=",":
                        EXO2=EXO2+EXO[j]
                        j=j+1
                    print(EXO2)
                    EXO3=""
                    j=j+1
                    while j<(len(EXO)-1):
                        EXO3=EXO3+EXO[j]
                        j=j+1
                    print(EXO3)
                    listexos.insert(END, EXO2)
                    listexos2.insert(END, EXO3)
                            
                            
                
        def Retour():
            global fen
            fen.destroy()
            fen = Tk()
            Base()
        def Supprimer():
            PRGN=str(listprg.get(ACTIVE))
            PRGN=PRGN.split()
            PRGN=PRGN[1]
            PRGN2=""
            for j in range(len(PRGN)-1):
                PRGN2=PRGN2+PRGN[j]
            print(PRGN2)
            execution="DELETE FROM ndp WHERE nom="+PRGN2
            execution2="drop table if exists "+PRGN2
            print(execution)
            with base:
                c = base.cursor()
                c.execute(execution)
                c.execute(execution2)
            listprg.delete(ACTIVE)
        fen_1=Frame(fen)
        fen_1.grid(row=0, column=0)
        fen_2=Frame(fen)
        fen_2.grid(row=0, column=1)
        fen_3=Frame(fen)
        fen_3.grid(row=0, column=2)
        fen_4=Frame(fen)
        fen_4.grid(row=0, column=3)
        fen_5=Frame(fen)
        fen_5.grid(row=0, column=4)
        Prgl=Label(fen_1,text="Liste des programmes")
        Prgl.pack()
        listprg = Listbox(fen_1)
        listprg.pack()
        op = PhotoImage(file='image/Ouvrir.gif', master=fen_1)
        bck = PhotoImage(file='image/Retour2.gif', master=fen_1)
        sup = PhotoImage(file='image/Supprimer.gif', master=fen_1)
        Open=Button(fen_1,text="Ouvrir",command=Ouvrir, image=op, bd=0)
        Open.image = op
        Open.pack()
        Del=Button(fen_1,text="Supprimer",command=Supprimer, image=sup, bd=0)
        Del.image=sup
        Del.pack()
        Back=Button(fen_1,text="Retour",command=Retour, image=bck, bd=0)
        Back.image = bck
        Back.pack()
        with base:
            c = base.cursor()
            c.execute("SELECT * FROM ndp")
            rows = c.fetchall()
            for row in rows:
                listprg.insert(END, row)
             
    def NPRG():
        global fen
        fen.destroy()
        fen = Tk()
        fen.title("AltéroToto Ma Musculation Perso")
        def Ajouter():
            listexos.insert(END, (listmolets.get(ACTIVE)+listtriceps.get(ACTIVE)+listbiceps.get(ACTIVE)+listcnfs.get(ACTIVE)+listabdos.get(ACTIVE)+listdos.get(ACTIVE)+listepaules.get(ACTIVE)+listpectoraux.get(ACTIVE)))
        def Supprimer():
            listexos.delete(ACTIVE)
        def Retour():
            global fen
            fen.destroy()
            fen = Tk()
            Base()
        def Valider():
            PRGN=str(Nompge.get())
            params=(str(PRGN),)
            with base:
                c = base.cursor()
                c.execute("CREATE TABLE "+PRGN+" (id INTEGER PRIMARY KEY, Ex TEXT,Nr INTEGER,Ns INTEGER,Ts INTEGER,Te INTEGER)")
                c.execute("INSERT INTO ndp VALUES (NOT NULL,?)",params)
            def Retour():
                global fen
                fen.destroy()
                fen = Tk()
                Base()
                NPRG()
            def Suivant():
                Ex=str(listexos.get(0))
                Nr=str(Nre.get())
                Ns=str(Nse.get())
                Ts=Tse.get()
                Te=Tee.get()
                params=(Ex,Nr,Ns,Ts,Te,)
                with base:
                    c = base.cursor()
                    c.execute("INSERT INTO "+PRGN+" VALUES (NULL,?,?,?,?,?)",params)
                listexos.delete(0)
                nde.set("Nom de l'exercice: "+str(listexos.get(0)))
                fen.update_idletasks()
                if listexos.get(0)=="":

                    fen.destroy()
                    fen = Tk()
                    Base()

            Abdob.destroy()
            listabdos.destroy()
            Pectob.destroy()
            listpectoraux.destroy()
            Dob.destroy()
            listdos.destroy()
            epauleb.destroy()
            listepaules.destroy()
            bicepb.destroy()
            listbiceps.destroy()
            tricepb.destroy()
            listtriceps.destroy()
            Cnfb.destroy()
            listcnfs.destroy()
            Moletb.destroy()
            listmolets.destroy()
            Add.destroy()
            Del.destroy()
            Val.destroy()
            Back.destroy()
            Nompge.destroy()
            Nompgl.destroy()
            videe.destroy()

            
            nde=StringVar()
            nde.set("Nom de l'exercice: "+str(listexos.get(0)))
            print(nde)
            Exosl=Label(fen_1,textvariable=nde)
            Exosl.pack()
            Sv = PhotoImage(file='image/Suivant.gif', master=fen_5)
            Bck = PhotoImage(file='image/Retour2.gif', master=fen_5)
            Suiv=Button(fen_5,text="Suivant",command=Suivant, image = Sv, bd = 0)
            Suiv.image = Sv
            Suiv.pack()
            BACK=Button(fen_5,text="Retour",command=Retour, image = Bck, bd=0)
            BACK.image = Bck
            BACK.pack()
            Nrl=Label(fen_1,text="Nombre de répétition:",height=5,width=35)
            Nrl.pack()
            
            fen.update_idletasks()
            vide=Label(fen_2,text="")
            vide.pack()
            Nsl=Label(fen_2,text="Nombre de Série:",height=5,width=35)
            Nsl.pack()
            vide=Label(fen_3,text="")
            vide.pack()
            Tsl=Label(fen_3,text="Temps de pause entre chaque série (en sec):",height=5)
            Tsl.pack()
            vide=Label(fen_4,text="")
            vide.pack()
            Tel=Label(fen_4,text="Temps de pause après l'exercice (en sec):",height=5)
            Tel.pack()
            Nre=Entry(fen_1,width=35)
            Nre.pack()
            Nse=Entry(fen_2,width=35)
            Nse.pack()
            Tse=Entry(fen_3,width=35)
            Tse.pack()
            Tee=Entry(fen_4,width=35)
            Tee.pack()            
            
        def Abdos():
            listmolets.delete(0, END)
            listtriceps.delete(0, END)
            listbiceps.delete(0, END)
            listcnfs.delete(0, END)
            listabdos.delete(0, END)
            listdos.delete(0, END)
            listepaules.delete(0, END)
            listpectoraux.delete(0, END)
            for item in ["Crunch au sol", "Relevés de bassin sur plan incliné", "Sit-up", "Relevés de genoux", "Relevés de jambes sur plan incliné", "Relevés de buste sur banc incliné", "Relevés de jambes renversés", "Crunch à la poulie haute", "Crunchs avec rotation", "Flexions Latérales", "Torsion de bassin couché","Rotation de buste à la poulie","Relevés de jambes en suspension","La planche","Le développé Pallof","Gainage des obliques avec le Side Bridge"]:
                listabdos.insert(END, item)
        def Pectoraux():
            listmolets.delete(0, END)
            listtriceps.delete(0, END)
            listbiceps.delete(0, END)
            listcnfs.delete(0, END)
            listabdos.delete(0, END)
            listdos.delete(0, END)
            listepaules.delete(0, END)
            listpectoraux.delete(0, END)
            for item in ["Développé couché barre","Pompes au sol","Ecarté couché haltères","Pec-Deck","Pompes Dive Bomber","Les dips façon Gironda","Développé assis à la machine","Développé couché à la smith machine","Développé couché incliné","Ecarté couché incliné","Développé à la machine convergente","Développé couché prise inversée","Développé couché décliné","Les dips","Les dips entre 2 bancs","Ecartés à la poulie vis-à-vis","Pull-over"]:
                listpectoraux.insert(END, item)
        def Dos():
            listmolets.delete(0, END)
            listtriceps.delete(0, END)
            listbiceps.delete(0, END)
            listcnfs.delete(0, END)
            listabdos.delete(0, END)
            listdos.delete(0, END)
            listepaules.delete(0, END)
            listpectoraux.delete(0, END)
            for item in ["Tractions à la barre fixe","Tirage poitrine","Tirage nuque","Tirage prise serrée","Le Power Clean","Muscle-Up","Rowing barre","Tirage sol poulie basse","Rowing un bras","Rowing barre T","Rowing inversé","Tractions au sternum Gironda","Extensions au banc","Good Morning barre","Shrug barre"]:
                listdos.insert(END, item)
        def Epaules():
            listmolets.delete(0, END)
            listtriceps.delete(0, END)
            listbiceps.delete(0, END)
            listcnfs.delete(0, END)
            listabdos.delete(0, END)
            listdos.delete(0, END)
            listepaules.delete(0, END)
            listpectoraux.delete(0, END)
            for item in ["Développé devant","Développé haltère","Développé nuque","Rowing menton","Elévations latérales","Elévations latérales buste penché (Oiseau)","Elévations latérales aux câbles","Développé Arnold","Développé Cubain","Le Face Pull"]:
                listepaules.insert(END, item)
        def Biceps():
            listmolets.delete(0, END)
            listtriceps.delete(0, END)
            listbiceps.delete(0, END)
            listcnfs.delete(0, END)
            listabdos.delete(0, END)
            listdos.delete(0, END)
            listepaules.delete(0, END)
            listpectoraux.delete(0, END)
            for item in ["Curl barre","Curl haltère","Curl pupitre","Curl concentration","Le curl incliné","Le curl Araignée","Le curl Gironda","Curl Zottman"]:
                listbiceps.insert(END, item)
        def Triceps():
            listmolets.delete(0, END)
            listtriceps.delete(0, END)
            listbiceps.delete(0, END)
            listcnfs.delete(0, END)
            listabdos.delete(0, END)
            listdos.delete(0, END)
            listepaules.delete(0, END)
            listpectoraux.delete(0, END)
            for item in ["Barre front","Extensions au-dessus de la tête","kick back","Extensions à la poulie haute","Développé couché prise serrée"]:
                listtriceps.insert(END, item)
        def Cnfs():
            listmolets.delete(0, END)
            listtriceps.delete(0, END)
            listbiceps.delete(0, END)
            listcnfs.delete(0, END)
            listabdos.delete(0, END)
            listdos.delete(0, END)
            listepaules.delete(0, END)
            listpectoraux.delete(0, END)
            for item in ["Le squat","Presse à cuisses","Squat 1 jambe","Hack Squat","Les fentes","Leg Extension","Sissy squat","Leg curl couché","Leg curl assis","Soulevé de terre","Le soulevé de terre Roumain","Soulevé de terre jambes tendues","Burpee","Le soulevé de terre Sumo","Le Power Clean"]:
                listcnfs.insert(END, item)
        def Molets():
            listmolets.delete(0, END)
            listtriceps.delete(0, END)
            listbiceps.delete(0, END)
            listcnfs.delete(0, END)
            listabdos.delete(0, END)
            listdos.delete(0, END)
            listepaules.delete(0, END)
            listpectoraux.delete(0, END)
            for item in ["Mollets debout","Mollets assis","Mollets presse à cuisses","Mollets au donkey"]:
                listmolets.insert(END, item)
            
        fen_1=Frame(fen)
        fen_1.grid(row=0, column=0)
        fen_2=Frame(fen)
        fen_2.grid(row=0, column=1)
        fen_3=Frame(fen)
        fen_3.grid(row=0, column=2)
        fen_4=Frame(fen)
        fen_4.grid(row=0, column=3)
        fen_5=Frame(fen)
        fen_5.grid(row=0, column=4)
        listdos = Listbox(fen_3)
        Abdob=Radiobutton(fen_1,text="Abdos",command=Abdos,value=8)
        Abdob.pack()
        listabdos = Listbox(fen_1)
        listabdos.pack()
        Pectob=Radiobutton(fen_2,text="Pectoraux",command=Pectoraux,value=1)
        Pectob.pack()
        listpectoraux = Listbox(fen_2)
        listpectoraux.pack()
        Dob=Radiobutton(fen_3,text="Dos",command=Dos,value=2)
        Dob.pack()
        listdos = Listbox(fen_3)
        listdos.pack()
        epauleb=Radiobutton(fen_4,text="Epaules",command=Epaules,value=3)
        epauleb.pack()
        listepaules = Listbox(fen_4)
        listepaules.pack()
        bicepb=Radiobutton(fen_1,text="Biceps",command=Biceps,value=4)
        bicepb.pack()
        listbiceps = Listbox(fen_1)
        listbiceps.pack()
        tricepb=Radiobutton(fen_2,text="Triceps",command=Triceps,value=5)
        tricepb.pack()
        listtriceps = Listbox(fen_2)
        listtriceps.pack()
        Exol=Label(fen_5,text="Exercices sélectionnées:")
        Exol.pack()
        listexos = Listbox(fen_5)
        listexos.pack()
        listexos.delete(0,END)
        Cnfb=Radiobutton(fen_3,text="Cuisses et Fessiers",command=Cnfs,value=6)
        Cnfb.pack()
        listcnfs = Listbox(fen_3)
        listcnfs.pack()
        Moletb=Radiobutton(fen_4,text="Mollets",command=Molets,value=7)
        Moletb.pack()
        listmolets = Listbox(fen_4)
        listmolets.pack()


        Deli= PhotoImage(file='image/Supprimer.gif', master=fen_5)
        Addi= PhotoImage(file='image/Ajouter.gif', master=fen_5)
        Vali= PhotoImage(file='image/Valider.gif', master=fen_5)
        Retouri= PhotoImage(file='image/Retour2.gif', master=fen_5)
        
        Add=Button(fen_5,text="Ajouter",command=Ajouter, image=Addi, width=120, height=25, bd=0)
        Add.image = Addi
        Add.pack()
        Del=Button(fen_5,text="Supprimer",command=Supprimer, image=Deli, width=120, height=25,bd=0)
        Del.image=Deli
        Del.pack()
        Val=Button(fen_5,text="Valider",command=Valider, image=Vali, width=120, height=25,bd=0)
        Val.image = Vali
        Val.pack()
        Back=Button(fen_5,text="Retour",command=Retour, image=Retouri, width=120, height=25,bd=0)
        Back.image = Retouri
        Back.pack()
        Nompgl=Label(fen_5,text="Nom du programme:")
        Nompgl.pack()
        Nompge=Entry(fen_5)
        Nompge.pack()
        videe=Label(fen_5,text="",height=2)
        videe.pack()
        global modifieur
        global Exoskelist
        if modifieur==1:
            for i in range(len(Exoskelist)):
                NEXO=str(Exoskelist[i])
                NEXO2=""
                for j in range(len(NEXO)-4):
                    NEXO2=NEXO2+NEXO[j+3]
                listexos.insert(END, NEXO2)
                
        
        
    fen_d=Frame(fen)
    fen_d.grid(row=0, column=0)
    fen_g=Frame(fen)
    fen_g.grid(row=0, column=1)
    imgPPM = PhotoImage(file='image/PPM.gif', master=fen_g)
    imgPLVL = PhotoImage(file='image/PLVL.gif', master=fen_d)
    imgMPRG = PhotoImage(file='image/MPRG.gif', master=fen_d)
    imgNPRG = PhotoImage(file='image/NPRG.gif', master=fen_g)
    BPPM=Button(fen_g,text="Programmes par Muscle",command=PMSC, image=imgPPM, bd=0)
    BPPM.pack()
    BPPM.image = imgPPM
    BPPLVL=Button(fen_d,text="Programmes par level",command=PLVL, image=imgPLVL, bd=0)
    BPPLVL.pack()
    BPPLVL.image =imgPLVL
    BMP=Button(fen_d,text="Mes programmes",command=MyPRG, image=imgMPRG, bd=0)
    BMP.pack()
    BMP.image =imgMPRG
    NP=Button(fen_g,text="Nouveau Programme",command=NPRG, image=imgNPRG, bd=0)
    NP.pack()
    NP.image =imgNPRG
fen.title("Altero toto ma musculation perso")
fen.iconphoto(False, PhotoImage(file='image/ico.png'))
Base()
fen.mainloop()

