from sys import exit
from random import randint
from textwrap import dedent



class Scene(object):

    def enter(self):
        print("This scene is not yet implemented.")
        print("Subclass it an implement enter().")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("finished")

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #be sure to print out the last Scene
        current_scene.enter()



class Death(Scene):

    quips = [
        "You died.",
        "Ur ded.",
        "Game error. Your fault.",
        "Don't even bother trying again.",
        "I still don't understand the logic of this program. Bye."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
        This is the start of the game.
        Choose a number: 1, 2 or 3.
        """))

        action = input("What's your number?: ")

        if action == "1":
            print(dedent("""
            This choice was unsuccessful.
            Why did you think you're #1?
            Narcissist.
            """))
            return 'death'

        elif action == "2":
            print(dedent("""
                Unfortunately, you chose wrong.
                Now you're going to suffer the consequenses.
                Inconsequential.
                """))
            return 'death'

        elif action == "3":
            print(dedent("""
                You're lucky.
                Three is a solid number.
                You may contiue.
                """))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            You now have to choose three digits.
            Choose correctly, you move on.
            Incorectly, you fail.
            You have 10 tries.
            """))

        code = f"{randint(1,9)}, {randint(1,9)}, {randint(1,9)}"
        guess = input("Choose now [keypad]: ")

        if guess == code:
            print(dedent("""
                You win!
                We move ahead.
                """))
            return 'the_bridge'

        else:
            print(dedent("""
                You fail.
                Unsurprising.
                """))
            return 'death'




class TheBridge(Scene):

    def enter(self):
        print(dedent("""Get ready. You're going to have to choose a number again.
            Choose one from 1 to 9.
            """))

        action = input("What number?: ")

        if action == "1":
            print(dedent("""
                No sorry, you're dead.
                """))

            return 'death'

        elif action == "5":
            print(dedent("""
                Lucky! You advance!
                """))

            return 'escape_pod'

        else:
            print("DOES NOT COMPUTE!")

            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
        Now you need to pick a number from 1 to 5.
        """))

        good_pod = randint(1,5)
        guess = input("Go ahead [pod #]: ")

        if int(guess) != good_pod:
            print(dedent("""
            No. That's wrong.
            """))
            return 'death'

        else:
            print("You won!")
            return 'finished'

class Finished(Scene):

    def enter(self):
        print(dedent("""
        Good job.
        """))
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
        }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val  = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')

a_game = Engine(a_map)

a_game.play()