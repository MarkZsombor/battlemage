
class Wizard:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level



class Creature:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level

    # __repr__ method will define what is returned when the print function is called on the class
    def __repr__(self):
        return "Creature: {} of level {}".format(
            self.name, self.level
        )