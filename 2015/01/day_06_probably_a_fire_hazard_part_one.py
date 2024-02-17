"""
--- Day 6: Probably a Fire Hazard ---
Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
After following the instructions, how many lights are lit?
"""

input_file = open("day_06_input.txt", "r")
input_file_read = input_file.read()
input_data = input_file_read.splitlines()

grid = [[0 for _ in range(1000)] for _ in range(1000)]


def turn_off(start_row, end_row, start_col, end_col):
    for i in range(start_row, end_row + 1):
        for j in range(start_col, end_col + 1):
            grid[i][j] = 0


def turn_on(start_row, end_row, start_col, end_col):
    for i in range(start_row, end_row + 1):
        for j in range(start_col, end_col + 1):
            grid[i][j] = 1


def toggle(start_row, end_row, start_col, end_col):
    for i in range(start_row, end_row + 1):
        for j in range(start_col, end_col + 1):
            if grid[i][j] == 1:
                grid[i][j] = 0
            else:
                grid[i][j] = 1


def count_lights():
    counter = 0
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if grid[i][j] == 1:
                counter += 1
    return counter


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


print(f"nuber of lights on: {count_lights()}")
