import random


class Wizard:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level

    def attack(self, creature):
        print('The mage {} attacks {}!'.format(self.name, creature.name))

        my_roll = random.randint(1, 12) * self.level
        creature_roll = random.randint(1, 12) * creature.level

        print('You rolled {}'.format(my_roll))
        print('{} rolled {}'.format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print('The mage has defeated {}'.format(creature.name))
            return True
        else:
            print('You lost! Game over man!')
            return False

class Creature:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level

    # __repr__ method will define what is returned when the print function is called on the class
    def __repr__(self):
        return "Creature: {} of level {}".format(
            self.name, self.level
        )