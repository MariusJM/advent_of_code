"""
--- Part Two ---
You finally arrive at the bathroom (it's a several minute walk from the lobby so visitors can behold the many fancy conference rooms and water coolers on this floor) and go to punch in the code. Much to your bladder's dismay, the keypad is not at all like you imagined it. Instead, you are confronted with the result of hundreds of man-hours of bathroom-keypad-design meetings:

    1
  2 3 4
5 6 7 8 9
  A B C
    D
You still start at "5" and stop when you're at an edge, but given the same instructions as above, the outcome is very different:

You start at "5" and don't move at all (up and left are both edges), ending at 5.
Continuing from "5", you move right twice and down three times (through "6", "7", "B", "D", "D"), ending at D.
Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), ending at B.
Finally, after five more moves, you end at 3.
So, given the actual keypad layout, the code would be 5DB3.

Using the same instructions in your puzzle input, what is the correct bathroom code?
"""
def main():

    input_file = open("day_02_input.txt", "r")
    input_file_read = input_file.read()
    input_data = input_file_read.splitlines()

    # input_data = ["ULL", "RRDDD", "LURDL", "UUUUD"]
    # print(input_data)

    current_position = 5
    answer_numeric = []

    for i in range(len(input_data)):
        current_position = get_number(current_position, input_data[i])
        answer_numeric.append(current_position)
    
    finall_answer = convert_answer(answer_numeric)
    print(finall_answer)

def convert_answer(answer_numeric):
    answer_alnum = ""
    for i in answer_numeric:
        if i == 10:
            answer_alnum += "A"
        elif i == 11:
            answer_alnum += "B"
        elif i == 12:
            answer_alnum += "C"
        elif i == 13:
            answer_alnum += "D"
        else:
            answer_alnum += str(i)
    return answer_alnum


def get_number(current_position,instructions):
    for i in range(len(instructions)):
        if instructions[i] == "L":
            current_position = go_left(current_position)
        elif instructions[i] == "R":
            current_position = go_right(current_position)
        elif instructions[i] == "U":
            current_position = go_up(current_position)
        else:
            current_position = go_down(current_position)
    return current_position

def go_left(current_position):
    border = [1, 2, 5, 10, 13]
    if current_position in border:
        return current_position
    else:
        current_position -= 1
        return current_position


def go_right(current_position):
    border = [1, 4, 9, 12, 13]
    if current_position in border:
        return current_position
    else:
        current_position += 1
        return current_position


def go_up(current_position):
    border = [5, 2, 1, 4, 9]
    if current_position in border:
        return current_position
    elif current_position in [3, 13]:
        current_position -= 2
        return current_position
    else:
        current_position -= 4
        return current_position

def go_down(current_position):
    border = [5, 9, 10, 12, 13]
    if current_position in border:
        return current_position
    elif current_position in [1, 11]:
        current_position += 2
        return current_position
    else:
        current_position += 4
        return current_position




if __name__ == "__main__":
    main()