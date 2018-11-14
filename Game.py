from Struktura import Struktura
from Player import Player
import os
import Code
import Addons


FILE_NAME = ["1.txt", "2.txt", "3.txt", "boss.txt", "weapon.txt"]
for i in FILE_NAME:
    if not os.path.isfile(i):
        input("Brak pliku " + i)
        exit(0)

Addons.print_welcome()

while True:
    sec = 0.08
    Addons.menu(sec)
    print("\nPodaj numer opcji")
    x = input(">>>")
    os.system('cls')
    if x == '2':
        Addons.score_table()

    elif x == '3':
        Addons.credits()

    elif x == '4':
        quit(0)
    elif x == '1':
        while True:
            os.system('cls')
            print("Jesteś gotowy na przygodę?\n")
            print("Wybierz poziom trudności (1/2/3)\n")
            print("1. Łatwy")
            print("2. Normalny")
            print("3. Trudny")
            difficulty = input(">>>")

            if difficulty in ["1", "2", "3"]:
                difficulty = int(difficulty)
                break

        Code.generate(difficulty + 2)

        while True:
            os.system('cls')
            print("Wybierz klasę (1/2/3)\n")
            print("1. Wojownik")
            print("2. Mag")
            print("3. Łotrzyk")
            klasa = input(">>>")

            if klasa == "1":
                player = Player((4 - int(difficulty)) * 60)
                player.add_weapon("Noga", 16, 99, 5, "Kopnięcie przeciwnika")
                player.add_weapon("Miecz pazia", 40 - (difficulty - 1) * 5, 70 - (difficulty - 1) * 5, 5, "Cios mieczem pazia")
                player.add_armor("Zardzewiała zbroja", 15)
                break

            elif klasa == "2":
                player = Player((4 - int(difficulty)) * 40)
                player.add_weapon("Ręce", 16, 99, 5, "Proste zaklęcie rażące")
                player.add_weapon("Dębowa różdżka", 50 - (difficulty - 1) * 5, 80 - (difficulty - 1) * 5, 15, "Silne zaklęcie oszałamiające")
                player.add_armor("Stara szata", 5)
                break

            elif klasa == "3":
                player = Player((4 - int(difficulty)) * 50)
                player.add_weapon("Ręka", 16, 99, 5, "Sierpowy")
                player.add_weapon("Sztylet złodziejaszka", 40 - (difficulty - 1) * 5, 75 - (difficulty - 1) * 5, 10,"Cios sztyletem")
                player.add_armor("Skurzana tunika", 10)
                break

        player.load_names(int(klasa))
        stru = Struktura(klasa + ".txt")

        # wczytywanie obrazka z bossem
        Code.boss_name = ['Deathwing', 'Czarnoksieznik', 'Ksiezniczka'][int(klasa) - 1]
        Code.boss_pict = ""
        with open("boss.txt", "r") as f:
            tmp = 0
            for line in f:
                if line[:3] == "x x":
                    tmp += 1
                if tmp > int(klasa) * 2:
                    break
                if tmp > int(klasa) * 2 - 2:
                    Code.boss_pict += line
        f.close()

        while True:
            stru.p_move(player)
            if stru.end or player.dead:
                break

        while True:
            os.system('cls')
            print("Zagrać ponownie? (t/n)")
            p = input(">>>")

            if p.upper() == "T":
                break

            if p.upper() == "N":
                exit(0)

            else:
                print("Zła wartość!\n")
    else:
        sec = 0
