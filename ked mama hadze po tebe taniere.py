#naimportovanie modulov
import tkinter
import random
import math

#nastavenie platna
canvas = tkinter.Canvas(width="500", height="100", background="white")
canvas.pack()

#zadefinovanie zoznamov
pismena = ["A","B","C","D","E","F","G","H","I","J"]
kliknute = []

#vyzrebovanie zo zoznamu
puknuty = random.choice(pismena)

def vykreslenie(): #funkcia na vykreslenie tanierov
    #zadefinovanie globalnej premennej
    global puknuty_sur_x

    #nastavenie pociatocnych suradnic
    x = 0
    y = 25
    x1 = 10
    y1 = 35
    x2 = 25
    y2 = 50
    
    for i in pismena: #cyklus na prechadzanie hodnot v zozname
        #vykreslenie tanierov
        canvas.create_oval(x,y,x+50,y+50,fill="blue",tags=i)
        canvas.create_oval(x1,y1,x1+30,y1+30,outline="grey")
        canvas.create_text(x2,y2,text=i,font="Arial 20",fill="white")

        #podmienka na zistenie prvej suradnice puknuteho taniera
        if i == puknuty:
            puknuty_sur_x = canvas.coords(i)[0]

        #zmena suradnic
        x += 50
        x1 += 50
        x2 += 50

def vyber(suradnice): #funkcia na vybratie taniera
    #zadefinovanie globalnych premennych
    global x, zaok_x, puknuty_sur_x

    #nastavenie suradnic kliknutia
    x = suradnice.x
    y = suradnice.y

    def zaokruhlenie(): #funkcia na zaokruhlenie vybranej suradnice
        #zadefinovanie globalnych premennych
        global x, zaok_x

        #vypocet zaokruhlenia
        zaklad = 50
        zaok_x = zaklad * math.floor(x/zaklad)

    #privolanie funkcie 
    zaokruhlenie()

    for i in pismena: #cyklus na prechadzanie hodnot v zozname
        #priradenie prvej suradnice
        sur_x = canvas.coords(i)[0]

        #podmienka na vlozenie do zoznamu
        if zaok_x == sur_x:
            kliknute.append(i)

    #podmienka na spravnu y suradnicu
    if y >= 25 and y <= 75:
        #podmienka na zistenie ci oznaceny tanier je puknuty
        if zaok_x == puknuty_sur_x:
            #vymazanie platna
            canvas.delete("all")

            #vykreslenie finalneho textu 
            canvas.create_text(300,25,text="Gratulujem, označil si puknutý tanier!",fill="blue",font="Arial 15")

            #zistenie viackrat kliknutych tanierov
            duplikaty = set([item for item in kliknute if kliknute.count(item) > 1])

            #podmienka na vypisanie viackrat kliknutych tanierov
            if len(duplikaty) > 0:
                canvas.create_text(300,75,text="Viackrát si klikol na taniere "+"".join(duplikaty),fill="red",font="Arial 15")

            #zrusenie zistovania
            return

#zavolanie funkcie
vykreslenie()

#nabindovanie laveho tlacidla mysi na funkciu    
canvas.bind("<Button-1>",vyber)
