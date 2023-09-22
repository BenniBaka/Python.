trust = 40
Chadness = 10
kort_kniv = 0
kjøkken_kniv = 0
spade = 0
baseball_kølle = 0
bue = 0
piler = 0
knyttnever = 2

def rom_1():
    print("du er på skeld og Red sier at han så deg vent selv om det var du som så han vent, og han kaller deg får en sussy baka, og nå er alle i crewet enig med red. hva gjør du?")
    valg = input("A: Løpe vekk for og prøve og gjømme deg B: Si, Red kinda SUS C: Gå til huset til Red og skru av nettet til han. -> ")
    if valg == "A":
        rom_2()
    if valg == "B":
        rom_3()
    if valg == "C":
        rom_4()

def rom_2():
    print("Du kan ikke løpe mens du er i et meeting, de ble voted ut, og Red vant.")

def rom_4():
    print("God ide, men møte gikk ut av tid mens du var på vei og du ente opp med og DØ!")

def rom_3():
    print("Alle ente opp med og vote Red og nå er det bare en imposter igjen. Nå er møte over og nå vet alle at du er snill, som betyr at den andre imposteren kommer til og prøve og drepe deg. Hva gjør du nå?")
    valg = input("A: Du holer deg med 2 eller flere crewmates B: Du prøver og løpe så langt vekk som mulig fra de andre, og du prøverog gjømme deg C: Du går til kjelleren til Shaman Durek for og spørre om guidence D: Du ringer Truls og Caller et emergency meeting. -> ")
    if valg == "A":
        rom_5()
    if valg == "D":
        rom_6()
    if valg == "B":
        rom_7()
    if valg == "C":
        rom_8()

def rom_5():
    print("Du ente opp med og gjøre ingen tasks fordi folkene var på cams, og imposteren drepte alle de andre rundt deg og vant.")


def rom_7():
    print("imposteren fant deg og drepte deg")


def rom_8():
    print("du kommer deg på en eller annen måte til the republic of Congo og spør Shaman Durek om visdom, men hanlagde uglesuppe av deg i stedet")


def rom_6():
    print("Du setter på høyrtaller slilk at Truls kan høre alle stemmene i møte, Truls gjennskjenner all stemmene siden han stalker alle barna i byen, Truls\
vet hvor alle barna bor så du får han til og løpe til alle kidsan sine hus for og og se hvem som er imposteren og siden det er kids dobbler han løpefarten sin som er like raskt som the flash\
og så kom han tilbake på 3,14 sekunder, men ingen av dem var imposteren, men det var en person han ikke hadde løpt til, og det var Svart AKA Shaman durek,\
han hadde ikke løpt dit fordi han er dypt inni jungelen i Congo. og siden alle andre er crewmates må shamanen skjølv være imposteren.")
    valg = input("imposteren var Black/Shaman Durek. Hva gjør du nå. A: Du sier black kinda SUS B: Du sier at vi burde gjøre ferdig tasks\
C: Du suer Shaman durek for illegal drug business med the cartel der han har solgt rundt 50Kg av 100% pure colombian cokecaine og rundt 20kg av black tar heroin og hans beste seller 100kg 99,67% pure crystal meth som har tatt heisenberg ut av business. -> ")
    if valg == "A":
        rom_9()
    if valg == "B":
        rom_10()
    if valg == "C":
        rom_11()

def rom_9():
    print("Du sier black kinda sus, og alle i hele game kaller deg for en rasict fordi det er 2023 og du blir cancelled på alle sosiale media appene du har")

def rom_10():
    print("Alle skipper og dere fortsetter og gjøre tasks.")
    print("Det er 2 tasks igjen men en av de døde står AFK og han har de 2 tasksan igjen så dere kan ikke vinne på tasks og reactor ble sabotert.")
    print("Hva gjør du nå?")
    valg = input("A: du leter helt til du finner en kropp. B: du du fikser reactor. C: Du ringer den som ikke har gjort tasksan sine på mobilen. D: Du infiltrerer basen til shaman durek.")
    if valg == "A":
        rom_16()
    if valg == "B":
        rom_17()
    if valg == "C":
        rom_18()
    if valg == "D":
        rom_19()


def rom_16():
    print("Du leter og leter, men finner ingen kropp helt til du ble en kropp.")


def rom_17():
    print("Du går til reactor og fikser den mens imposteren fikser glocken, PANG!")
    print("Shaman kom bakfra med glocken.")


def rom_18():
    print("Du ringer grønn og sier at han må gjøre tasksan sine")
    print("nå gjør han tasksan sine, men det er forskjent, reactor ble ikke fiksa")


def rom_19():
    print("Du ringer opp Roger sitt crew og sier at de må bli med til Congo for og få takk i Shaman Durek, og at de kommer til og bli rik av det.")
    print


