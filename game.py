# require './room'

inventory = []
room0_state, room1_state, room2_state, room3_state, room4_state, room5_state, room6_state, room7_state, room8_state = 1, 1, 1, 1, 1, 1, 1, 1, 1
room2_items = ['torch', 'key']
room3_switch = 0
room4_items = ['pickaxe']


#####################
# PRIMARY FUNCTIONS #
#####################
def process_input(cmd):
    if cmd in 'inventory' or cmd in 'items':
        get_inventory()
    elif cmd in 'use':
        # use_item
        print("nothing to use")
    elif cmd in 'help' or cmd in 'instructions' or cmd in 'guide':
        instructions()
    elif cmd in 'exit':
        exit_game()
    elif cmd in 'reset':
        start()
    else:
        invalid_action()


def instructions():
    print('Use the compass directions \'north\', \'south\', \'east\', and \'west\' to move around. You are always facing north.')
    print('Use \'look\' to get a description of your current location.')
    print('View your inventory with \'inventory\'. You can use those items with \'use <item>\'')
    print(
        'To progress through the adventure, use single words you think will interact with your current location using the location descriptions as hints')
    print('Use \'help\' to repeat these instructions')
    # print('Type one or two words at a time')


def exit_game():
    #print('Are you sure you want to exit?')
    #cmd = input(">>>").lower()
    #if cmd in 'yes':
    exit()


def die():
    print('You died.')
    print('Would you like to start again?')
    cmd = input(">>>").lower()
    if cmd in 'yes':
        start()
    else:
        exit_game()


def invalid_action():
    print('You can\'t do that')


def get_inventory():
    global inventory
    if inventory:
        for item in inventory:
            print(item)
    else:
        print('You don\'t have any items')


##########
# start  #
##########
def start():
    print('*********************************')
    print('* Eddie\'s Awesome Adventure game *')
    print('*********************************')
    print('')

    #reinitialize rooms
    global room1_state, room2_state, room3_state, room4_state, room5_state, room6_state, room7_state, room8_state
    room1_state, room2_state, room3_state, room4_state, room5_state, room6_state, room7_state, room8_state = 1, 1, 1, 1, 1, 1, 1, 1
    entrance()


############
# ENTRANCE #
############
def entrance():
    # print('\nEXTERIOR\n')
    # state 1 = new
    # state 2 = visited

    # No puzzles here. Player can read the sign or continue north.
    global room0_state

    if room0_state == 1:
        print('You are an adventurer. You have traveled far and wide seeking riches and fame.')
        print('You just emerged from the woods into a small clearing. You are facing a cliff wall stretching to the east')
        print('and west as far as you could see. Directly in front of you to the north is a cave entrance.')
        print('You believe this to be the lair of the infamous dragon that has ravaged many towns and slain many people.')
        print('Legends say that it also guards a vast treasure; he who claims it will amass a fortune worth many lifetimes')
        print('and he who slays the dragon will become hero of the land.')
        print('There is a wooden sign just next to the cave entrance.')
        room0_state = 2
    else:
        print('You are outside the cave entrance')

    while True:

        cmd = input(">>>").lower()

        if cmd in 'look':
            print('There is a cliff wall to the north, with the cave entrance in front of you and a sign next to it.')
        elif cmd in 'read' or cmd in 'sign':
            print('You walk up to the sign. It seems hastily put together, being held up with simple string. It reads:\n')
            print('Here\'s some useful information that will help you in your adventure:\n')
            instructions()
        elif cmd in 'north' or cmd in 'cave' or cmd in 'enter' or cmd in 'entrance':
            room1()
        elif cmd in 'south' or cmd in 'east' or cmd in 'west':
            print('You can\'t go that way. There is a mysterious force pulling you north towards the cave.')
        else:
            process_input(cmd)


