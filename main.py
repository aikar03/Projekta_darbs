import tkinter as tk
from pygame import mixer
from tkinter import *
import os
import random
from pathlib import Path

mixer.init()

Audio_mape = os.path.join(os.path.dirname(__file__), "klavieru_skanas(mp3)")
Harmoniski = os.path.join(os.path.dirname(__file__), "Harmoniski")
Melodiski = os.path.join(os.path.dirname(__file__), "Melodiski")

izvelets_skaits = None
izvelets_rezims = None
pedejais_fails = None
melodiski_audio= []
harmoniski_audio = []
pogu_saraksts = []

intervala_piemers = 0
punkti = 0
uzdevumu_skaits = None

ievade = None


#-------------skaņu funkcijas-------------------------------------#
def C():
    fails = os.path.join(Audio_mape, "28.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def Db():
    fails = os.path.join(Audio_mape, "29.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def D():
    fails = os.path.join(Audio_mape, "30.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def Eb():
    fails = os.path.join(Audio_mape, "31.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def E():
    fails = os.path.join(Audio_mape, "32.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def F():
    fails = os.path.join(Audio_mape, "33.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def Gb():
    fails = os.path.join(Audio_mape, "34.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def G():
    fails = os.path.join(Audio_mape, "35.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def Ab():
    fails = os.path.join(Audio_mape, "36.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def A():
    fails = os.path.join(Audio_mape, "37.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def Bb():
    fails = os.path.join(Audio_mape, "38.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def B():
    fails = os.path.join(Audio_mape, "39.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def C2():
    fails = os.path.join(Audio_mape, "40.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def Db2():
    fails = os.path.join(Audio_mape, "41.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def D2():
    fails = os.path.join(Audio_mape, "42.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def Eb2():
    fails = os.path.join(Audio_mape, "43.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def E2():
    fails = os.path.join(Audio_mape, "44.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def F2():
    fails = os.path.join(Audio_mape, "45.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def Gb2():
    fails = os.path.join(Audio_mape, "46.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def G2():
    fails = os.path.join(Audio_mape, "47.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def Ab2():
    fails = os.path.join(Audio_mape, "48.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def A2():
    fails = os.path.join(Audio_mape, "49.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def Bb2():
    fails = os.path.join(Audio_mape, "50.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def B2():
    fails = os.path.join(Audio_mape, "51.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def C3():
    fails = os.path.join(Audio_mape, "52.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def Db3():
    fails = os.path.join(Audio_mape, "53.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def D3():
    fails = os.path.join(Audio_mape, "54.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def Eb3():
    fails = os.path.join(Audio_mape, "55.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def E3():
    fails = os.path.join(Audio_mape, "56.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def F3():
    fails = os.path.join(Audio_mape, "57.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def Gb3():
    fails = os.path.join(Audio_mape, "58.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def G3():
    fails = os.path.join(Audio_mape, "59.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def Ab3():
    fails = os.path.join(Audio_mape, "60.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def A3():
    fails = os.path.join(Audio_mape, "61.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def Bb3():
    fails = os.path.join(Audio_mape, "62.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def B3():
    fails = os.path.join(Audio_mape, "63.mp3")
    mixer.music.load(fails)
    mixer.music.play()
def C4():
    fails = os.path.join(Audio_mape, "64.mp3")
    mixer.music.load(fails)
    mixer.music.play()

#----------------------Pārējās funkcijas-----------------------------------------#



def Apturet_programmu():
    window.destroy()

def Uzstadijumi():
    sakuma_skats.pack_forget()  # aizver skatu
    uzstadijumu_skats.pack(fill='both', expand=True)  # atver skatu

def Sakt():
    global izvelets_skaits
    global izvelets_rezims
    global uzdevumu_skaits, punkti, intervala_piemers
    global ievade
    izvelets_skaits = ievade.get()
    izvelets_rezims = rezims.get()
    if not izvelets_rezims:
        bridinajums = tk.Label(uzstadijumu_skats, text="Izvēlies atskaņošanas veidu!", font=('Verdana', 10, 'bold'), fg='red')
        bridinajums.pack(pady=10)
        bridinajums.after(2000, bridinajums.destroy)
        return 
    if izvelets_skaits.isdigit():
        izvelets_skaitlis = int(izvelets_skaits)
        if 1 <= izvelets_skaitlis <= 30:

            uzdevumu_skaits = izvelets_skaitlis
            intervala_piemers = 0
            punkti = 0
            
            Atjaunot_skaititaju()

            uzstadijumu_skats.pack_forget()
            intervalu_skats.pack(fill='both', expand=True)

            Ieladet_audio()
            return
            
        else:
            bridinajums = tk.Label(uzstadijumu_skats, text="Izvēlies skaitli no 1 līdz 30!", font=('Verdana', 10, 'bold'), fg='red')
            bridinajums.pack(pady=10)
            bridinajums.after(2000, bridinajums.destroy)
            return
    else:
        bridinajums = tk.Label(uzstadijumu_skats, text="Izvēlies, cik intervālus klausīties!", font=('Verdana', 10, 'bold'), fg='red')
        bridinajums.pack(pady=10)
        bridinajums.after(2000, bridinajums.destroy)
        return

def Saglabat_rezims():
    global izvelets_rezims
    izvelets_rezims = rezims.get()

def Ieladet_visus_audio():
    global melodiski_audio, harmoniski_audio
    
    melodiski_audio = list(Path(Melodiski).glob("*.mp3"))
    harmoniski_audio = list(Path(Harmoniski).glob("*.mp3")) 

def Ieladet_audio():
    global pedejais_fails, izvelets_rezims, melodiski_audio, harmoniski_audio, sobrid_intervals
    
    for p, t in pogu_saraksts:
        p.config(bg='SystemButtonFace')

    if izvelets_rezims == "Mel":
        pedejais_fails = random.choice(melodiski_audio)
        mixer.music.load(str(pedejais_fails))
        mixer.music.play()
        print(f"Atskaņots melodiskais: {pedejais_fails.name}")

    elif izvelets_rezims == "Harm":
        pedejais_fails = random.choice(harmoniski_audio)
        mixer.music.load(str(pedejais_fails))
        mixer.music.play()
        print(f"Atskaņots harmoniskais: {pedejais_fails.name}")

    sobrid_intervals = Atpazit_intervalu(pedejais_fails.name)


def Atkartot_pedejo():
    mixer.music.load(str(pedejais_fails))
    mixer.music.play()
        
def Atpazit_intervalu(faila_nosaukums):
    
    nosaukums = Path(faila_nosaukums).stem
    atslega = nosaukums[:2]
 
    intervāli = {
        "m2": "Msekunda",
        "l2": "Lsekunda", 
        "m3": "Mterca",
        "l3": "Lterca",
        "t4": "Tkvarta",
        "tr": "Tritons", 
        "t5": "Tkvinta", 
        "m6": "Mseksta",
        "l6": "Lseksta",
        "m7": "Mseptima",
        "l7": "Lseptima",
        "t8": "Toktava",
    }
    
    return intervāli.get(atslega, "Nezināms")


def Parbaudit_atbildi(atbilde, poga):
    global pogaAtkarto, intervala_piemers, punkti, uzdevumu_skaits

    pareiza = Atpazit_intervalu(pedejais_fails.name)

    for p, t in pogu_saraksts:
        p.config(bg='SystemButtonFace')

    if atbilde == pareiza:
        poga.config(bg='lightgreen')
        punkti += 1
    else:
        poga.config(bg='lightcoral')
        for p, t in pogu_saraksts:
            if t == pareiza:
                p.config(bg='lightgreen')
                break
    
    intervala_piemers += 1 
    Atjaunot_skaititaju()
    
    if intervala_piemers >= uzdevumu_skaits:
        pogaAtkarto.config(text="Beigt sesiju", command=Beigt_speli, width=20, height=2, bg='lightgrey', fg='#800000', font=('Verdana', 12, 'bold'))
        return

    pogaAtkarto.config(text="Nākamais intervāls", command=Nakamais_intervals, width=20, height=2, bg='lightgrey', fg='#800000', font=('Verdana', 12, 'bold'))


def Nakamais_intervals():
    global pogaAtkarto

    pogaAtkarto.config(text="Atškaņot intervālu", command=Atkartot_pedejo, width=20, height=2, bg = 'lightgrey', fg = '#800000', font = ('Verdana', 12, 'bold'))
    
    Ieladet_audio()  #Atskaņo nākamo intervālu

def Atjaunot_skaititaju():
    global intervala_piemers, uzdevumu_skaits, skaititajs
    
    if uzdevumu_skaits:
        skaititajs.config(text=f"{intervala_piemers}/{uzdevumu_skaits}")
    else:
        skaititajs.config(text=" ")

def Atjaunot_uzstadijumu_skatu():
    global ievade, rezims
    
    ievade.delete(0, tk.END)
    rezims.set("")
    
    for widget in uzstadijumu_skats.winfo_children():
        if isinstance(widget, tk.Label) and widget.cget("fg") == "red":
            widget.destroy()


def Beigt_speli():
    global intervalu_skats, beigu_skats, punkti, uzdevumu_skaits, poga_velreiz, poga_uzstadijumi
    
    intervalu_skats.pack_forget()

    for widget in beigu_skats.winfo_children():
        widget.destroy()
    
    tk.Label(beigu_skats, text=f"Tu atpazini {punkti} no {uzdevumu_skaits} intervāliem!", font=('Verdana', 24, 'bold'), fg='#800000').pack(pady=(80, 40))
    
    poga_velreiz=tk.Button(beigu_skats, text="Spēlēt vēlreiz", command=Jauna_spēle_no_beigām, width=20, height=2, bg='lightgrey', font=('Verdana', 12)).pack(pady=10)
    
    poga_uzstadijumi = tk.Button(beigu_skats, text="Sesijas uzstādījumi", command=Uz_uzstadijumiem_no_beigām, width=20, height=2, bg='lightgrey', font=('Verdana', 12)).pack(pady=10)
    
    beigu_skats.pack(fill='both', expand=True)

def Jauna_spēle_no_beigām():
    global beigu_skats, intervalu_skats, intervala_piemers, punkti, pogaAtkarto
    
    beigu_skats.pack_forget()
    
    intervala_piemers = 0
    punkti = 0
    Atjaunot_skaititaju()
    
    for p, t in pogu_saraksts:
        p.config(bg='SystemButtonFace') #Atjauno pogas

    pogaAtkarto.config(text="Atškaņot intervālu", command=Atkartot_pedejo, 
                       width=20, height=2, bg='lightgrey', fg='#800000', 
                       font=('Verdana', 12, 'bold'))
    
    for widget in beigu_skats.winfo_children():
        widget.destroy()
    
    intervalu_skats.pack(fill='both', expand=True)
    
    Ieladet_audio()

def Uz_uzstadijumiem_no_beigām():
    global beigu_skats, uzstadijumu_skats, intervala_piemers, punkti, pogaAtkarto 
    
    beigu_skats.pack_forget()
    
    intervala_piemers = 0
    punkti = 0

    for p, t in pogu_saraksts:
        p.config(bg='SystemButtonFace')
  
    pogaAtkarto.config(text="Atškaņot intervālu", command=Atkartot_pedejo, 
                       width=20, height=2, bg='lightgrey', fg='#800000', 
                       font=('Verdana', 12, 'bold'))
    
    for widget in beigu_skats.winfo_children():
        widget.destroy()

    Atjaunot_uzstadijumu_skatu()
    
    uzstadijumu_skats.pack(fill='both', expand=True)


# programmas loga izveide
window = tk.Tk()
window.title("Skaņas intervāli")
window.geometry("990x550")
window.resizable(False, False) 
mixer.init()

# ---------- Teksta kaste ----------#
teksta_kaste = tk.Frame(window, height=350)
teksta_kaste.pack(fill='both', expand=True)
teksta_kaste.pack_propagate(False)

# ---------- Klavieru kaste ----------#
klavieru_kaste = tk.Frame(window, height=200)
klavieru_kaste.pack(side='bottom', fill='x') 
klavieru_kaste.pack_propagate(False)



#---------------------------------------Klavieru taustiņi------------------------#
 #Klavieru dizains un taustiņu programmas kods no https://github.com/aniketroy03/Piano
 #Klavieru skaņu audio no https://github.com/daviddeborin/Piano-Sounds-High-Quality-

b = Button(klavieru_kaste, height=10, width=5, command=C, bg="white")
b.grid(row=0,column=1)

b2 = Button(klavieru_kaste, height=10, width=5, command=D, bg="white")
b2.grid(row=0,column=2)

b3 = Button(klavieru_kaste, height=10, width=5, command=E, bg="white")
b3.grid(row=0,column=3)

b4 = Button(klavieru_kaste, height=10, width=5, command=F, bg="white")
b4.grid(row=0,column=4)

b5 = Button(klavieru_kaste, height=10, width=5, command=G, bg="white")
b5.grid(row=0,column=5)

b6 = Button(klavieru_kaste, height=10, width=5, command=A, bg="white")
b6.grid(row=0,column=6)

b7 = Button(klavieru_kaste, height=10, width=5, command=B, bg="white")
b7.grid(row=0,column=7)

b8 = Button(klavieru_kaste, height=10, width=5, command=C2, bg="white")
b8.grid(row=0,column=8)

b9 = Button(klavieru_kaste, height=10, width=5, command=D2, bg="white")
b9.grid(row=0,column=9)

b10 = Button(klavieru_kaste, height=10, width=5, command=E2, bg="white")
b10.grid(row=0,column=10)

b11 = Button(klavieru_kaste, height=10, width=5, command=F2, bg="white")
b11.grid(row=0,column=11)

a1 = Button(klavieru_kaste, command=Db, width=2, height=6, bg="black")
a1.place(x=32,y=0)

a2 = Button(klavieru_kaste, command=Eb, width=2, height=6, bg="black")
a2.place(x=77,y=0)

a3 = Button(klavieru_kaste, command=Gb, width=2, height=6, bg="black")
a3.place(x=167,y=0)

a4 = Button(klavieru_kaste, command=Ab, width=2, height=6, bg="black")
a4.place(x=213,y=0)

a5 = Button(klavieru_kaste, command=Bb, width=2, height=6, bg="black")
a5.place(x=257,y=0)

a6 = Button(klavieru_kaste, command=Db2, width=2, height=6, bg="black")
a6.place(x=347,y=0)

a7 = Button(klavieru_kaste, command=Eb2, width=2, height=6, bg="black")
a7.place(x=393,y=0)

b12 = Button(klavieru_kaste, height=10, width=5, command=G2, bg="white")
b12.grid(row=0,column=12)

b13 = Button(klavieru_kaste, height=10, width=5, command=A2, bg="white")
b13.grid(row=0,column=13)

b14 = Button(klavieru_kaste, height=10, width=5, command=B2, bg="white")
b14.grid(row=0,column=14)

b15 = Button(klavieru_kaste, height=10, width=5, command=C3, bg="white")
b15.grid(row=0,column=15)

b16 = Button(klavieru_kaste, height=10, width=5, command=D3, bg="white")
b16.grid(row=0,column=16)

b17 = Button(klavieru_kaste, height=10, width=5, command=E3, bg="white")
b17.grid(row=0,column=17)

b18 = Button(klavieru_kaste, height=10, width=5, command=F3, bg="white")
b18.grid(row=0,column=18)

b19 = Button(klavieru_kaste, height=10, width=5, command=G3, bg="white")
b19.grid(row=0,column=19)

b20 = Button(klavieru_kaste, height=10, width=5, command=A3, bg="white")
b20.grid(row=0,column=20)

b21 = Button(klavieru_kaste, height=10, width=5, command=B3, bg="white")
b21.grid(row=0,column=21)

b22 = Button(klavieru_kaste, height=10, width=5, command=C4, bg="white")
b22.grid(row=0,column=22)

a8 = Button(klavieru_kaste, command=Gb2, width=2, height=6, bg="black")
a8.place(x=482,y=0)

a9 = Button(klavieru_kaste, command=Ab2, width=2, height=6, bg="black")
a9.place(x=528,y=0)

a10 = Button(klavieru_kaste, command=Bb2, width=2, height=6, bg="black")
a10.place(x=572,y=0)

a11 = Button(klavieru_kaste, command=Db3, width=2, height=6, bg="black")
a11.place(x=662,y=0)

a12 = Button(klavieru_kaste, command=Eb3, width=2, height=6, bg="black")
a12.place(x=708,y=0)

a13 = Button(klavieru_kaste, command=Gb3, width=2, height=6, bg="black")
a13.place(x=797,y=0)

a14 = Button(klavieru_kaste, command=Ab3, width=2, height=6, bg="black")
a14.place(x=842,y=0)

a15 = Button(klavieru_kaste, command=Bb3, width=2, height=6, bg="black")
a15.place(x=887,y=0)

#--------------------------------- sākuma skats ---------------------------------#
sakuma_skats = tk.Frame(teksta_kaste)

uzraksts = tk.Label(sakuma_skats, text="Skaņas intervāli", font=('Verdana', 32, 'bold'), fg = '#800000')
uzraksts.pack(pady=(100, 40))

pogaUzstadijumi = tk.Button(sakuma_skats, text="Sesijas uzstādījumi", command=Uzstadijumi, width=20, height=2, bg = 'lightgrey', fg = '#800000', font = ('Verdana', 12, 'bold'))
pogaUzstadijumi.pack(pady=10)

#------------------------------- uzstādījumu skats -------------------------------#
uzstadijumu_skats = tk.Frame(teksta_kaste)

uzraksts = tk.Label(uzstadijumu_skats, text="Jauna sesija", font=('Verdana', 24, 'bold'), fg = '#800000')
uzraksts.pack(pady= 20)

jautajums = tk.Label(uzstadijumu_skats, text="Cik intervālus tu vēlies klausīties?", font=('Verdana', 16), fg = 'black')
jautajums.pack(pady=5)

ievade = tk.Entry(uzstadijumu_skats, width=10, font=('Verdana', 12))
ievade.pack(pady=5)

kaste_opcijam = tk.Frame(uzstadijumu_skats)
kaste_opcijam.pack(pady=10)
rezims = tk.StringVar(value="")

izvele_a = tk.Radiobutton(kaste_opcijam, text="Melodiski",variable=rezims, value="Mel", font=('Verdana', 11), command=Saglabat_rezims)
izvele_a.pack(side=tk.LEFT, padx=30)

izvele_b = tk.Radiobutton(kaste_opcijam, text="Harmoniski",variable=rezims, value="Harm", font=('Verdana', 11), command=Saglabat_rezims)
izvele_b.pack(side=tk.LEFT, padx=30)

pogaSakt = tk.Button(uzstadijumu_skats, text="Sākt sesiju", command=Sakt, width=20, height=2, bg = 'lightgrey', fg = '#800000', font = ('Verdana', 12, 'bold'))
pogaSakt.pack(pady=10)

#------------------------------- intervalu skats -------------------------------#
intervalu_skats = tk.Frame(teksta_kaste)

skaititajs = tk.Label(intervalu_skats, text="", font=('Verdana', 10, 'bold'), fg='black')
skaititajs.place(x=10, y=10)

uzraksts = tk.Label(intervalu_skats, text="Kāds intervāls tiek atskaņots?", font=('Verdana', 24, 'bold'), fg = '#800000')
uzraksts.pack(pady= 20)

# Rāmis pogām
pogu_ramis1 = tk.Frame(intervalu_skats)
pogu_ramis1.pack(pady=20)
pogu_ramis2 = tk.Frame(intervalu_skats)
pogu_ramis2.pack(pady=20)

#------------------------------- intervalu pogas -------------------------------#
poga_m2 = tk.Button(pogu_ramis1, text="m2", width=10, height=2)
poga_m2.pack(side=tk.LEFT, padx=5)
poga_m2.config(command=lambda: Parbaudit_atbildi("Msekunda", poga_m2))
pogu_saraksts.append([poga_m2, "Msekunda"])

poga_l2 = tk.Button(pogu_ramis1, text="l2", width=10, height=2)
poga_l2.pack(side=tk.LEFT, padx=5)
poga_l2.config(command=lambda: Parbaudit_atbildi("Lsekunda", poga_l2))
pogu_saraksts.append([poga_l2, "Lsekunda"])

poga_m3 = tk.Button(pogu_ramis1, text="m3", width=10, height=2)
poga_m3.pack(side=tk.LEFT, padx=5)
poga_m3.config(command=lambda: Parbaudit_atbildi("Mterca", poga_m3))
pogu_saraksts.append([poga_m3, "Mterca"])

poga_l3 = tk.Button(pogu_ramis1, text="l3", width=10, height=2)
poga_l3.pack(side=tk.LEFT, padx=5)
poga_l3.config(command=lambda: Parbaudit_atbildi("Lterca", poga_l3))
pogu_saraksts.append([poga_l3, "Lterca"])

poga_t4 = tk.Button(pogu_ramis1, text="t4", width=10, height=2)
poga_t4.pack(side=tk.LEFT, padx=5)
poga_t4.config(command=lambda: Parbaudit_atbildi("Tkvarta", poga_t4))
pogu_saraksts.append([poga_t4, "Tkvarta"])

poga_tritons = tk.Button(pogu_ramis1, text="pl4/pm5", width=10, height=2)
poga_tritons.pack(side=tk.LEFT, padx=5)
poga_tritons.config(command=lambda: Parbaudit_atbildi("Tritons", poga_tritons))
pogu_saraksts.append([poga_tritons, "Tritons"])

poga_t5 = tk.Button(pogu_ramis2, text="t5", width=10, height=2)
poga_t5.pack(side=tk.LEFT, padx=5)
poga_t5.config(command=lambda: Parbaudit_atbildi("Tkvinta", poga_t5))
pogu_saraksts.append([poga_t5, "Tkvinta"])

poga_m6 = tk.Button(pogu_ramis2, text="m6", width=10, height=2)
poga_m6.pack(side=tk.LEFT, padx=5)
poga_m6.config(command=lambda: Parbaudit_atbildi("Mseksta", poga_m6))
pogu_saraksts.append([poga_m6, "Mseksta"])

poga_l6 = tk.Button(pogu_ramis2, text="l6", width=10, height=2)
poga_l6.pack(side=tk.LEFT, padx=5)
poga_l6.config(command=lambda: Parbaudit_atbildi("Lseksta", poga_l6))
pogu_saraksts.append([poga_l6, "Lseksta"])

poga_m7 = tk.Button(pogu_ramis2, text="m7", width=10, height=2)
poga_m7.pack(side=tk.LEFT, padx=5)
poga_m7.config(command=lambda: Parbaudit_atbildi("Mseptima", poga_m7))
pogu_saraksts.append([poga_m7, "Mseptima"])

poga_l7 = tk.Button(pogu_ramis2, text="l7", width=10, height=2)
poga_l7.pack(side=tk.LEFT, padx=5)
poga_l7.config(command=lambda: Parbaudit_atbildi("Lseptima", poga_l7))
pogu_saraksts.append([poga_l7, "Lseptima"])

poga_t8 = tk.Button(pogu_ramis2, text="t8", width=10, height=2)
poga_t8.pack(side=tk.LEFT, padx=5)
poga_t8.config(command=lambda: Parbaudit_atbildi("Toktava", poga_t8))
pogu_saraksts.append([poga_t8, "Toktava"])

#-------------------------------------------------------------#

pogaAtkarto = tk.Button(intervalu_skats, text="Atskaņot intervālu", command=Atkartot_pedejo, width=20, height=2, bg = 'lightgrey', fg = '#800000', font = ('Verdana', 12, 'bold'))
pogaAtkarto.pack(pady=10)

#------------------------------- beigu skats -------------------------------#
beigu_skats = tk.Frame(teksta_kaste)


# sāk Tkinter galveno cilpu
sakuma_skats.pack(fill='both', expand=True)
Ieladet_visus_audio()
window.mainloop()