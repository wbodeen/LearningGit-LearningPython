## import some file to use in game
## use one class per room 
## the game runner needs to know the rooms. consider having each room return what room is next or setting a variable of what room is next

from textwrap import dedent
from sys import exit
from random import randint

class Room():

    def enter(self):

        print("This room is not yet described.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine():

    def __init__(self, area_map):
        
        self.area_map = area_map
        

    def play(self):

        current_room = self.area_map.opening_room()
        last_room = self.area_map.next_room('outside')

        while current_room != last_room:
            next_room_name = current_room.enter()
            current_room = self.area_map.next_room(next_room_name)

        current_room.enter()
    

class EntryGate(Room):

    def enter(self):

        print(dedent("""
        You find yourself blurry eyed and disoriented
        in the midst of several other adventurers. The
        air is filled with sand and the stench of 
        death. Near a sandstone wall lays the corpse
        of a felled adventurer, covered in slime
        and blood. From his chest an almost impossibly
        black stinger, broken from a rather large insect,
        is embedded in the adventurers chest. The corpse
        hangs suspended by this apparent warning. You
        look at the faces of disbelief staring back from
        your new found companions. Do you turn tail and run?
        Or do you try and convince the others to continue
        bravely into this strange sandy death trap?"""))
        
        response = input("run or convince? > ")

        if response == "run":

            print(dedent("""
            Given the mutilated adventurer you've seen 
            and the strange circumstance of the whole
            ordeal, you've decided to save your own skin
            and seek out riches elsewhere. As you turn,
            a mysterious portal comes into view. You walk
            towards it given the impaling alternative. Your
            eyes feel fuzzy as the view and the companions
            spin away as you are sucked into the void."""))

            return 'death'

        elif response == "convince":

            print(dedent("""
            Quickly erasing any weakness of fear from your
            expression, you laugh nervously and quip 'Looks 
            like he's sticking around!' Their faces soften
            suprisingly and you walk through the crowded 
            adventurers to the sandy space behind the group.
            Their gaze pivots, following you as you progress,
            ending their transition as you stop next to
            a battle scarred and gooey sandstone wall. 
            You place your back on the only space not marred 
            by what were seemingly fierce blows into the 
            stone surface. You feel the wall give way 
            and it topples over smashing into a decending 
            stairway wider than twenty men."""))

            return 'stairs'
        
        else:

            print("There are only two choice, genius.")
            return 'entry'
    

class GateExit(Room):
    pass

class ArchwayStairs(Room):
    def enter(self):

        print(dedent("""
        Dust, seemingly undisturbed for centuries, erupts 
        into the air, clogging the nostrals of all within the 
        vicinity. Suppressed coughs sound all around as
        everyone, including yourself, try peering through
        the dust clouds. Stumbling down the rubble laden
        staircase, your group emerges into the open air halfway
        down the staircase. Puzzled by the existance of such a
        staircase, you turn, peer up, and determine the wall
        was meant to seal an ornate archway decorated with
        the carvings of various runes and insect-like creatures.

        Feeling triumphant you exhale while speaking 'Well, that
        was quite easy, now wasn't it.' Out of breath, you
        collect yourself and surmise the skepticism of your 
        inherent abilities. Moving down the staircase, the group
        takes a haphazard formation, randomly spaced. Where do 
        you position yourself?
        """))
        
        response = input("first, middle, or last?> ")
        inputs = ['first', 'middle', 'last']
        
        if response in inputs:

            print(dedent("""
            The staircase has a checkerboard pattern slightly 
            distinguishable through the dusty layers. Taking each 
            level with careful footing, the group transitions down
            to a sand strewn rock surface at the base of the stairs.
            Taking note of the total trek, the staircase was
            six hundred and fifteen steps from top to bottom. This
            number seems oddly familiar, but you shrug it off.

            As people spread out at random, a repetitive clicking
            noise bounces off the rock surface. Everyone starts 
            looking around, puzzled by the periodic ticking."""))

            if response == 'first':

                print(dedent("""
                You proceed further at the head of the group 
                taking a step onto a primarily sandy spot. As 
                your foot applies pressure, a distinct
                thud can be heard several paces from where you
                currently stand. As everyone turns towards you,
                your leg is ripped into the earth, dragging your
                body with it. As your body snaps in half, your
                consciousness ends and it all is dark once again.
                """))

                return 'death'
            else:
                print(dedent("""
                One of the group takes a step onto a primarily sandy 
                spot and a distinct thud can be heard several paces 
                from them as his foot becomes lodged in the sand. All 
                turn towards the thud just as the man is ripped into 
                the earth. His body breaking in half as it's drug under 
                the rock surface before the air can leave his lungs 
                to produce an agonising scream.

                Realizing the indefiniteness of your approaching demise,
                you calmly walk over the rock surface hopping any 'sus'
                sandy holes along the way. Reassuring the remaining three
                adventurers they follow your enthusiasm and method. 
                """))     
                return 'temple'
        else:
            print("There are only three choice, genius.")
            return 'stairs'
        
                    
    

class TempleEnt(Room):
    pass

class BossRoom(Room):
    pass

class DreamAwake(Room):
    pass

class OutsideHouse(Room):
    pass

class Death(Room):
    endings = [
        "You chose... poorly.",
         "I see now that the circumstances of one's birth are irrelevant; it is what you do with the gift of life that determines who you are.",
         "A real loser is someone who's so afraid of not winning he doesn't even try.",
         "Carpe diem. Seize the day, boys. Make your lives extraordinary.",
         "I like the way you die, boy."
    ]

    def enter(self):
        print(Death.endings[randint(0, len(self.endings)-1)])
        exit(1)

class Map():

    areas = {
        'entry': EntryGate(),
        'early_exit': GateExit(),
        'stairs': ArchwayStairs(),
        'temple': TempleEnt(),
        'boss_fight': BossRoom(),
        'wake_up': DreamAwake(),
        'outside': OutsideHouse(),
        'death': Death()
    }

    def __init__(self, entrance):
        self.entrance = entrance
    
    def next_room(self, nextroom):
        val = Map.areas.get(nextroom)
        return val

    def opening_room(self):
        return self.next_room(self.entrance)


start = Map('entry')
a_game = Engine(start)
a_game.play()