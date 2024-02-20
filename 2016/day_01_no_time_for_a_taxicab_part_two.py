"""--- Part Two ---
Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?
"""

def move_east(current_location, visited_locations, n):
    for i in range(n):
        current_location = [current_location[0] + 1, current_location[1]]
        if current_location not in visited_locations:
            visited_locations.append(current_location)
        else:
            print(f"Location {current_location} has been visited before")
            location_visited = True
            return current_location, visited_locations, location_visited
    return current_location, visited_locations, False


def move_south(current_location, visited_locations, n):
    for i in range(n):
        current_location = [current_location[0], current_location[1]-1]
        if current_location not in visited_locations:
            visited_locations.append(current_location)
        else:
            print(f"Location {current_location} has been visited before")
            location_visited = True
            return current_location, visited_locations, location_visited
    return current_location, visited_locations, False

def move_west(current_location, visited_locations, n):
    for i in range(n):
        current_location = [current_location[0] - 1, current_location[1]]
        if current_location not in visited_locations:
            visited_locations.append(current_location)
        else:
            print(f"Location {current_location} has been visited before")
            location_visited = True
            return current_location, visited_locations, location_visited
    return current_location, visited_locations, False

def move_north(current_location, visited_locations, n):
    for i in range(n):
        current_location = [current_location[0], current_location[1]+1]
        if current_location not in visited_locations:
            visited_locations.append(current_location)
        else:
            print(f"Location {current_location} has been visited before")
            location_visited = True
            return current_location, visited_locations, location_visited
    return current_location, visited_locations, False


starting_coordinates = [0,0]
orientation = "N"
visited_locations = []
location_visited = False

input_file = open("day_01_input.txt", "r")
input_file_read = input_file.read()
input_data = input_file_read.split(", ")
# input_data = ["R8", "R4", "R4", "R8",]

for i in range(len(input_data)):
    direction = input_data[i][0]
    distance = int(input_data[i][1::])
    if not location_visited:
        if orientation == "N":
            if direction == "L":
                starting_coordinates, visited_locations, location_visited = move_west(starting_coordinates, visited_locations,distance)
                orientation = "W"
            else:
                starting_coordinates, visited_locations, location_visited = move_east(starting_coordinates, visited_locations,distance)
                orientation = "E"
        elif orientation == "E":
            if direction == "L":
                starting_coordinates, visited_locations, location_visited = move_north(starting_coordinates, visited_locations,distance)
                orientation = "N"
            else:
                starting_coordinates, visited_locations, location_visited = move_south(starting_coordinates, visited_locations,distance)
                orientation = "S"
        elif orientation == "S":
            if direction == "L":
                starting_coordinates, visited_locations, location_visited = move_east(starting_coordinates, visited_locations,distance)
                orientation = "E"
            else:
                starting_coordinates, visited_locations, location_visited = move_west(starting_coordinates, visited_locations,distance)
                orientation = "W"
        elif orientation == "W":
            if direction == "L":
                starting_coordinates, visited_locations, location_visited = move_south(starting_coordinates, visited_locations,distance)
                orientation = "S"
            else:
                starting_coordinates, visited_locations, location_visited = move_north(starting_coordinates, visited_locations,distance)
                orientation = "N"
answer = abs(starting_coordinates[0])+abs(starting_coordinates[1])
print(f"Answer = {answer}")
