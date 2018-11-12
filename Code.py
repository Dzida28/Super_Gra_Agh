# -*- coding: utf-8 -*-
import random as r
import os
import Addons

code = ""
unknown = []
boss_name = ""
boss_pict = ""


def generate(amount):
    global code
    global unknown
    code = ""
    unknown = []
    for i in range(amount):
        code += str(r.randint(1, 9))

    for i in range(len(code)):
        unknown.append("*" * i + code[i] + "*" * (len(code) - i - 1))


def get_rand_num():
    global unknown
    if len(unknown) > 0:
        num = r.choice(unknown)
        unknown.remove(num)
        return "\"Kod: " + num + "\"\n"
    else:
        return "Kod: " + code


def return_known_code():
    know = list(code)

    for i in unknown:
        for x in range(len(i)):
            if i[x] != "*":
                know[x] = "*"
                break
    know = "".join(know)
    return know


def ending(player):
    while True:
        os.system('cls')
        print("-" * 20)
        print("Przed Tobą znajdują się duże wrota otwierane kodem, a za Tobą portal.\n\n")
        print("Co robisz? (1/2)\n")
        print("1. Próbujesz wpisać kod")
        print("2. Wchodzisz do portalu")
        p = input(">>>")

        if p == "1":
            if guess(player) == 1:
                return 1

        elif p == "2":
            print("Portal przenosi Cię do pokoju startowego.\n\n")
            input("\nWciśnij ENTER, aby kontunuować...")
            return 0


def guess(player):
    print("\nPodaj kod")
    code1 = input(">>>")

    if code == code1:
        print("Podałeś właściwy szyfr.")
        Addons.slow_print("Wrota otwierają się\n" + boss_name + " chce pożreć Twoją duszę!", 0.01)
        Addons.slow_print(boss_pict, 0.0001)
        input("\nWciśnij ENTER, aby kontunuować...")

        player.attack(boss_name, r.randint(8 + player.lvl, 13 + player.lvl) * 10)
        if not player.dead:
            Addons.print_congrats()
            print("\nKONIEC GRY")
            player.save_score()
            input("\nWciśnij ENTER, aby kontunuować...")
        os.system('cls')
        return 1

    else:
        print("\nZły kod.\nZ podłogi wysuwają się kłujące kolce.\n")
        player.update_hp(10)
        input("\nWciśnij ENTER, aby kontunuować...")
        return 0