def rom_11():
    print("Du ringer opp crewet til Roger som består av Roger, Håvard-baka, Truls og slavene deres og du får dem til og tracke lokasjonen til shaman durek, men de klarte ikke det, fordi det går ikke ann og tracke lokkasjonen til shaman durek, viss ikke man bruker unethical ways.\
hva gjør du nå?")
    valg = input("A: du går inn i en dark alley for og finne en local crack-head for og høre hvor han for drugsan sine fra B: du repoterer Shaman durek til govermentet av congo. C: du challenger shaman durek til hand to hand combat. D: Du ringer shaman durek på discord. -> ")
    if valg == "A":
        rom_12()
    if valg == "B":
        rom_13()
    if valg == "C":
        rom_14()
    if valg == "D":
        rom_15()


def rom_12():
    print("Du går ned mellom husene til osama bin ladin og nikocado acocado og ser en svart skillese i mørke og det ser ut som om han sniffer meth")

def rom_13():
    print("De leter i to uker men finner ingen hint om shaman durek, men shaman durek finnner deg.")

def rom_14():
    print("Siden shaman durek har en stor banan så har han ingen valg anna enn og akseptere challengen din.")

def rom_15():
    global trust
    print("Du ringer shaman banan")
    print("Han svarer, hva gjør du nå?")
    valg = input("A: Du tracker hans eksakte lokasjon via og se hvor dekningen hans kommer fra og du sender Truls sine slaver for og ta han ned. B: Du sier at han må komme til Sindres magiske kjeller. C: Du sier at han må komme på besøk for og få en suprise.\
D: Du sier at han må møte Gustavo for og conducte business med los buornos hermanos og at Gus sier at han må kjappe seg")
    if valg == "A":
        rom_20()
    if valg == "B":
        rom_21()
    if valg == "C":
        rom_22()
    if valg == "D":
        trust += 30
        rom_23()
    

def rom_20():
    print("Man kan ikke ikke tracke lokasjonen til Shaman Durek med og finne ut av hvor dekningen hans kommer i fra fordi han bruker ikke dekning han bruker potetsalat som wifi.")
    

def rom_21():
    global trust
    print("Shaman Durek lurer på hvorfor.")
    print("Hva skal du si?")
    valg = input("A: Du sier at Sindre kunne bare gi informasjonen til Shaman Durek og at du måtte komme til basemanten hannes får og finne ut. B: Du sier at han må komme for og starte opp en Minecraft server som kommer til og gjøre dem rik.\
C: Du sier at han Sindre har lyst til at Shaman og han skal joine Håvard sin kjeller -> ")
    if valg == "A":
        trust -= 30
    print(f"Nå er shaman durek på vei til Sindre's magiske kjeller og du har {trust} trust. Hva gjør du nå?")
    valg = input("A: Si ifra til Sindre at han må gjøre klar kjelleren B: Se på youtube.")
    if valg == "A":
        rom_24()
    if valg == "B":
        rom_game_over()


    if valg == "B":
        trust -= 10
    print(f"Nå er shaman durek på vei til Sindre's magiske kjeller og du har {trust} trust. Hva gjør du nå?")
    valg = input("A: Si ifra til Sindre at han må gjøre klar kjelleren B: Se på youtube.")
    if valg == "A":
        rom_24()
    if valg == "B":
        rom_game_over()


    if valg == "C":
        trust += 10
    print(f"Nå er shaman durek på vei til Sindre's magiske kjeller og du har {trust} trust. Hva gjør du nå?")
    valg = input("A: Si ifra til Sindre at han må gjøre klar kjelleren B: Se på youtube.")
    if valg == "A":
        rom_24()
    if valg == "B":
        rom_game_over()



def rom_22():
    global trust
    trust -= 20
    print("Han aksepterer og komme på besøk og han er på vei")
    valg = input("")



def rom_23():
    global trust
    print(f"Shaman spørr ingen spørsmål og han er kjapt på vei og du har {trust} trust. Hva gjør du nå?")
    valg = input("A: Si ifra til Sindre at han må gjøre klar kjelleren B: Se på youtube.")
    if valg == "A":
        rom_24()
    if valg == "B":
        rom_game_over()


def rom_24():
    print ("Mens han er på vei sier du ifra til Sindre, og han gjør klar crewet og kjelleren, i mellom tiden ringer du politiet og sier at Shaman Durek er på vei, Du må ta deg et våpen viss han angriper deg.\
Hva velger du?")
    valg = input("A: Kort kniv. B: kjøkken kniv. C: spade. D: baseball-kølle. E: Bue med 5 piler. F: Knyttnever")
    if valg == "A":
        rom_Kort_kniv()
    if valg == "B":
        rom_Kjøkken_kniv()
    if valg == "C":
        rom_Spade()
    if valg == "D":
        rom_Baseball_kølle()
    if valg == "E":
        rom_Pil_og_bue()
    if valg == "F":
        rom_knyttnever()


