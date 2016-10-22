#require './room'

@inventory = Array.new
@room1, @room2, @room3, @room4, @room5, @room6, @room7, @room8 = 1, 1, 1, 1, 1, 1, 1, 1
@room2_items = ['torch', 'key']
@room3_switch = true
@room4_items = ['pickaxe']
#@room1, @room2, @room3 = Room.new, Room.new, Room.new

def start
  puts '*********************************'
  puts '* Eddies Awesome Adventure game *'
  puts '*********************************'
  puts ''
  entrance
end

############
# ENTRANCE #
############

def entrance
  puts 'You are an adventurer. You have traveled far and wide seeking riches and fame.'
  puts 'You just emerged from the woods into a small clearing. You are facing a cliff wall stretching to the east'
  puts 'and west as far as you could see. Directly in front of you to the north is a cave entrance.'
  puts 'You believe this to be the lair of the infamous dragon that has ravaged many towns and slain many people.'
  puts 'Legends say that it also guards a vast treasure; he who claims it will amass a fortune worth many lifetimes'
  puts 'and he who slays the dragon will become hero of the land.'
  puts 'There is a wooden sign just next to the cave entrance.'

  while true
    cmd = take_input

    if cmd.include? 'inventory'
      list_inventory
    elsif cmd.include? 'use'
      use_string = cmd.split(' ')
      use_item use_string[1]
    elsif cmd.include? 'help'
      help
    elsif cmd.include? 'exit'
      exit_game
    elsif cmd.include? 'look'
      puts 'There is a cliff wall to the north, with the cave entrance in front of you and a sign next to it.'
    elsif cmd.include? 'read' or cmd.include? 'sign'
      puts 'You walk up to the sign. It seems hastily put together, being help up with simple string. It reads:'
      puts 'Here\'s some useful information that will help you out in the cave.'
      help
    elsif cmd.include? 'north' or cmd.include? 'cave' or cmd.include? 'enter' or cmd.include? 'entrance'
      room1
    elsif cmd.include? 'south' or cmd.include? 'east' or cmd.include? 'west'
      puts 'You can\'t go that way. There is a mysterious force pulling you north towards the cave.'
    else
      invalid_action
    end
  end
end

##########
# ROOM 1 #
##########

def room1
  #state 1 = new
  #state 2 = visited, door locked and lever in locked position
  #state 3 = door unlocked, lever in unlocked position
  #state 4 = lever in unlocked position, door unlocked

  if @room1 == 1
    puts 'You walk into the cave. It appears no one has been here for a long time. Cobwebs line the ceiling. Random bits of bone are scattered across the floor.'
    puts 'There is a large lever on the floor to the right of you and a door to the north'
    @room1 = 2
  else
    puts 'You are in a room with a lever and a door to the north'
  end


  while true

    cmd = take_input

    if cmd.include? 'inventory'
      list_inventory
    elsif cmd.include? 'help'
      help
    elsif cmd.include? 'exit'
      exit_game
    elsif cmd.include? 'look'
      if @room1 == 2
        puts 'There is a lever to the right, and a door to the north'
      elsif @room1 == 3
        puts 'You see a lever that has been pulled, and a closed door to the north.'
      elsif @room1 == 4
        puts 'You see a lever that has been pulled, and a door to the north.'
      end
    else
      if cmd.include? 'lever'
        if @room1 == 2
          puts 'You pull on the lever. It is a bit difficult to move with the rust of years of unuse damaging its gears, but it finally gives in.'
          puts 'You hear a hollow clank come from the door to the north.'
          @room1 = 3
        else
          puts 'You try and move the lever, but it appears to have jammed.'
        end
      elsif cmd.include? 'door' or cmd.include? 'open'
        if @room1 == 3
          puts 'You make your way to the door and give it a push. It slowly swings open with a loud creek that reverberates throughout the cave.'
          @room1 = 4
        elsif @room1 == 4
          puts 'The door is already open'
        else
          puts 'You try to open the door but it is locked.'
        end
      elsif cmd.include? 'north'
        if @room1 == 4
          room2
        else
          puts 'There is a closed door blocking the way'
        end
      else
        invalid_action
      end
    end
  end
