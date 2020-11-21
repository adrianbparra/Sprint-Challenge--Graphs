from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


old_room_id = player.current_room.id
# old rooom set to none
# gets current room
new_room = player.current_room.id

rooms = {}
# create a dict
room_dict = {}

current_rooms = player.current_room.get_exits()
for room in current_rooms:
    room_dict[room] = "?"

rooms[new_room] = room_dict

room_to_explore = random.choice(current_rooms)

q = []

q.append(room_to_explore)

# print(rooms)

directions = {"n":"s","s":"n","e":"w","w":"e"}

visited = set()

visited.add(new_room)

while len(visited) < 500:

    player.travel(room_to_explore)
    # q.append(room_to_explore)

    traversal_path.append(room_to_explore)

    new_room = player.current_room.id
    
    visited.add(new_room)

    # updates old rooms
    # print(new_room)
    old_room_dict = rooms[old_room_id]
    old_room_dict[room_to_explore] = new_room
    rooms[old_room_id] = old_room_dict

    # print(f"{old_room_id} : {rooms[old_room_id]}")
    # print(q)

    # update old rooms id
    # rooms[old_room_id][room_to_explore] = new_room

    if new_room in rooms:

        # update room on id
        # rooms[new_room][directions[room_to_explore]] = old_room_id

        room_dict = rooms[new_room]
        pass
        room_dict[directions[room_to_explore]] = old_room_id
    else:
        # create the new dict for new room and updates
        room_dict = {}
        
        for room in player.current_room.get_exits():
            if room == directions[room_to_explore]:

                room_dict[directions[room_to_explore]] = old_room_id
            else:
                room_dict[room] = "?"
    # updates new rooms dict
    rooms[new_room] = room_dict
    
    
    # get new room dict directions that are not explored
    current_rooms = [key for key,value in room_dict.items() if value == "?"]

    old_room_id = player.current_room.id 
    # traverse back
    if len(current_rooms) < 1:
        room_explored = q.pop()
        room_to_explore = directions[room_explored]
        
    else:
        room_to_explore = random.choice(current_rooms)
        q.append(room_to_explore)
    
# read or 

    # gets rooms for current room {'n','e','s','w'}
# create new rooms dict
    # gets rooms for current room ['n','e','s','w']
    # creates dict with directions
# if there is old_room_id update current rooms by reading last direction in queue
# gets rooms that are not explored and shuffles them
# travels direction that is choosen
# add direction to queue
# get new room id
# updates old room dict
    # current_room[directin] = new_room id


# assigns new_room to old_room_id

'''
search for an unexplored room

get current rooms in a dict n , e , s , w

place the room explored in the bfs queue

n [0] 

loop over 

'''


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