def rom_Kort_kniv():
    global kort_kniv
    kort_kniv += 1
    if kort_kniv == 1: print("Du har nå 1 kort kniv og du drar ned i Sindre sin magiske kjeller og der er Sindre, Oompaville, Doge og politiet som er gjømt i basementen.\
Shaman Durek texter deg på discord og sier at han er der vi skulle møtes. Du texter han og sier at du er der om 1 minutt. Du sier at Shaman Durek er hær til politiet og at de må være klare med gunsa når\
Shaman Durek kommer ned, men de må vente til vi kunne exspose han for crimesan hannes og når vi gjorde det kan de komme ut. Du går ut og der er Shaman Durek, du tar han med ned til Sindre sin magiske kjeller.\
Shaman Durek tar en bag på på bordet og det er 20kg av 100% pure meth som han nettopp kom opp med en formula på og ingen andre på markede har dette og han sier at 1 kg selles for 2 mill\
og han spørr om vi vil joine han og Gustavo fring med og selle dette og bli rike i lag. Hva gjør du nå?")
    valg = input("A: Joine Shaman Durek og må slåss mot politiet. B: Betray Shaman Durek og la politier arrester han.")
    if valg == "A":
        rom_join()
    if valg == "B":
        rom_betray()
    if kort_kniv == 2: print("Du har nå 2 korte kniver og du drar ned i Sindre sin magiske kjeller og der er Sindre, Oompaville, Doge og politiet som er gjømt i basementen.\
Shaman Durek texter deg på discord og sier at han er der vi skulle møtes. Du texter han og sier at du er der om 1 minutt. Du sier at Shaman Durek er hær til politiet og at de må være klare med gunsa når\
Shaman Durek kommer ned, men de må vente til vi kunne exspose han for crimesan hannes og når vi gjorde det kan de komme ut. Du går ut og der er Shaman Durek, du tar han med ned til Sindre sin magiske kjeller.\
Shaman Durek tar en bag på på bordet og det er 20kg av 100% pure meth som han nettopp kom opp med en formula på og ingen andre på markede har dette og han sier at 1 kg selles for 2 mill\
og han spørr om vi vil joine han og Gustavo fring med og selle dette og bli rike i lag. Hva gjør du nå?")
    valg = input("A: Joine Shaman Durek og må slåss mot politiet. B: Betray Shaman Durek og la politier arrester han.")
    if valg == "A":
        rom_join()
    if valg == "B":
        rom_betray()



def rom_Kjøkken_kniv():
    global kjøkken_kniv
    kjøkken_kniv += 1
    print("Du har nå 1 kjøkken-kniv og du drar ned i Sindre sin magiske kjeller og der er Sindre, Oompaville, Doge og politiet som er gjømt i basementen.\
Shaman Durek texter deg på discord og sier at han er der vi skulle møtes. Du texter han og sier at du er der om 1 minutt. Du sier at Shaman Durek er hær til politiet og at de må være klare med gunsa når\
Shaman Durek kommer ned, men de må vente til vi kunne exspose han for crimesan hannes og når vi gjorde det kan de komme ut. Du går ut og der er Shaman Durek, du tar han med ned til Sindre sin magiske kjeller.\
Shaman Durek tar en bag på på bordet og det er 20kg av 100% pure meth som han nettopp kom opp med en formula på og ingen andre på markede har dette og han sier at 1 kg selles for 2 mill\
og han spørr om vi vil joine han og Gustavo fring med og selle dette og bli rike i lag. Hva gjør du nå?")
    valg = input("A: Joine Shaman Durek og må slåss mot politiet. B: Betray Shaman Durek og la politier arrester han.")
    if valg == "A":
        rom_join()
    if valg == "B":
        rom_betray()



def rom_Spade():
    global spade
    spade += 1
    print("Du har nå 1 spade og du drar ned i Sindre sin magiske kjeller og der er Sindre, Oompaville, Doge og politiet som er gjømt i basementen.\
Shaman Durek texter deg på discord og sier at han er der vi skulle møtes. Du texter han og sier at du er der om 1 minutt. Du sier at Shaman Durek er hær til politiet og at de må være klare med gunsa når\
Shaman Durek kommer ned, men de må vente til vi kunne exspose han for crimesan hannes og når vi gjorde det kan de komme ut. Du går ut og der er Shaman Durek, du tar han med ned til Sindre sin magiske kjeller.\
Shaman Durek tar en bag på på bordet og det er 20kg av 100% pure meth som han nettopp kom opp med en formula på og ingen andre på markede har dette og han sier at 1 kg selles for 2 mill\
og han spørr om vi vil joine han og Gustavo fring med og selle dette og bli rike i lag. Hva gjør du nå?")
    valg = input("A: Joine Shaman Durek og må slåss mot politiet. B: Betray Shaman Durek og la politier arrester han.")
    if valg == "A":
        rom_join()
    if valg == "B":
        rom_betray()