end


##########
# ROOM 2 #
##########
#HALLWAY

def room2
  #state 1 = new
  #state 2 = door closed
  #state 3 = door open

  if @room2 == 1
    puts 'You are in a medium sized hallway going north and south. There is a lit torch hanging on the left wall lighting the hallway.'
    puts 'There is an open door to the south and an open doorway to the north.'
    @room2 = 2
  else
    puts 'You are in a hallway, with a door to the north and south and a torch hanging on the wall'
  end


  while true

    cmd = take_input

    if cmd.include? 'help'
      help
    elsif cmd.include? 'exit'
      exit_game
    elsif cmd.include? 'inventory'
      list_inventory
    elsif cmd.include? 'look'
      if @room2_items.include?('key')
        puts 'You are in a hallway with a door to the north and south, and torches hanging from the wall.'
        puts 'Upon closer inspection, you notice a small key on the floor.'
      else
        puts 'You are in a hallway with a door to the north and south, and torches hanging from the wall.'
      end
    elsif cmd.include? 'use'
      use_item_cmd = cmd.split(' ')
      has_item, item = use_item use_item_cmd[1]
      if has_item
        if item.eql? 'key'
         if @room2 == 3
          puts 'There is nothing to use the key with.'
         else
          puts 'You try to use the key to unlock the door, but it doesn\'t appear to have any keyholes'
         end
        end
      end
    elsif (cmd.strip!).include? 'key'
      if @room2_items.include? 'key'
        puts 'You take the key.'
        @inventory.push('key')
        @room2_items.delete('key')
      else
        puts 'You already took the key'
      end
    elsif cmd.include? 'door' or cmd.include? 'open'
      puts 'The door opens without any effort.'
      @room2 = 3
    elsif cmd.include? 'north'
      if @room2 == 3
        room3
      else
        puts 'The door to the north is closed.'
      end
    elsif cmd.include? 'south'
      room1
    else
      invalid_action
    end
  end
end

##########
# ROOM 3 #
##########
#CIRCULAR ROOM WITH PEDESTAL

