import random
import time

from creatures import Wizard, Creature, SmallAnimal, Dragon

def main():
    print_header()
    game_loop()


def print_header():
    print('          BATTLEMAGE')


def game_loop():

    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 20, True),
        Wizard('Evil Wizard', 100)
    ]

    hero = Wizard('Magic Mike', 75)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared in front of you'.format(active_creature.name, active_creature.level))

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around?')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('You run away to recuperate')
                time.sleep(5)
                print('You are now ready to go forth again')
        elif cmd == 'r':
            print('You flee in terror, screaming like a frightened child.')
        elif cmd == 'l':
            print('You look around and see:')
            for c in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        else:
            print('Exiting Game')
            break

        if not creatures:
            print("You've done it! All your enemies have been vanquished!")
            break

        print()


if __name__ == '__main__':
    main()