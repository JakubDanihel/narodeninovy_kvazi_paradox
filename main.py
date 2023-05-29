#importovanie kniznic
import datetime, random

def getNarodeniny(pocet_narodenin):
    #ziskanie zoznamu s poctom narodenin
    narodeniny = []

    for i in range(pocet_narodenin):
        #potrebne pre generovanie zoznamu narodenin. rok moze byt rozny. ale dni musia byt z rovnakeho roku
        zac_roka = datetime.date(2001, 1, 1)
        #generovanie nahodneho datumu
        nah_poc_dni = datetime.timedelta(random.randint(0, 364))
        narodenie = zac_roka + nah_poc_dni
        narodeniny.append(narodenie)
    return narodeniny

#porovnanie a urcenie rovnakych nahodnych datumov
def rovnake_narodeniny(narodeniny):
    #ak su vsetky cisla rozne vrati hodnotu none
    if len(narodeniny) == len(set(narodeniny)):
        return None
    
    #porovnanie kazdeho dna a urcenie ci su rovnake
    for a, narodenie_A in enumerate(narodeniny):
        for b, narodenie_B in enumerate(narodeniny[a + 1 :]):
            if narodenie_A == narodenie_B:
                return narodenie_A #vratenie zhodnych narodenin

MESIACE = ('Januar', 'Febuar', 'Marec', 'April', 'Maj', 'Jun', 'Jul', 'August', 'September', 'Oktober', 'November', 'December')

pocDni = 0

#cyklus bude bezat pokial nebude zadana spravna hodnota
while True:
    print("Zadaj pocet narodenin: ")
    pocet = input("=> ")
    if pocet.isdecimal() and (0 < int(pocet) <= 100):
        pocDni = int(pocet)
        print(type(pocDni))
        break

print()

#vypisanie poctu narodenin
print("Pocet narodenin je: ",pocDni)
narodeniny = getNarodeniny(int(pocDni))

for i, narodenie in enumerate(narodeniny):
    if i != 0:
        #zobraz ciarku za kazdym poctom narodenin
        print(', ', end = '')
        men_mesiac = MESIACE[narodenie.month - 1]
        datum_text = '{} {}'.format(men_mesiac, narodenie.day)
        print(datum_text, end = '')

print("")
print("")

#urci ci vsetky rovnake dni
rovnake = rovnake_narodeniny(narodeniny)
print("V tejto simulaci je pocet narodenin: ", end = "")
if rovnake != None:
    men_mesiac = MESIACE[narodenie.month - 1]
    datum_text = '{} {}'.format(men_mesiac, narodenie.day)
    print("pocet ludi co maju narodeniny v rovnaky den je: ", datum_text)
else:
    print("Nikto nema narodeniny v rovnaky den.")
print("")

#spustenie 100 000 simulacii
print("Generovanie ", pocDni, "nahodne narodeniny 100 000 krat")
input("Zadaj ENTER pre spustenie: ")

#spustenie dalsich 100 000 simulacii
sim_rovnake = 0 #kolko rovnakych simulaci maju v sebe rovnake narodeniny
for i in range(100_000):
    #vrat hodnotu kazdych 10 000 simulacii
    if i % 10_000 == 0:
        print("Pocet simulaci spustenych: ", i)
    narodeniny = getNarodeniny(pocDni)
    if rovnake_narodeniny(narodeniny) != None:
        sim_rovnake = sim_rovnake + 1

print("100 000 simulacii prebehlo.")

#vypisanie spravnych hodnot:
pravdepodobnost = round(sim_rovnake / 100_000*100, 2)
print("Zo 100 000 ma", pocDni, " ludi v ten isty den")
print("Nachadzalo sa tam ", sim_rovnake, " krat.")
print(pocDni, " ludi malo v rovnaky den narodeniny co je: ", pravdepodobnost, " %")
