# require './room'

inventory = []
room0_state, room1_state, room2_state, room3_state, room4_state, room5_state, room6_state, room7_state, room8_state = 1, 1, 1, 1, 1, 1, 1, 1, 1
room2_items = ['torch', 'key']
room3_switch = True
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
    print('Use the compass \'north\', \'south\', \'east\', and \'west\' to move around. You are always facing north.')
    print('Use \'look\' to get a description of your current location.')
    print('View your inventory with \'inventory\'. You can use those items with \'use <item>\'')
    print(
        'To progress through the adventure, use single words you think will interact with your current location using the location descriptions as hints')
    print('Use \'help\' to repeat these instructions')
    # print('Type one or two words at a time')


def exit_game():
    print('Are you sure you want to exit?')
    cmd = input(">>>").lower()
    if cmd in 'yes':
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
    elif room0_state == 2:
        print('You are outside the cave entrance')

    while True:

        cmd = input(">>>")

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
    global room1_state

    #print('\nCAVE ENTRANCE\n')

    if room1_state == 1:
        print('You walk into the cave. It appears no one has been here for a long time. Cobwebs line the ceiling. Random bits of bone are scattered across the floor.')
        print('There is a large lever on the floor to the right of you and a door to the north')
        room1_state = 2
    else:
        print('You are in a room with a lever and a door to the north')

    while True:

        cmd = input(">>>")

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

    global room2_state, room2_items

    if room2_state == 1:
        print('You are in a medium sized hallway going north and south. There is a lit torch hanging on the left wall lighting the hallway.')
        print('There is an open door to the south and a door to the north.')
        room2_state = 2
    else:
        print('You are in a hallway, with a door to the north and south and a torch hanging on the wall')


    while True:

        cmd = input(">>>")

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
                room2_items.pop('key')
                room2_state = 3
            elif room2_state == 3:
                print('You already took the key.')
        elif cmd in 'door' or cmd in 'open' or cmd in 'north':
            if room2_state == 2:
                print('The door opens without any effort.')
        elif cmd in 'south':
            room1()
        else:
            process_input(cmd)


start()