def room3
  #state 1 = new
  #state 2 = door closed, wall up
  #state 3 = door closed, wall down
  #state 4 = door open, wall up
  #state 5 = door open, wall down

  if @room3 == 1
    puts 'You appear in a rather large room. You follow the dripping water up to see stalagtites. You faintly hear running water.'
    puts 'There is a door to the north and an open passageway to the west.'
    puts 'There is a pedestal near the center of the room, though you can\'t tell what is on it.'
    @room3 = 2
  else
    puts 'You are in a rather large room. There is a door to the north and an open passageway to the west and a pedestal in the center.'
  end

  while true

    cmd = take_input

    if cmd.include? 'help'
      help
    elsif cmd.include? 'exit'
      exit_game
    elsif cmd.include? 'inventory'
      list_inventory
    elsif cmd.include? 'look'
      puts 'You are in a large room with a pedestal in the center, a door to the north and an opening to the east.'
      if @room3 == 2
        #puts 'You take a closer look at the pedestal and notice what seems like a switch.'
        puts 'You also notice a faint light coming from the wall on the east, as if the wall was full of cracks allowing light to seep through.'
      elsif @room3 == 3
        #puts 'You notice a switch on the pedestal at the center of the room.'
        puts 'The wall to the right has been destroyed, revealing a small room to the west'
      elsif @room3 == 4
        #puts 'You notice a switch on the pedestal at the center of the room.'
        puts 'You also notice a faint light coming from the wall on the east, as if the wall was full of cracks allowing light to seep through.'
      elsif @room3 == 5
        #puts 'You notice a switch on the pedestal at the center of the room.'
        puts 'The wall to the right has been destroyed, revealing a small room to the east'
      end
    elsif cmd.include? 'pedestal'
      puts 'The pedestal is made of stone, too perfectly circular to be a natural formation.'
      puts 'You inspect it and see what appears to be a switch at the top of it.'
    elsif cmd.include? 'switch' or cmd.include? 'flip' or cmd.include? 'press'
      puts 'You press the switch. You hear a clank come from the north'
      @room3_switch = !@room3_switch
    elsif cmd.include? 'use'
      use_item_cmd = cmd.split(' ')
      has_item, item = use_item use_item_cmd[1]
      if has_item
        if item.include? 'axe'
          if @room3 == 2 or @room3 == 4
            puts 'You swing the pickaxe at the wall to the east. Chunks slowly start to chip away from it.'
            puts 'You give it one final strike, and the entire wall comes crumbling down, revealing a passageway to the east.'
            puts 'The axe, being worn and rusty, falls apart. Pickaxe is removed from your inventory.'
            @inventory.delete('pickaxe')
            @room3 += 1
          end
        end
      end
    elsif cmd.include? 'door'
      if @room3_switch
        if @room3 == 2 or @room3 == 3
          puts 'You push the north door open.'
          @room += 2
        else
          puts 'The door is already open'
        end
      else
        puts 'You push the door, but it doesn\'t budge.'
      end
    elsif cmd.include? 'west'
      room4
    elsif cmd.include? 'south'
      room2
    elsif cmd.include? 'wall' or cmd.include? 'light'
      puts 'You walk up to the wall to the east and notice it looks very fragile. Rocks have chipped away from it,'
      puts 'allowing a faint light to seep through it from the other side'
    elsif cmd.include? 'east'
      if @room3 == 2 or @room3 == 4
        puts 'There is a wall to the east, but it looks like it can be broken down'
      else
        room5
      end
    elsif cmd.include? 'north'
      if @room3 == 2 or @room3 == 3
        puts 'There is a door blocking the way to the north'
      else
        puts 'go to room 6'
      end
    else
      invalid_action
    end
  end
end

##########
# ROOM 4 #
##########
#ROOM WITH AXE
def room4
  #state 1 = new
  #state 2 = axe not taken
  #state 3 = axe taken
  if @room4 == 1
    puts 'You are in a small round room, with lots of rock and debris. There is an open doorway to the east'
    @room4 = 2
  end

  while true

    cmd = take_input

    if cmd.include? 'help'
      help
    elsif cmd.include? 'exit'
      exit_game
    elsif cmd.include? 'inventory'
      list_inventory
    elsif cmd.include? 'look'
      if @room4 == 2
        puts 'You kick the debris around with your feet and reveal a pickaxe on the ground'
      else
        puts 'You are in a small circular room full of dirt and debris. There is a passageway to the east.'
      end
    elsif cmd.include? 'use'
      puts 'You can\'t use that here'
    elsif cmd.include? 'axe'
      if @room4_items.include? 'pickaxe'
        puts 'You take the pickaxe'
        @inventory.push('pickaxe')
        @room4_items.delete('pickaxe')
        @room4 = 3
      else
        puts 'You already took the pickaxe'
      end
    elsif cmd.include? 'east'
      room3
    else
      invalid_action
    end
  end
end

##########
# ROOM 5 #
##########
#ROOM WITH CHEST WITH SWORD
def room5
  #state 1 = new
  #state 2 = chest closed
  #state 3 = chest opened
  #state 4 = sword taken

  if @room3 == 1
    puts 'You walk down the narrow passageway into a small alcove. The room is barely big enough for you to stand in.'
    puts 'There is a treasure chest, simply decorated and made of wood.'
    @room3 = 2
  else
    puts 'You are in the small room with a treasure chest'
  end

  while true

    cmd = take_input

    if cmd.include? 'help'
      help
    elsif cmd.include? 'exit'
      exit_game
    elsif cmd.include? 'inventory'
      list_inventory
    elsif cmd.include? 'look'
      if @room5 == 2
        puts 'You are in a very small room, with a treasure chest.'
      else
        puts 'You are in a small room, the treasure chest has been opened'
      end
    elsif cmd.include? 'use'
      puts 'You can\'t use that here'
    elsif cmd.include? 'west'
      room3
    else
      invalid_action
    end
  end
