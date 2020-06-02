from sys import exit
from random import randint
from textwrap import dedent

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #printing out last scene
        current_scene.enter()

class Scene(object):

        def enter(self):
            print("aint ready yet")
            exit(1)

class Death(Scene):

    quips = [
        "You died. You kinda suck.",
        "Do you even care?",
        "Please use your useless brain",
        "You dead..."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(0)

class MainRoom(Scene):

    def enter(self):
        print(dedent("""
            Welcome to the darkness...
            Here we tell you what to do!
            if you have a problem, you have to find a way to escape
            Now get back to work.\n
            You have 3 options: work, escape, run
            """))

        action = input("> ")

        if action == 'run':
            print(dedent("""
                They killed you.
                """))
            return 'death'

        elif action == 'work':
            print(dedent("""
                You work for yor rest of your life there.
                Bye.
                """))
            return 'death'

        elif action == 'escape':
            print(dedent("""
                Okay i will help you.
                """))
            return 'laser_weapon_armory'

        else:
            print("\nNOT SUCH ACTION")
            return 'main_room'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            Good...
            I am your imaginary guide.
            I will help you to get out from here alive.
            But you have to fight!
            \n
            You found a door who lead to the exit, but its locked.
            Open it.
            (3 digits)
            """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"

        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("Nope...Try again")
            guesses += 1
            guess = input("[keypad]> ")
            print(f"The code is: {code}")

        if guess == code:
            print(dedent("""
                Good!
                You did open the door
                """))
            return 'the_bridge'
        else:
            print(dedent("""
                You failed to open the door and a hellboy found you
                """))
            return 'death'

class TheBridge(Scene):

        def enter(self):
            print(dedent("""
                Once you opened the door someone attacked you!
                But with your ninja skills,
                You grabbed his gun.
                Do something......
                """))

            action = input("> ")

            if action == "run":
                print(dedent("""
                    You tried to run,
                    Unfortunately he killed you with his knife.
                    """))
                return 'death'

            elif action == "shoot":
                    print(dedent("""
                        You killed the hellboy!
                        Good.
                        That was a close one.
                        """))
                    return 'escape_pod'
            else:
                print("Nope...Try again")
                return 'the_bridge'

class EscapePod(Scene):

    def enter(self):
            print(dedent("""
                WOW! You made it!
                You reached the parking lot.
                There are 5 spaceships.
                One of them works.
                Pick one and go!
                Before any hellboys find you!
                Be careful, ONLY ONE WORKS!
                """))

            good_pod = randint(1,5)
            guess = input("[pod #]> ")

            if int(guess) != good_pod:
                    print(dedent("""
                        You picked a bad spaceship.
                        You failed to reach back to earth.
                        """))
                    return 'death'
            else:
                    print(dedent("""
                        Great job!
                        Fortune is with you!
                        You picked the working spaceship!
                        Congratulations!
                        """))
                    return 'finished'

class Finished(Scene):

    def enter(self):
        print("You made it back alive!\n")
        return 'finished'

class Map(object):

    scenes = {
        'main_room': MainRoom(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('main_room')
a_game = Engine(a_map)
a_game.play()
