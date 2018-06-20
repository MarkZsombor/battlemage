import random

from creatures import Wizard, Creature

def main():
    print_header()
    game_loop()


def print_header():
    print('          BATTLEMAGE')


def game_loop():

    creatures = [
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 100)
    ]

    hero = Wizard('Magic Mike', 75)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared in front of you'.format(active_creature.name, active_creature.level))

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around?')
        if cmd == 'a':
            hero.attack(active_creature)
        elif cmd == 'r':
            print('r')
        elif cmd == 'l':
            print('l')
        else:
            print('Exiting Game')
            break


if __name__ == '__main__':
    main()