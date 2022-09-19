import tkinter
canvas = tkinter.Canvas(width='600', height='300', bg='white')
canvas.pack() #naimportujem si knižnicu tkinter aby som mohol kresliť na plátno

poc_rad = 10 #premenna s poctom stlpcov
vel = 40 #velkost jedneho miesta
x, y = 50, 50 #premenna na vykreslenie do canvasu
pocitadlo = 0 #premenna na pocitanie miest
farba = 'lime' #premenna na zelenu farbu
zoznam = [1]*40 #zoznam na zaznamenanie obsadenosti urcitych miest
vol, obs, vol_stred = 40, 0, 20 #premenna na pociatnie volny, obsadenych a volnych miest v ulicke

def prefarbi(miesto, farba): #funkcia na zmenenie farby danych miest
    canvas.itemconfig('s'+str(miesto), fill=farba) #zmena farby danemo miesta
    canvas.itemconfig('volne', text='Počet volných miest: '+str(vol)) #aktualizuje pocet volnych miest
    canvas.itemconfig('obsadene', text='Počet obsadených miest: '+str(obs)) #aktualizuje pocet obsadenych miest
    canvas.itemconfig('volny_s', text='Počet volných miest v uličke: '+str(vol_stred)) #aktualizuje pocet volnych miest v ulicke
    
def vykresli(): #funkcia na vykreslenie miest a textu
    global x, y, pocitadlo #zadefinovanie premennych ako globalne aby som ich mohol vo funkcii upravovat
    for i in range(poc_rad): #for cyklus pomocou ktoreho budem posuvat suradnice po x-ovej osi
        for j in range(4): #for cyklus pomocou ktoreho budem posuvat suradnice po y-ovej osi
            pocitadlo += 1 #zvacsim pocitadlo kazdym prejdenim for cyklu
            canvas.create_rectangle(x+i*vel, y+j*vel, x+(i+1)*vel-10, y+(j+1)*vel-10, tags='s'+str(pocitadlo), fill=farba) #vykreslim stvorec s danymi vlastnostami
            canvas.create_text(x+(i+1)*vel-25, y+(j+1)*vel-25, text=str(pocitadlo), font='Arial 10 bold') #vykreslim cisla do nakreslenych stvorcov
            canvas.create_text(100, 220, text='Počet volných miest: '+str(vol), tags='volne') #vypisem pocet volnych miest 
            canvas.create_text(100, 250, text='Počet obsadených miest: '+str(obs), tags='obsadene') #vypisem pocet obsadenych miest 
            canvas.create_text(100, 280, text='Počet volných miest v uličke: '+str(vol_stred), tags='volny_s') #vypisem pocet volnych miest v ulicke 
            
def klik(event): #funkcia na kliknutie mysou na dane miesto
    global vol, obs, vol_stred #zadefinovanie premennych ako globalne aby som ich mohol vo funkcii upravovat
    if (x<event.x<x+vel*poc_rad and y<event.y<y+vel*4): #podmienka if na zistenie ci sme klikli niekde v priestore vykreslenych stvorcov
        x1 = (event.x - x) // vel #pomocou vypoctu zistim na ktoru kocku z lava som klikol
        y1 = (event.y - y) // vel #pomocou vypoctu zistim na ktoru kocku z zhora som klikol
        miesto = x1*4+y1+1 #zistim presne cislo kocky na ktoru som klikol
        if zoznam[miesto-1]==1:#podmienkou if zistim zo zoznamu ci je dana kocka volna a ak ano zmenim ju v zozname za obsadenu a prefarbim na cerveno
            obs += 1 #zmenim pocet obsadenych miest o 1 viac
            if y1==1 or y1==2: #pomocou ifu zistim ci ide o miesto pri ulicke
                vol_stred -= 1 #zmensim pocet volnych miest v ulicke o 1
            elif y1==0 or y1==3: #pomocou ifu zistim ci ide o miesto nie pri ulicke
                vol -= 1 #zmensim pocet volnych miest nie v ulicke o 1
            zoznam[miesto-1] = 0 #zmenim danu kocku na obsadenu pomocou nuly
            prefarbi(miesto, 'red') #zmenim jej farbu zo zelenej na cervenu
        elif zoznam[miesto-1]==0: #podmienkou if zistim zo zoznamu ci je dana kocka obsadena a ak ano zmenim ju v zozname za volnu a prefarbim na zeleno
            obs -= 1 #zmenim pocet obsadenych miest o 1 menej
            if y1==1 or y1==2: #pomocou ifu zistim ci ide o miesto pri ulicke
                vol_stred += 1 #zvacsim pocet volnych miest v ulicke o 1
            elif y1==0 or y1==3: #pomocou ifu zistim ci ide o miesto nie pri ulicke
                vol += 1 #zvacsim pocet volnych miest nie v ulicke o 1
            zoznam[miesto-1] = 1 #zmenim danu kocku na volnu pomocou jednotky
            prefarbi(miesto, 'lime') #zmenim jej farbu z cervenej na zelenu

vykresli() #zavolam funkciu vykresli 
canvas.bind('<Button-1>', klik) #nabindujem lave tlacitko mysi a po jeho stlaceni sa spusti funkcia klik
