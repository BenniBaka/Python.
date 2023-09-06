import random

tilfeldig_tall = random.randint(1,100)


gjett = input("Skriv ett tall fra 1 til 100 -> ")

if gjett == tilfeldig_tall:
    print("riktig")
else: print("feil")