end


##########
# ROOM 6 #
##########
#ROOM leading to boulder and ladder
def room6
  #state 1 = new
  #state 2 = axe not taken
  #state 3 = axe taken

  if @room6 == 1
    puts 'You are in a small round room with a passageways heading east and west.'
    @room6 = 2
  end

  while true

    cmd = take_input

    if cmd.include? 'help'
      help
    elsif cmd.include? 'exit'
      exit_game
    elsif cmd.include? 'inventory'
      list_inventory
    elsif cmd.include? 'look'
      puts 'You are in a small round room with a passageways heading east and west.'
    elsif cmd.include? 'use'
      puts 'You can\'t use that here'
    elsif cmd.include? 'west'
      room7
    elsif cmd.include? 'east'
      room8
    else
      invalid_action
    end
  end
end

##########
# ROOM 7 #
##########
#room with ladder
def room7
  #state 1 = new
  #state 2 = axe not taken
  #state 3 = axe taken

  if @room7 == 1
    puts 'you are in room7'
    @room7 = 2
  end

  while true

    cmd = take_input

    if cmd.include? 'help'
      help
    elsif cmd.include? 'exit'
      exit_game
    elsif cmd.include? 'inventory'
      list_inventory
    elsif cmd.include? 'look'
      puts 'You are in a small round room with a passageways heading east and west.'
    elsif cmd.include? 'use'
      puts 'You can\'t use that here'
    elsif cmd.include? 'west'
      room7
    elsif cmd.include? 'east'
      room8
    else
      invalid_action
    end
  end
end

##########
# ROOM 8 #
##########
#room with boulder
def room8
  #state 1 = new
  #state 2 = axe not taken
  #state 3 = axe taken
  if @room6 == 1
    puts 'you are in room 8'
    @room6 = 2
  end

  while true

    cmd = take_input

    if cmd.include? 'help'
      help
    elsif cmd.include? 'exit'
      exit_game
    elsif cmd.include? 'inventory'
      list_inventory
    elsif cmd.include? 'look'
      puts 'You are in a small round room with a passageways heading east and west.'
    elsif cmd.include? 'use'
      puts 'You can\'t use that here'
    elsif cmd.include? 'west'
      room7
    elsif cmd.include? 'east'
      room8
    else
      invalid_action
    end
  end
end

#####################
# PRIMARY FUNCTIONS #
#####################

def exit_game
  puts 'Are you sure you want to exit?'
  cmd = take_input
  if cmd == 'yes'
    Process.exit
  else
    false
  end
end

def invalid_action
  puts 'You can\'t do that here'
end

def list_inventory
  if !@inventory.empty?
    @inventory.each { |item| puts item}
  else
    puts 'You dont have any items'
  end
end

def use_item(requested_item)
  has_item = false
  if requested_item.nil? or requested_item.empty?
    requested_item = String.new
    while requested_item.nil? or requested_item.empty?
      puts 'Which item do you want to use?'
      requested_item = take_input.strip!
    end
  end
  if @inventory.include? requested_item
    has_item = true
  end
  if !has_item
    puts 'You dont have ' + requested_item
  end
  return has_item, requested_item
end

def take_input
  print '> '
  cmd = gets
  cmd.downcase
end

def help
  puts 'You can use any compass directions to move around (ex. north, southeast).'
  puts 'You can view your inventory with \'inventory\'. You can use those items with \'use <item>\''
  puts 'You can use \'look\' to get a description of your current location.'
  puts 'Use words you think will interact with your current location, using the location descriptions as hints'
  puts 'Use \'help\' to repeat these instructions'
  #puts 'Type one or two words at a time'
end

start