##########
# ROOM 1 #
##########
def room1():
    # state 1 = new
    # state 2 = visited, door locked and lever in locked position
    # state 3 = door unlocked, lever in unlocked position
    # state 4 = lever in unlocked position, door unlocked

    # Player is expected to pull the lever before proceeding north.

    global room1_state

    #print('\nCAVE ENTRANCE\n')

    if room1_state == 1:
        print('You walk into the cave. It appears no one has been here for a long time. Cobwebs line the ceiling. Random bits of bone are scattered across the floor.')
        print('There is a large lever on the floor to the right of you and a door to the north')
        room1_state = 2
    else:
        print('You are in a room with a lever and a door to the north')

    while True:

        cmd = input(">>>").lower()

        if cmd in 'look':
            if room1_state == 2:
                print('There is a lever on the right side of the room and a door on the north wall.')
            elif room1_state == 3:
                print('You see a lever that has been pulled, and a closed door to the north.')
            elif room1_state == 4:
                print('You see a lever that has been pulled, and a door to the north.')
        elif cmd in 'door' or cmd in 'open' or cmd in "north":
            if room1_state == 2:
                print('There is a closed door blocking the way. You try to open it but it doesn\'t budge.')
            elif room1_state == 3:
                print('You make your way to the door and give it a push. It slowly swings open with a loud creek that reverberates throughout the cave.')
                room1_state = 4
                room2()
            elif room1_state == 4:
                room2()
        elif cmd in 'south':
            entrance()
        elif cmd in 'east' or cmd in 'west':
            print('There is a wall there.')
        elif cmd in 'lever':
            if room1_state == 2:
                print('You pull on the lever. It is a bit difficult to move with the rust of years of unuse damaging its gears, but it finally gives in.')
                print('You hear a hollow clank come from the door to the north, the sound of a deadbolt being released.')
                room1_state = 3
            elif room1_state == 3 or room1_state == 4:
                print('You try and move the lever, but it appears to have jammed in place.')
        elif cmd in 'bone':
            print('You take some of the bones scattered about thinking it might be useful')
            inventory.append('bone')
        else:
            process_input(cmd)


##########
# ROOM 2 #
##########
#HALLWAY

def room2():
    #state 1 = new
    #state 2 = door closed, key on ground
    #state 3 = door closed, no key
    #state 4 = door open, no key

    # Player can take the torch and proceed north freely.

    global room2_state, room2_items

    if room2_state == 1:
        print('You are in a medium sized hallway going north and south. There is a lit torch hanging on the left wall lighting the hallway.')
        print('There is an open door to the south and a door to the north.')
        room2_state = 2
    else:
        print('You are in a hallway, with a door to the north and south and a torch hanging on the wall')

    while True:

        cmd = input(">>>").lower()

        if cmd in 'look':
            if room2_state == 2:
                print('You are in a hallway with a door to the north and south, and torches hanging from the wall.')
                print('Upon closer inspection, you notice a small key on the floor.')
            else:
                print('You are in a hallway with a door to the north and south, and torches hanging from the wall.')
        elif cmd in 'key':
            if room2_state == 2:
                print('You take the key.')
                inventory.append('key')
                room2_items.remove('key')
                room2_state = 3
            elif room2_state == 3:
                print('You already took the key.')
        elif cmd in 'door' or cmd in 'open' or cmd in 'north':
            if room2_state == 2 or room2_state == 3:
                print('The door opens without any effort. You walk through.')
                room3()
            elif room2_state == 4:
                room3()
        elif cmd in 'south':
            room1()
        else:
            process_input(cmd)


##########
# ROOM 3 #
##########
#CIRCULAR ROOM WITH PEDESTAL

