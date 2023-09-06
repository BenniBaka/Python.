print("du er på skeld og Red sier at han så deg vent selv om det var du som så han vent, og han kaller deg får en sussy baka, og nå er alle i crewet enig med red. hva gjør du? ")

valg = input("A: Løpe vekk for og prøve og gjømme deg B: Si, Red kinda SUS C: Gå til huset til Red og skru av nettet til han -> ")

if valg == "A":
    print("Du kan ikke løpe mens du er i et meeting, de ble voted ut, og Red vant")


if valg == "C":
    print("God ide, men møte gikk ut av tid mens du var på vei og du ente opp med og DØ!")

if valg == "B":
    print("Alle ente opp med og vote Red og nå er det bare en imposter igjen")
    print("Nå er møte over og nå vet alle at du er snill, som betyr at den andre imposteren kommer til og prøve og drepe deg. Hva gjør du nå?")
valg = input("A: Du holer deg med 2 eller flere crewmates. B: Du prøver og løpe så langt vekk som mulig fra de andre får og gjømme deg C: Du går til kjelleren til Shaman Durek for og spørre om guidence D: Du ringer Truls og Caller et emergency meeting.")


def rom_1():
    print("du er på skeld og Red sier at han så deg vent selv om det var du som så han vent, og han kaller deg får en sussy baka, og nå er alle i crewet enig med red. hva gjør DU?")
    valg = input("A: Løpe vekk for og prøve og gjømme deg B: Si, Red kinda SUS C: Gå til huset til Red og skru av nettet til han -> ")
    if valg == "A":
        rom_2("Du kan ikke løpe mens du er i et meeting, de ble voted ut, og Red vant. Nå er møte over og nå vet alle at du er snill, som betyr at den andre imposteren kommer til og prøve og drepe deg. Hva gjør du nå?")
    if valg == "B":
        rom_3("Alle ente opp med og vote Red og nå er det bare en imposter igjen")
    if valg == "C":
        rom_4("God ide, men møte gikk ut av tid mens du var på vei og du ente opp med og DØ!")

def rom_3():
    print("A: Du holr på der deg med 2 eller flere crewmates  B: Du prøver og løpe så langt vekk som mulig fra de andre, og du prøver og gjømme deg C: Du går til kjelleren til Shaman Durek for og spørre om guidence D: Du ringer Truls og Caller et emergency meeting.")
    print("Du settehøyraller slilk at Truls kan høre alle stemmene i møte, Truls gjennskjenner all stemmene siden han stalker alle barna i byen, Truls vet hvor alle barna bor så du får han til og løpe til alle kidsan sine hus får og se hvem som er imposteren")
    input