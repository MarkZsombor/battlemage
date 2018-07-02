import random


class Creature:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level

    # __repr__ method will define what is returned when the print function is called on the class
    def __repr__(self):
        return "Creature: {} of level {}".format(
            self.name, self.level
        )

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    def attack(self, creature):
        print('The mage {} attacks {}!'.format(self.name, creature.name))

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print('You rolled {}'.format(my_roll))
        print('{} rolled {}'.format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print('The mage has defeated {}'.format(creature.name))
            return True
        else:
            print('You lost! Game over man!')
            return False


class SmallAnimal(Creature):
    # Override the first method, makes SmallAnimal weaker
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breaths_fire = breaths_fire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifer = self.scaliness / 10

        return base_roll * fire_modifier * scale_modifer
