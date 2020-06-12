from room import Room
from player import Player
from items import Item
import argparse


# parser = argparse.ArgumentParser()
# parser.add_argument('n', type=str)
# args = parser.parse_args()
# if args.n:
#     print(f'current room: {player1.current_room}')
# elif args.w:
#     pass
# Declare all the rooms

# room = {
#     'outside':  Room("Outside Cave Entrance",
#                      "North of you, the cave mount beckons"),

#     'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
# passages run north and east."""),

#     'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm."""),

#     'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
# to north. The smell of gold permeates the air."""),

#     'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south."""),
# }

outside = Room("Outside Cave Entrance", "North of you, the cave mount beckons")

foyer = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""")

overlook = Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

narrow = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

treasure = Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")


# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

outside.n_to = foyer
foyer.s_to = outside
foyer.n_to = overlook
foyer.e_to = narrow
overlook.s_to = foyer
narrow.w_to = foyer
narrow.n_to = treasure
treasure.s_to = narrow

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('steve')
player.current_room = outside
foyer.add_item('sword')
treasure.add_item('shield')
# Write a loop that:
#
# * Prints the current room name
print(player.current_room.name)
# * Prints the current description (the textwrap module might be useful here).
print(player.current_room.description)

sword = Item('sword', 'special sword')
shield = Item('shield', 'special shield')
# player.get_item(sword)
# player.get_item(shield)
# print(player.items)

# * Waits for user input and decides what to do.
user = input('enter command: [move NSWE] [get/drop] [name item]: ')
direction = user.split(' ')[0]

if len(user.split(' ')) > 1:
    action = user.split(' ')[1]
    item_name = user.split(' ')[2]


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while not direction == 'q':
    if direction in {'n', 's', 'w', 'e'}:
        if hasattr(player.current_room, f'{direction}_to'):
            player.current_room = getattr(
                player.current_room, f'{direction}_to')
            print(player.current_room)
            user = input('choose direction: N, S, W, E,  --or-- q to quit: ')
            direction = user.split(' ')[0]
            if direction in {'i', 'get', 'drop'}:
                if direction == "i":
                    print(player.items)
                elif direction == 'get':
                    item = user.split(' ')[1]
                    if player.current_room.items.count(f'{item}') > 0:
                        print(player.current_room.items)
                        player.get_item(sword)
                        player.current_room.items.remove(f'{item}')
                        print(player.current_room.items)
                    else:
                        print('no such item in room')
                elif direction == 'drop':
                    item = user.split(' ')[0]
                    print(player.items)
                    player.drop_item(item)
                    print(player.items)

                # user = input('choose direction: N, S, W, E --or-- q to quit: ')
        else:
            print('cannot move in that direction')
            user = input('choose direction: N, S, W, E --or-- q to quit: ')
            direction = user.split(' ')[0]

    else:
        print('enter in a valid direction')
        user = input('choose direction: N, S, W, E --or-- q to quit: ')
        direction = user.split(' ')[0]
