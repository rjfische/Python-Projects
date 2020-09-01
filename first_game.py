from random import randint
from random import random

def roll():
    val = randint(0,20)
    return val

class Character(object):
    def __init__(self, name, strength, armor, speed, health):
        self.name = name
        self.strength = strength
        self.armor = armor
        self.speed = speed
        self.health = health

    def attack(self):
        to_hit = self.strength + roll()
        return to_hit

    def dodge(self):
        to_dodge = random()
        dodge_chance = 1 - self.speed
        if to_dodge  >= dodge_chance:
            return True
        else:
            return False

orc = Character("orc",2, 14, 0, 20)
spider = Character("spider", 0, 13, 0.3, 10)
golem = Character("golem", 6, 12, 0, 40)

fighter = Character("fighter", 4, 16, 0, 35)
ranger = Character("ranger", 2, 14, .4, 25)

enemies = [orc, spider, golem]
jobs = [fighter, ranger]
champions = [orc, spider, golem, fighter, ranger]

def fight(c1, c2):
    f1 = c1.name
    f2 = c2.name
    c1_health = c1.health
    c2_health = c2.health
    print(f"A {f1} and a {f2} square off!")
    print(f"The {f1} attacks first!")

    round = 0
    victor = None

    while c1_health > 0 and c2_health > 0:

        strike_result = c1.attack() - c2.armor
        strike_result_2 = c2.attack() - c1.armor
        dodge_result_1 = c1.dodge()
        dodge_result_2 = c2.dodge()

        if round % 2 == 0:
            if dodge_result_2 == True:
                print(f"The {f1} swings but the {f2} dodges the attack!")
            elif strike_result >= 0 and dodge_result_2 == False:
                c2_health -= strike_result
                print(f"The {f1} hits for {strike_result} damage! ({f2}: {c2_health}/{c2.health})")
                round += 1
                if c2_health <= 0:
                    victor = f1
            else:
                print(f"The {f1} misses!")
                round += 1

        else:
            if dodge_result_1 == True:
                print(f"The {f2} swings but the {f1} dodges the attack!")
            elif strike_result_2 >= 0 and dodge_result_1 == False:
                c1_health -= strike_result_2
                print(f"The {f2} hits for {strike_result_2} damage! ({f1}: {c1_health}/{c1.health})")
                round += 1
                if c1_health <= 0:
                    victor = f2
            else:
                print(f"The {f2} misses!")
                round += 1

    if victor == f1:
        print(f"The {f2} loses the fight. The {f1} is victorious!")
    else:
        print(f"The {f1} loses the fight. The {f2} is victorious!")

def startgame():
    print("""
          Welcome to the arena!
          Here you can square off against any number of opponents.
          But first, pick your champion:
          - fighter
          - ranger
          - orc
          - spider
          - golem
          """)

    choice = input("> ")
    champion = next((x for x in champions if x.name == choice))
    print(f"You chose the {choice}.")

    fight(champion, enemies[randint(0,2)])

    print("Would you like to fight in the arena again?")
    replay = input("> ")

    if replay == "yes":
        startgame()
    else:
        print("Bye... for now.")

startgame()
