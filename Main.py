navn = input("Hva heter du? -> ")
alder = input("Hvor gammel er du? -> ")
 
print("Hei " + navn + ", så hyggelig å snakke med deg. Du er", alder, "år")
 
alder = int(alder)

if alder >= 18:
    print("Du er over 18")
 
print("Om 100 år er du ", alder + 100, " år.")
