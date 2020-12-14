import random


class Creature:

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level

    def __repr__(self):
        return f"Creature: {self.name} of level {self.level}"


class Wizard(Creature):

    def attack(self, creature):
        print(f"A wizard {self.name} attacks {creature.name}!")
        my_roll = random.randint(1, 12) * self.level
        creature_roll = creature.get_defensive_roll()
        print(f"You roll {my_roll}...")
        print(f"{creature.name} roll {creature_roll}...")
        if my_roll >= creature_roll:
            print(f"The wizard has handily triumphed over {creature.name}.")
            return True
        else:
            print("The wizard has been DEFEATED!!!")
            return False


class SmallAnimal(Creature):

    def get_defensive_roll(self):
       base_roll = super().get_defensive_roll()
       return base_roll / 2


class Dragon(Creature):
    
    def __init__(self, name, level, scaliness, fire_breath):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.fire_breath = fire_breath

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.fire_breath else 1
        scale_modifier = self.scaliness / 10
        return base_roll * fire_modifier * scale_modifier