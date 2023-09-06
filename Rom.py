hp = 100    

def rom_1():
    print("")
    valg = input("")
    if valg == "A":
        rom_2()
    if valg == "B":
        rom_3()

def rom_2():
    global hp
    print("")
    hp -= 30
    print("")
    rom_1

    if hp <=0:
        game_over()

    rom_1()

def rom_3():
    print("")

def game_over():
    print("")
    exit()

rom_1()