def rom_Baseball_kølle():
    global baseball_kølle
    baseball_kølle += 1 
    print("Du har nå 1 baseball-kølle og du drar ned i Sindre sin magiske kjeller og der er Sindre, Oompaville, Doge og politiet som er gjømt i basementen.\
Shaman Durek texter deg på discord og sier at han er der vi skulle møtes. Du texter han og sier at du er der om 1 minutt. Du sier at Shaman Durek er hær til politiet og at de må være klare med gunsa når\
Shaman Durek kommer ned, men de må vente til vi kunne exspose han for crimesan hannes og når vi gjorde det kan de komme ut. Du går ut og der er Shaman Durek, du tar han med ned til Sindre sin magiske kjeller.\
Shaman Durek tar en bag på på bordet og det er 20kg av 100% pure meth som han nettopp kom opp med en formula på og ingen andre på markede har dette og han sier at 1 kg selles for 2 mill\
og han spørr om vi vil joine han og Gustavo fring med og selle dette og bli rike i lag. Hva gjør du nå?")
    valg = input("A: Joine Shaman Durek og må slåss mot politiet. B: Betray Shaman Durek og la politier arrester han.")
    if valg == "A":
        rom_join()
    if valg == "B":
        rom_betray()



def rom_Pil_og_bue():
    global bue
    global piler
    bue += 1
    piler += 5
    print("Du har nå 1 bue og 5 piler og du drar ned i Sindre sin magiske kjeller og der er Sindre, Oompaville, Doge og politiet som er gjømt i basementen.\
Shaman Durek texter deg på discord og sier at han er der vi skulle møtes. Du texter han og sier at du er der om 1 minutt. Du sier at Shaman Durek er hær til politiet og at de må være klare med gunsa når\
Shaman Durek kommer ned, men de må vente til vi kunne exspose han for crimesan hannes og når vi gjorde det kan de komme ut. Du går ut og der er Shaman Durek, du tar han med ned til Sindre sin magiske kjeller.\
Shaman Durek tar en bag på på bordet og det er 20kg av 100% pure meth som han nettopp kom opp med en formula på og ingen andre på markede har dette og han sier at 1 kg selles for 2 mill\
og han spørr om vi vil joine han og Gustavo fring med og selle dette og bli rike i lag. Hva gjør du nå?")
    valg = input("A: Joine Shaman Durek og må slåss mot politiet. B: Betray Shaman Durek og la politier arrester han.")
    if valg == "A":
        rom_join()
    if valg == "B":
        rom_betray()



def rom_knyttnever():
    global Chadness
    Chadness += 50
    print("Du har ingen våpen annet enn 2 knyttnever og du drar ned i Sindre sin magiske kjeller og der er Sindre, Oompaville, Doge og politiet som er gjømt i basementen.\
Shaman Durek texter deg på discord og sier at han er der vi skulle møtes. Du texter han og sier at du er der om 1 minutt. Du sier at Shaman Durek er hær til politiet og at de må være klare med gunsa når\
Shaman Durek kommer ned, men de må vente til vi kunne exspose han for crimesan hannes og når vi gjorde det kan de komme ut. Du går ut og der er Shaman Durek, du tar han med ned til Sindre sin magiske kjeller.\
Shaman Durek tar en bag på på bordet og det er 20kg av 100% pure meth som han nettopp kom opp med en formula på og ingen andre på markede har dette og han sier at 1 kg selles for 2 mill\
og han spørr om vi vil joine han og Gustavo fring med og selle dette og bli rike i lag. Hva gjør du nå?")
    valg = input("A: Joine Shaman Durek og må slåss mot politiet. B: Betray Shaman Durek og la politier arrester han.")
    if valg == "A":
        rom_join()
    if valg == "B":
        rom_betray()



def rom_betray():
    print


def rom_join():
    print



def rom_game_over():
    print("trodde du faktisk at det var det riktige valget, Stupid")
    valg = input("Du tapte. vil du starte på nytt. ja eller nei")
    if valg == "ja":
        rom_1
    if valg == "nei":
        print("Dårlig")
    else:
        print("bor, du skal type ja eller nei din bimbo.")



if trust <= 0:
    trust = 0




rom_1()