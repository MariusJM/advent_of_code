"""
--- Part Two ---
You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

turn on 0,0 through 0,0 would increase the total brightness by 1.
toggle 0,0 through 999,999 would increase the total brightness by 2000000.
"""

input_file = open("day_06_input.txt", "r")
input_file_read = input_file.read()
input_data = input_file_read.splitlines()

grid = [[0 for _ in range(1000)] for _ in range(1000)]


def turn_off(start_row, end_row, start_col, end_col):
    for i in range(start_row, end_row + 1):
        for j in range(start_col, end_col + 1):
            if grid[i][j] != 0:
                grid[i][j] -= 1


def turn_on(start_row, end_row, start_col, end_col):
    for i in range(start_row, end_row + 1):
        for j in range(start_col, end_col + 1):
            grid[i][j] += 1


def toggle(start_row, end_row, start_col, end_col):
    for i in range(start_row, end_row + 1):
        for j in range(start_col, end_col + 1):
            grid[i][j] += 2


def count_lights():
    total_brightness = 0
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            total_brightness += grid[i][j]
    return total_brightness


for i in range(len(input_data)):
    line = input_data[i].split()
    if line[0] == "toggle":
        start_row, start_col = map(int, line[1].split(","))
        end_row, end_col = map(int, line[3].split(","))
        toggle(start_row, end_row, start_col, end_col)
    elif line[1] == "on":
        start_row, start_col = map(int, line[2].split(","))
        end_row, end_col = map(int, line[4].split(","))
        turn_on(start_row, end_row, start_col, end_col)
    else:
        start_row, start_col = map(int, line[2].split(","))
        end_row, end_col = map(int, line[4].split(","))
        turn_off(start_row, end_row, start_col, end_col)

print(f"Total brightness: {count_lights()}")
