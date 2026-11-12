import random

# Startvärdena väljer du själv.
own_hp = 750
corvette_hp = 200
patrol_hp = 2
battleship_hp = 3500
lightCruiser_hp = 250
HeavyCruiser_hp = 750
L3_hp = 9000000

patrol_armour = 2.1
corvette_armour = 1.5
lightCruiser_armour = 1
heavycruiser_armour = 0.5
battelship_armour = 0.2
Own_armour = 0.5


Patrol_APdmg = random.randint(1,3)
Corvette_HEdmg = random.randint(3,7)
Corvette_APdmg = random.randint(10,20)
LightCruiser_HEdmg = random.randint(40,60)
LightCruiser_APdmg = random.randint(50,75)
HeavyCruiser_HEdmg = random.randint(50, 100)
HeavyCruiser_APdmg = random.randint(75,150)
battleship_HEdmg = random.randint(300,500)
battleship_APdmg = random.randint(250,400)
own_HEdmg = random.randint(100, 200)
own_APdmg = random.randint(75, 150)


print("Welcome to BoatBatlr")

while True:
    game_ready = input("Play Y/N ")
    if game_ready.lower() == "yes" or game_ready.lower() == "y":
        print("Starting level 1")
        break
    elif game_ready.lower() == "no" or game_ready.lower() == "n":
        print("You have no free will")
        break
    else:
        print("try again")

print("a patrol boat approaches")

while True:
    ammo_choise = input("Load HE or AP ")
    if ammo_choise.lower() == ("he") or ammo_choise.lower() == ("high explosive"):
        print("You load HE")
        break
    elif ammo_choise.lower == ("ap") or ammo_choise.lower() == ("armour piercing"):
        print("You load AP rounds")
        break
    else:
        print("pick an ammo type")

while True:
    aiming = input("aim front or backside of patrol boat ")
    if aiming.lower() == ("back") or aiming.lower() == ("backside"):
        print()