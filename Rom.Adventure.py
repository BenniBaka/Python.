hp = 100
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
    print("Alle ente opp med og vote Red og nå er det bare en imposter igjen. Nå er møte over og nå vet alle at du er snill\
som betyr at den andre imposteren kommer til og prøve og drepe deg. Hva gjør du nå?")
    valg = input("A: Du holer deg med 2 eller flere crewmates B: Du prøver og løpe så langt vekk som mulig fra de andre, og du prøver\
og gjømme deg C: Du går til kjelleren til Shaman Durek for og spørre om guidence D: Du ringer Truls og Caller et emergency meeting. -> ")
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
og så kom han tilbake på 0,593 sekunder, men ingen av dem var imposteren, men det var en person han ikke hadde løpt til, og det var Svart AKA Shaman durek,\
han hadde ikke løpt dit fordi han er dypt inni jungelen i Congo. og siden alle andre er crewmates må shamanen skjølv være imposteren.")
    valg = input("imposteren var Black/Shaman Durek. Hva gjør du nå. A: Du sier black kinda SUS B: Du sier at vi burde gjøre ferdig tasks\
    C: Du suer Shaman durek for illegal drug business med the cartel der han har solgt rundt 50Kg av 100% pure colombian cokecaine og rundt 20kg av black tar heroin og hannes beste seller 100kg 99,67% pure crystal meth som har tatt heisenberg ut av business. -> ")
    if valg == "A":
        rom_9()
    if valg == "B":
        rom_10()
    if valg == "C":
        rom_11()

def rom_9():
    print("Du sier black kinda sus, og alle i hele game kaller deg for en rasict fordi det er 2023 og du blir cancelled på alle sosiale media appene du har")

def rom_10():
    print("Alle skipper og dere fortsetter og gjøre tasks")


def rom_11():
    print("Du ringer opp crewet til Roger som består av Roger, Håvard-baka og Truls og du får dem til og tracke lokasjonen til shaman durek, men de kalrte ikke det, fordi det går ikke ann og tracke lokkasjonen til shaman durek, viss ikke man bruker unethical ways.\
hva gjør du nå?")
    input("A: du går inn i en dark alley for og finne en local crack-head for og høre hvor han for drugsan sine fra B: du repoterer Shaman durek til govermentet av congo. C: du challenger shaman durek til hand to hand combat. Du ringer shaman durek på discord. -> ")

def rom_12():
    pass






rom_1()
if hp <=0:
    print("Shit, du døde, Skill-isue")