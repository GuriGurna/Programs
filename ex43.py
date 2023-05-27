from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("this scene is not yet configured.")
        print("subclass it and implement enter().")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene !=last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            current_scene.enter()
class Death(Scene):
    quips = [
        "you died. you kinda suck at this.",
        "your mom would be proud ... if she were smarter.",
        "such a looser.",
        "i  have a small puppy that is better at this.",
        "you are worse than your dad's jokes."
    ]            
    def enter(self):
        print(Death.quips[randint(0,len(self.quips)-1)])
        exit(1) 

class Centralcorridor(Scene):
    def enter(self):
        print(dedent(""" \t\t\t ---------------------------------------- 
        the gothons invaded your ship and you have to get bomb from weapons armory,put it in the bridge,and blow the ship after getting
        into escape pod .your are running to armory and a gothon come in your way and tries to kill you
        choices are =
        1-shoot!
        2-dodge
        3-tell a joke"""))
        action = input(">")
        if action == "shoot!":
            print(dedent("""
            you didn't aim proprely and he blast and eats you """))
            return'death'
        elif action =="dodge":
            print(dedent("""
            you dodge but unfortunately you slip and died """))
            return'death'
        elif action == "tell a joke":
            print(dedent("""
            you tell a joke and gothon statred laughinh and then you shoot him"""))
            return'laser_weapon_armory'
        else:
            print("does not compute")
            return'central_corridor'
            
class Laserweaponarmory(Scene):
    def enter(self):
        print(dedent("""\t\t\t------------------------------------------
        you did find the bomb but it is in a suitcase and you need to enter a code of 3 digits and if you put it 10 times wrongly it 
         will never open again""" ))
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        print(code)
        guess = input("[keypad]>")
        guesses= 0
        
        while guess != code and guesses <10:
            print("bzzzzeedd") 
            guesses +=1
            guess= input("[keypad]>")
        if guess == code:
            print(dedent("container opens and takes the bomb and runs towards the bridge "))
            return 'the_bridge'
        else:
            print(dedent("it did bot open and aliens destroy the ship"))
            return'death'
        
class Thebridge(Scene):
    def enter(self):
        print(dedent("""\t\t\t------------------------------------------------
                     you have the bomb and gothons see you and they dont want to set it off
                     choices are =
                     1-throw the bomb
                     2-slowly place the bomb"""))
        action = input(">")
        if action == "throw the bomb":
            print(dedent("you thow the bomb and they kill you"))
            return 'death' 
        elif action == "slowly place the bomb":
            print(dedent("you place the bomb and runs"))
            return 'escape_pod'
        else:
            print("does not compute")
            return 'the_bridge'

class Escape_pod(Scene):
    def enter(self):
        print(dedent("""\t\t\t---------------------------------------------------
                     you try to rush toward the pod and there are five pods which one would you take
                     enter pod number 
                     choices are =1,2,3,4 or 5"""))
        good_pod =randint(1,5)
        print(f"good pod no is={good_pod}")
        guess = input("[pod#]>")
        if int(guess) != good_pod:
            print(dedent("pod eject into space and exploded"))
            return 'death'
        else:
            print(dedent("you are heading towards the panet and you won "))
            return 'finished'

class Finished(Scene):
    def enter(self):
        print("you won good job")
        return 'finished'         
                               
class Map(object):
    scenes = {
        'central_corridor':Centralcorridor(),
        'laser_weapon_armory':Laserweaponarmory(),
        'the_bridge':Thebridge(),
        'escape_pod':Escape_pod(),
        'death':Death(),
        'finished':Finished(),
    }                           
    def __init__(self, start_scene):
        self.start_scene = start_scene
    def next_scene(self,scene_name):
        val = Map.scenes.get(scene_name) 
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map) 
a_game.play()
