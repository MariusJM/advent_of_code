"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
"""

# coordinates = [0, 0]
# visited_coordinates = [[0, 0]]
# visited_houses = 1
# input_data = open("day_03_input.txt", "r")
# directions = input_data.read()

# # test cases:
# # directions = ">"
# # directions = "^>v<"
# # directions = "^v^v^v^v^v"


# for i in range(len(directions)):
#     if directions[i] == "^":
#         coordinates[1] += 1
#     elif directions[i] == ">":
#         coordinates[0] += 1
#     elif directions[i] == "v":
#         coordinates[1] -= 1
#     elif directions[i] == "<":
#         coordinates[0] -= 1

#     current_coordinates = coordinates.copy()

#     if current_coordinates not in visited_coordinates:
#         visited_coordinates.append(current_coordinates)
#         visited_houses += 1
    
#     # print(f"Visited coordinates: {visited_coordinates}")
# print(f"Visited houses: {visited_houses}")


"""
--- Part Two ---
The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
"""

santa_coordinates = [0, 0]
robo_santa_coordinates = [0, 0]

visited_coordinates = [[0, 0]]

input_data = open("day_03_input.txt", "r")
directions = input_data.read()

# test cases:
# directions = "^v" # answer 3 houses
# directions = "^>v<" # answer 3 houses
# directions = "^v^v^v^v^v" # answer 11 houses

for i in range(len(directions)):
    if i % 2 == 0:
        if directions[i] == "^":
            santa_coordinates[1] += 1
        elif directions[i] == ">":
            santa_coordinates[0] += 1
        elif directions[i] == "v":
            santa_coordinates[1] -= 1
        elif directions[i] == "<":
            santa_coordinates[0] -= 1

        current_coordinates = santa_coordinates.copy()

        if current_coordinates not in visited_coordinates:
            visited_coordinates.append(current_coordinates)
    else:
        if directions[i] == "^":
            robo_santa_coordinates[1] += 1
        elif directions[i] == ">":
            robo_santa_coordinates[0] += 1
        elif directions[i] == "v":
            robo_santa_coordinates[1] -= 1
        elif directions[i] == "<":
            robo_santa_coordinates[0] -= 1

        current_coordinates = robo_santa_coordinates.copy()

        if current_coordinates not in visited_coordinates:
            visited_coordinates.append(current_coordinates)


# print(santa_coordinates)
# print(robo_santa_coordinates)
# print(visited_coordinates)
print(f"Houses receive at least one present: {len(visited_coordinates)}")