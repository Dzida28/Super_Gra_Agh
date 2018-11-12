# -*- coding: utf-8 -*-
import random
import os
import Code
import Addons


class Action:
    def __init__(self):
        self.description = []
        self.description2 = []
        self.exp = []
        self.damage = []
        self.encounter = []
        self.done = []

    def add_action(self, description, description2, exp, damage, encounter):
        self.description.append(description)
        self.description2.append(description2)
        self.exp.append(exp)
        self.damage.append(damage)
        self.encounter.append(encounter)
        self.done.append(False)

    def randomize(self):
        all = list(zip(self.description, self.description2, self.exp, self.damage, self.encounter))
        random.shuffle(all)

        self.description, self.description2, self.exp, self.damage, self.encounter = map(list, zip(*all))

    def print_actions(self):
        print("-"*20)
        print("\n0. Anuluj")
        for i in range(len(self.description)):
            print(str(i+1) + ". " + self.description[i])

    def do_action(self, player, room, room_id):
        while not all(self.done):
            num = -1

            while not (0 <= num < len(self.description) + 1 and not self.done[num - 1]):
                os.system('cls')
                room.introduce(room_id, 0)
                self.print_actions()
                print("\nPodaj numer akcji: ")
                num = input(">>>")
                try:
                    num = int(num)
                except ValueError:
                    Addons.slow_print("Wpisz cyfrę dzbanie!", 0.01)
                    Addons.slow_print("XD!\n\n", 0.5)
                    num = -1

                if num == 0:
                    break

            if num != 0:
                # tablica jest od zera wiec trzeba zmniejszyc
                num -= 1

                print("\n...")
                Addons.slow_print(self.description2[num], 0.01)
                self.done[num] = True
                self.description[num] = "*Wykonano*"

                if self.encounter[num][:4] == "Code":
                    Addons.slow_print(Code.get_rand_num(), 0.05)

                if self.encounter[num][:4] == "Item":
                    if random.randint(1, len(player.available_armors) + len(player.available_weapons)) + 1 > len(player.available_armors):
                        player.add_random_weapon()
                    else:
                        player.add_random_armor()

                if self.exp[num] > 0:
                    player.update_lvl(self.exp[num])

                if abs(self.damage[num]) > 0:
                    player.update_hp(self.damage[num])
                    if player.dead:
                        break

                if self.encounter[num][:4] not in ["None", "Item", "Code"]:
                    Addons.slow_print(self.encounter[num] + " atakuje Cię!", 0.01)
                    input("\nWciśnij ENTER, aby kontunuować...")
                    player.attack(self.encounter[num], random.randint(5 + player.lvl, 9 + player.lvl) * 10)
                    if player.dead:
                        break

                print("...\n")

                input("\nWciśnij ENTER, aby kontunuować...")
            else:
                break
