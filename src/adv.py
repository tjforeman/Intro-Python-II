from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

items = {
    "staff" : Item('staff', 'a powerful magical staff'),
    "Sword" : Item("sword","the sharpest sword in all of the land "),
    "Note"  : Item('note', 'a mysterious note dropped in the middle of the floor'),
    "Skull" : Item("skull", 'the skull of a body that didnt make it out'),
    "Dagger" : Item("dagger", 'A silver dagger with fresh blood still on it')
}

room['outside'].add_items(items['staff'])
room['foyer'].add_items(items['Sword'])
room['overlook'].add_items(items['Note'])
room['narrow'].add_items(items['Skull'])
room['treasure'].add_items(items['Dagger'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.



new_player = Player('player_1', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    directions = ['n','s','e','w','q','h',]
    print(new_player)
    print(new_player.current_room.print_item())

    user_input = input('please enter a command or press h for help:').split(' ')
    print()
    

    if user_input[0] == "q":
        break

    if user_input[0] == "h":
        print('Pick a direction n: is for north, s: is for south e: is for east, w: is for west, and q is for quit')
        print()
    # if user_input[0] not in directions:
    #      print('I did not understand that understand that')

    
    # if len(user_input) < 0:
    #     print('I did not understand that ')


    if user_input[0] == "n":
        if new_player.current_room.n_to != 0:
            new_player.current_room = new_player.current_room.n_to
        else:
            print('there is no room in that direction')
            print()
            

    if user_input[0] == "s":
        if new_player.current_room.s_to != 0:
            new_player.current_room = new_player.current_room.s_to
        else:
            print('there is no room in that direction')
            print()
            

    if user_input[0] == "e":
        if new_player.current_room.e_to != 0:
            new_player.current_room = new_player.current_room.e_to
        else:
            print('there is no room in that direction')
            print()
            

    if user_input[0] == "w":
        if new_player.current_room.w_to != 0:
            new_player.current_room = new_player.current_room.w_to
        else:
            print('there is no room in that direction')
            print()

    if user_input[0] == 'get':
        # new_player.current_room.remove_item(user_input[1])
        new_player.get_item(user_input[1])

    if user_input[0] == 'drop':
        new_player.remove_item(user_input[1])
        new_player.current_room.add_items(user_input[1])
        

    if user_input[0] == 'i' :
        new_player.print_item()

        

            