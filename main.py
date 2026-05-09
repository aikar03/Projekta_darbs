import tkinter as tk
from pygame import mixer
from tkinter import *
import os

Audio_mape = os.path.join(os.path.dirname(__file__), "klavieru_skanas(mp3)")

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



def close_all_windows():
    window.destroy()

def funkUzstadijumi():
    sakuma_skats.pack_forget()  # aizver skatu
    uzstadijumu_skats.pack(fill='both', expand=True)  # atver jautājumu skatu




# programmas loga izveide
window = tk.Tk()
window.title("Skaņas intervāli")
window.geometry("990x500")
window.resizable(False, False) 
mixer.init()

# ---------- Teksta kaste ----------#
teksta_kaste = tk.Frame(window, height=400)
teksta_kaste.pack(fill='both', expand=True)

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

uzraksts = tk.Label(sakuma_skats, text="Skaņas intervāli", font=('Verdana', 24, 'bold'), fg = '#800000')
uzraksts.pack(pady=(80, 40))

pogaUzstadijumi = tk.Button(sakuma_skats, text="Sesijas uzstādījumi", command=funkUzstadijumi, width=20, height=2, bg = 'lightgrey', fg = '#800000', font = ('Verdana', 12, 'bold'))
pogaUzstadijumi.pack(pady=10)

#------------------------------- kauliņa skats -------------------------------#
uzstadijumu_skats = tk.Frame(teksta_kaste)





# sāk Tkinter galveno cilpu
sakuma_skats.pack(fill='both', expand=True)
window.mainloop()