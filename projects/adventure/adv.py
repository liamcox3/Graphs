
from room import Room
from player import Player
from world import World
from ast import literal_eval
from util import Stack, Queue
import random


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "projects/adventure/maps/test_line.txt"
# map_file = "projects/adventure/maps/test_cross.txt"
# map_file = "projects/adventure/maps/test_loop.txt"
# map_file = "projects/adventure/maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n']
traversal_path = []

# add total moves
total_moves = []

# opposite direction


def reversed(direction):
    if direction == "n":
        return "s"
    elif direction == "s":
        return "n"
    elif direction == "e":
        return "w"
    elif direction == "w":
        return "e"
    else:
        return None


def explore_paths():
    # create stack
    stack = Stack()

    # keep track of visited nodes
    visited = set()

    # while visited is less than total amount of rooms
    while len(visited) < len(world.rooms):
        path = []

        # for every exit in current room
        for exits in player.current_room.get_exits():

            # if exits of players current room NOT in visited
            if player.current_room.get_room_in_direction(exits) not in visited:
                # append to paths
                path.append(exits)

        # add current_room to visited
        if player.current_room not in visited:
            visited.add(player.current_room)

        # if length of path is greater than zero
        if len(path) > 0:
            random_path_movement = random.randint(0, len(path) - 1)

            # print(random_path_movement)
            stack.push(path[random_path_movement])
            player.travel(path[random_path_movement])

            # print(path)
            total_moves.append(path[random_path_movement])
        else:
            last = stack.pop()
            player.travel(reversed(last))
            total_moves.append(reversed(last))


explore_paths()
traversal_path = total_moves

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
