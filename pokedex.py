#Here will be different functions for the bot to use when it's asked to give a dex entry for Pokémon.
import random

def bulbasaur():
    print("Bulbasaur, the Grass/Poison type pokémon.")
    print("Pokédex entry NO.001")
    num = random.randint(1,3)

    if num == 1:
        print("The bulb on its back acts as a built-in energy source, allowing it to go long periods without food!")

    if num == 2:
        print("The bulb on its back is known to have been there since birth, growing alongside it!")

    if num == 3:
        print("To keep its bulb full of energy, bulbasaur tend to sleep in sunny spaces!")

def ivysaur():
    print("Ivysaur, the Grass/Poison type Pokémon.")
    print("Pokédex entry NO.002")
    num = random.randint(1,3)

    if num == 1:
        print("The weight of an Ivysaur's bulb prevents it from running fast or standing on its hind legs,")
        print("forcing its legs to grow sturdy.")

    if num == 2:
        print("Ivysaur tend to spend more time in sunlight, preparing for their upcoming evolution!")

    if num == 3:
        print("When an Ivysaur's flower is ready to bloom, it will give off a sweet-smelling scent and will start to swell.")

def venusaur():
    print("Venusaur, the Grass/Poison type pokémon.")
    print("Pokédex entry NO.003")
    num = random.randint(1,3)

    if num == 1:
        print("The scent that emanates from a Venusaur's bulb can attract pokémon and calm emotions!")
        print("This scent becomes stronger after a rainy day!")

    if num == 2:
        print("Venusaur tend be stronger during the summertime, as there is more sunlight for them to absorb during that time.")

    if num == 3:
        print("Venusaur can shoot out huge amounts of pollen from their bulbs.")
        print("Breathing in too much can cause you to faint, so be careful!")

def charmander():
    print("Charmander, the Fire type pokémon.")
    print("Pokédex entry NO.004")
    num = random.randint(1,3)

    if num == 1:
        print("Charmander and the flame on their tail are interconnected,")
        print("reflecting its life force to how bright the flame burns!")

    if num == 2:
        print("As they sleep, Charmander supposedly draw heat from their tails for warmth!")

    if num == 3:
        print("Charmander like to behave in packs, finding food and making sure each other's tails stay lit!")

def charmeleon():
    print("Charmeleon, the Fire type Pokémon!")
    print("Pokédex entry NO.005")
    num = random.randint(1,3)

    if num == 1:
        print("Charmeleon are hotheaded by nature, constantly looking for opponents to fight.")
        print("Exceptionally strong pokemon excites them, even causing them to spout bluish-white flames!")

    if num == 2:
        print("Although they are known to be aggressive, they tend to relax after they win a battle.")

    if num == 3:
        print("A Charmeleon will use the fire on its tail to raise the temperature around it, tormenting the opponent with a hot atmosphere!.")

def charizard():
    print("Charizard, the Fire type pokémon.")
    print("Pokédex entry NO.006")
    num = random.randint(1,3)

    if num == 1:
        print("Charizard tend to live in mountains, and even inhabit volcanoes with others of its species!")

    if num == 2:
        print("Charizard fly around in search of strong opponents, with its fire on its tail burning brighter with gained experience!")
        print("They will never fight anything weaker than itself.")

    if num == 3:
        print("A Charizard's fiery breath can melt boulders and huge glaciers.")
        print("It's also been known to accidentally start forrest fires!")

pokelist = [bulbasaur, ivysaur, venusaur, charmander, charmeleon, charizard, squirtle, wartortle, blastoise, pikachu]


'''
Pokédex function format:

    print("NAME, the TYING type Pokémon.")
    print("Pokédex entry NO###.")

    num = random.randint(1,3)

    if num == 1:
        print()

    if num == 2:
        print()

    if num == 3:
        print()
'''











