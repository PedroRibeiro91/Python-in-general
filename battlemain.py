from pkmclass import Pokemon
from pkmclass import Charizard
from pkmclass import Blastoise
from pkmclass import Venasaur
import time
import sys
import random

def slowprint(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)


def battle(pokemon1, pokemon2):
    while pokemon1.gethp() > 0 and pokemon2.gethp() > 0: # while both have hp
        if pokemon1.getspeed() > pokemon2.getspeed():
            slowprint(pokemon1.getname() + " attacks")
            print()
            if pokemon1.type_advantage(pokemon2) == 2:
                slowprint("It's super effective!!")
                print()
            elif pokemon1.type_advantage(pokemon2) == 1:
                slowprint("Some damage was dealt")
                print()
            else:
                slowprint("It's not very effective...")
                print()
            pokemon2.hp -= pokemon1.type_advantage(pokemon2) * pokemon1.get_attack() - pokemon2.get_defense()
            slowprint(pokemon2.getname() + " attacks")
            print()
            if pokemon2.type_advantage(pokemon1) == 2:
                slowprint("It's super effective!!")
                print()
            elif pokemon2.type_advantage(pokemon1) == 1:
                slowprint("Some damage was dealt")
                print()
            else:
                slowprint("It's not very effective...")
                print()
            pokemon1.hp -= pokemon2.type_advantage(pokemon1) * pokemon2.get_attack() - pokemon1.get_defense()
        elif pokemon2.getspeed() > pokemon1.getspeed():
            slowprint(pokemon2.getname() + " attacks")
            print()
            if pokemon2.type_advantage(pokemon1) == 2:
                slowprint("It's super effective!!")
                print()
            elif pokemon2.type_advantage(pokemon1) == 1:
                slowprint("Some damage was dealt")
                print()
            else:
                slowprint("It's not very effective...")
                print()
            pokemon1.hp -= pokemon2.type_advantage(pokemon1) * pokemon2.get_attack() - pokemon1.get_defense()
            slowprint(pokemon1.getname() + " attacks")
            print()
            if pokemon1.type_advantage(pokemon2) == 2:
                slowprint("It's super effective!!")
                print()
            elif pokemon1.type_advantage(pokemon2) == 1:
                slowprint("Some damage was dealt")
                print()
            else:
                slowprint("It's not very effective...")
                print()
            pokemon2.hp -= pokemon1.type_advantage(pokemon2) * pokemon1.get_attack() - pokemon2.get_defense()
        else:
            tie = random.random()
            if tie > 0.5:
                slowprint(pokemon2.getname() + " attacks")
                print()
                if pokemon2.type_advantage(pokemon1) == 2:
                    slowprint("It's super effective!!")
                    print()
                elif pokemon2.type_advantage(pokemon1) == 1:
                    slowprint("Some damage was dealt")
                    print()
                else:
                    slowprint("It's not very effective...")
                    print()
                pokemon1.hp -= pokemon2.type_advantage(pokemon1) * pokemon2.get_attack() - pokemon1.get_defense()
                slowprint(pokemon1.getname() + " attacks")
                print()
                if pokemon1.type_advantage(pokemon2) == 2:
                    slowprint("It's super effective!!")
                    print()
                elif pokemon1.type_advantage(pokemon2) == 1:
                    slowprint("Some damage was dealt")
                    print()
                else:
                    slowprint("It's not very effective...")
                    print()
                pokemon2.hp -= pokemon1.type_advantage(pokemon2) * pokemon1.get_attack() - pokemon2.get_defense()
            else:
                slowprint(pokemon1.getname() + " attacks")
                print()
                if pokemon1.type_advantage(pokemon2) == 2:
                    slowprint("It's super effective!!")
                    print()
                elif pokemon1.type_advantage(pokemon2) == 1:
                    slowprint("Some damage was dealt")
                    print()
                else:
                    slowprint("It's not very effective...")
                    print()
                pokemon2.hp -= pokemon1.type_advantage(pokemon2) * pokemon1.get_attack() - pokemon2.get_defense()
                slowprint(pokemon2.getname() + " attacks")
                print()
                if pokemon2.type_advantage(pokemon1) == 2:
                    slowprint("It's super effective!!")
                    print()
                elif pokemon2.type_advantage(pokemon1) == 1:
                    slowprint("Some damage was dealt")
                    print()
                else:
                    slowprint("It's not very effective...")
                    print()
                pokemon1.hp -= pokemon2.type_advantage(pokemon1) * pokemon2.get_attack() - pokemon1.get_defense()

    if pokemon1.gethp() > 0 and pokemon2.gethp() <= 0:
        slowprint(pokemon2.getname() + " fainted..")
        print()
        slowprint(pokemon1.getname() + " is the winner!!")
        print()
    else:
        slowprint(pokemon1.getname() + " fainted..")
        print()
        slowprint(pokemon2.getname() + " is the winner!!")
        print()

battle(Blastoise, Charizard)







