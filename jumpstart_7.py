import actors
import random
import time


def main():
    print_header()
    game_loop()
    
    
def print_header():
    print("-------------------------------")
    print("        WIZARD GAME APP")
    print("-------------------------------")
    
    
def game_loop():

    creatures = [
        actors.SmallAnimal("Toad", 1),
        actors.Creature("Tiger", 12),
        actors.SmallAnimal("Bat", 3),
        actors.Dragon("Dragon", 50, 75, True),
        actors.Wizard("Evil Wizard", 1000)
    ]

    hero = actors.Wizard("Gandolf", 75)

    while True:

        active_creature = random.choice(creatures)
        print(f"A {active_creature.name} of level {active_creature.level} has appear from a dark and foggy forest...")
        cmd = input("Do you [a]ttack, [r]un away or [l]ook around? ")

        if cmd == "a":
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides taking time to recover...")
                time.sleep(5)
                print("The wizard returns revitalized!")

        elif cmd == "r":
            print("The wizard has become unsure of his powers and flees!!!")

        elif cmd == "l":
            print(f"The wizard {hero.name} takes in the surroundings and sees:")
            for c in creatures:
                print(f"* A {c.name} of level {c.level}")

        else:
            print("Goodbye!")
            break

        if not creatures:
            print("You've defeated all the creatures. Well done!")
            break

        print()


if __name__ == "__main__":
    main()