def room3():
    #state 1 = new
    #state 2 = door closed, wall up
    #state 3 = door closed, wall down
    #state 4 = door open, wall up
    #state 5 = door open, wall down

    #Player must inspect the pedestal and press the switch to open the north door. The wall to the east can only be broken
    #down by using the pickaxe, which is acquired in the room to the west.

    global room3_state, room3_switch

    if room3_state == 1:
        print('You appear in a rather large cavern. Water is slowly dripping above you. When you follow it up, you see the')
        print('entire ceiling covered in stalagtites. You faintly hear running water in the distance')
        print('There is a door to the north, an open passageway to the west and the door you just come through from the south')
        print('There is a pedestal near the center of the room, though you can\'t tell what is on it.')
        room3_state = 2
    else:
        print('You are in a rather large cavern. There is a door to the north and an open passageway to the west and a pedestal in the center.')

    while True:

        cmd = input(">>>").lower()

        if cmd in 'look':
            print('You are in a large room with a pedestal in the center, a door to the north and an opening to the west.')
            if room3_state == 2 or room3_state == 4:
                print('You also notice a faint light coming from the wall on the east, as if the wall was full of cracks allowing light to seep through.')
            elif room3_state == 3 or room3_state == 5:
                print('The wall to the right has been destroyed, revealing a small room to the east.')
        elif cmd in 'pedestal':
            print('You walk up to the pedestal. It is made of stone, too perfectly circular to be a natural formation.')
            print('You inspect it and see what appears to be a switch at the top of it.')
        elif cmd in 'switch' or cmd in 'flip' or cmd in 'press':
            print('You press the switch. You hear a clank come from the north')
            if room3_switch == 0:
                room3_switch = 1
            elif room3_switch == 1:
                room3_switch = 0
        elif cmd in 'use':
            if cmd in 'pickaxe':
                if 'pickaxe' in inventory and (room3_state == 2 or room3_state == 4):
                    print('You swing the pickaxe at the wall to the east. Chunks slowly start to chip away from it.')
                    print('You give it one final strike, and the entire wall comes crumbling down, revealing a passageway to the east.')
                    print('The axe, being worn and rusty, falls apart. Pickaxe is removed from your inventory.')
                    inventory.remove('pickaxe')
                    room3_state = room2_state + 1
                else:
                    print('You don\'t have that.')
            else:
                print('You can\'t use that here.')

        elif cmd in 'door' or cmd in 'north':
            if room3_switch == 0:
                if room3_state == 2 or room3_state == 3:
                    print('There is a door to the north. You push the door, but it doesn\'t budge.')
            elif room3_switch == 1:
                if room3_state == 2 or room3_state == 3:
                    print('You push the north door open and walk through.')
                    #room6()
                    print("go to room 6")
                elif room3_state == 2 or room3_state == 3:
                    # room6()
                    print("go to room 6")
        elif cmd in 'west':
            room4()
            print('go to room 4')
        elif cmd in 'south':
            room2()
        elif cmd in 'wall' or cmd in 'light':
            if cmd in 'punch' or cmd in 'hit' or cmd in 'strike' or cmd in 'kick' or cmd in 'break' or cmd in 'destroy':
                print('You try to destroy the wall. Some rocks crumble away, but the wall remains standing.')
            else:
                print('You walk up to the wall to the east and notice it looks very fragile. Rocks have chipped away from it,')
                print('allowing a faint light to seep through it from the other side')
        elif cmd in 'rock':
            print('You try to use the rocks to break the wall, but they are too small.')
        elif cmd in 'east':
            if room3 == 2 or room3 == 4:
                print('There is a wall to the east, but it looks like it can be broken down')
            else:
                #room5()
                print('go to room 5')
        else:
            process_input(cmd)


##########
# ROOM 4 #
##########
#ROOM WITH AXE
def room4():
    #state 1 = new
    #state 2 = axe not taken
    #state 3 = axe taken

    #Player acquires the pickaxe, which is used to tear down the wall in the room to the east.

    global room4_state

    if room4_state == 1:
        print('You are in a small round room, with lots of rock and debris. There is an open doorway to the east')
        room4_state = 2
    else:
        print('You are in a small round room, with lots of rock and debris. There is an open doorway to the east')

    while True:

        cmd = input(">>>")

        if cmd in 'look':
            print('You are in a small circular room full of dirt and debris. There is a passageway to the east.')
            if 'pickaxe' in room4_items:
                print('You see something shiny among the debris.')
        elif cmd in 'rock' or cmd in 'debris' or cmd in 'shiny':
            if 'pickaxe' in room4_items:
                print('You kick the debris around with your feet and reveal a pickaxe on the ground.')
            else:
                print('You kick around the debris but can\'t find anything else.')
        #elsif cmd.include? 'use'
        #print('You can\'t use that here.'
        elif cmd in 'pickaxe':
            if 'pickaxe' in room4_items:
                print('You take the pickaxe')
                inventory.append('pickaxe')
                room4_items.remove('pickaxe')
                room4_state = 3
            else:
                print('You already took the pickaxe')
        elif cmd in 'east':
            room3()
        else:
            process_input(cmd)


start()
