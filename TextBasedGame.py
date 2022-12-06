# Frances Lee
# This program is the process of move between rooms in the Simplified Text Game
# 11/23/2022

# instruction function
def show_instructions():
    print('Go to Planet 0259-S with all six special stones to defeat Thanos!')
    print('Move commands: go South, go North, go East, go West')
    print("Add to Inventory: get 'item name'")


# show player's status
def show_status(current_room, inventory, rooms, directions):
    # print current room
    print('You are in the {}'.format(current_room))
    # print inventory
    print('Inventory: {}'.format(str(inventory)))
    # print item in the room if there is one
    if 'item' in rooms[current_room]:
        print('You see a {}'.format(rooms[current_room]['item']))
    # to print directions that player can move
    if current_room != 'Planet 0259-S':
        # show player possible directions
        print('Directions:')
        for direction, room in rooms[current_room].items():
            if direction in directions:  # to not print you can move 'item' to item
                if 'item' in rooms[room]:  # to check if item in other room and to use rooms[room]['item']
                    if 'Thanos' == rooms[room]['item']:  # if there is Thanos, defeat
                        print('You can move {} to the {} to defeat {}'.format(direction, room, rooms[room]['item']))
                    else:  # otherwise get item
                        print('You can move {} to the {} to get a {}'.format(direction, room, rooms[room]['item']))
                else:  # if there is no item just print direction only
                    print('You can move {} to {}'.format(direction, room))


# add item function
def add_item(inventory, current_room, rooms):
    # add item to player's inventory
    inventory.append(rooms[current_room]['item'])
    # print the item that player retrieved
    print('{} retrieved!'.format(rooms[current_room]['item']))
    # remove item from the room
    del rooms[current_room]['item']


# move to new room upon player's commands
def get_new_state(direction_from_user, current_room, rooms):
    new_state = current_room
    if direction_from_user in rooms[current_room]:
        new_state = rooms[current_room][direction_from_user]  # Assigns new room.
    else:
        print("You can't go that way!")
    return new_state  # returns new room


# main function
def main():
    # A dictionary for rooms and directions
    rooms = {
        'Earth': {'South': 'Tesseract', 'North': 'Aether Chamber', 'West': 'Orb', 'East': 'Asgard'},
        'Aether Chamber': {'East': 'Vormir', 'South': 'Earth', 'item': 'Red Reality Stone'},
        'Vormir': {'West': 'Aether Chamber', 'item': 'Orange Soul Stone'},
        'Tesseract': {'East': 'Dark Dimension', 'North': 'Earth', 'item': 'Blue Space Stone'},
        'Dark Dimension': {'West': 'Tesseract', 'item': 'Green Time Stone'},
        'Orb': {'East': 'Earth', 'item': 'Purple Power Stone'},
        'Asgard': {'West': 'Earth', 'North': 'Planet 0259-S', 'item': 'Yellow Mind Stone'},
        'Planet 0259-S': {'South': 'Asgard', 'item': 'Thanos'}  # villain
    }
    # all the possible directions
    directions = ['North', 'South', 'East', 'West']
    # declare current room, which starts at the main room(Earth)
    current_room = 'Earth'
    # declare empty inventory to put item that retrieved
    inventory = []
    # display instructions before the game begin
    show_instructions()
    # while the game is running
    while True:
        # if the player is in the villain room
        show_status(current_room, inventory, rooms, directions)
        if current_room == 'Planet 0259-S':
            # if the inventory is full
            if len(inventory) == 6:
                print('Congratulations! You have collected all the items and defeated Thanos!')
                break  # exit the game
            # if the inventory is not full
            else:
                print('NOM NOM…GAME OVER!')
                break  # exit the game
        print('---------------------------')
        # enter player's move
        move = input('Enter your move:').split()
        move[0] = move[0].lower()  # player can enter in Upper/Lower case
        # if the move has go and entered one of the correct directions
        if 'go' == move[0]:
            direction = move[1].capitalize()  # player can enter in Upper/Lower case direction
            # if the player entered one of the four directions
            if direction in directions:
                current_room = get_new_state(direction, current_room, rooms)
            else:
                print('Invalid direction')
        # if the move has get
        elif 'get' == move[0]:
            # since there are no spacings by using split, rewrite the item in correct format
            current_item = ' '.join(move[1:]).title()
            # if the item entered matches item in the room
            if 'item' in rooms[current_room] and current_item == rooms[current_room]['item']:
                add_item(inventory, current_room, rooms)
            # if item is incorrect
            else:
                print('Can\'t get the {}'.format(current_item))
                # if command is exit
        # if player entered one word
        else:
            print('Invalid Move')
    # end message
    print('Thanks for playing the game. Hope you enjoyed it.')


# call main function
if __name__ == "__main__":
    main()
