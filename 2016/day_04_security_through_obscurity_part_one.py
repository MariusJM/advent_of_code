"""
--- Day 4: Security Through Obscurity ---
Finally, you come across an information kiosk with a list of rooms. 
Of course, the list is encrypted and full of decoy data, 
but the instructions to decode the list are barely hidden nearby. 
Better remove the decoy data first.

Each room consists of an encrypted name 
(lowercase letters separated by dashes) 
followed by a dash, 
a sector ID, and a 
checksum in square brackets.

A room is real (not a decoy) 
if the checksum is the five most common letters in the encrypted name, 
in order, with ties broken by alphabetization. For example:

aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
not-a-real-room-404[oarel] is a real room.
totally-real-room-200[decoy] is not.
Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?
"""
import re
from collections import Counter


def main():

    # input_data = "aaaaa-bbb-z-y-x-123[abxyz]"
    # input_data = "not-a-real-room-404[oarel]"
    # input_data = "a-b-c-d-e-f-g-h-987[abcde]"
    # input_data = "totally-real-room-200[decoy]"

    input_data = get_data("day_04_input.txt")
    print(f"Sum of sector ID's of real rooms: {check_data(input_data)}")

def check_data(input_data):
    answer = 0
    for data_entry in input_data:
        name, sector_id = get_name_id(data_entry)
        checksum = re.search(r'\[([a-zA-Z]+)\]', data_entry).group(1)
        letters = Counter(name)

        sorted_letters = sorted(letters.items(), key=lambda x: (-x[1], x[0]))
        calculated_checksum = "".join([letter[0] for letter in sorted_letters[:5]])

        if calculated_checksum == checksum:
            answer += sector_id
        else:
            pass
    return answer

def get_data(file_name):
    input_file = open(file_name, "r")
    input_file_read = input_file.read()
    input_data = input_file_read.splitlines()
    return input_data


def get_name_id(input_data):
    name = ""
    sector_id = ""
    for i in range(len(input_data)):
        if input_data[i].isalpha():
            name += input_data[i]
        elif input_data[i].isnumeric():
            sector_id += input_data[i]
        elif input_data[i] == "[":
            break
    return name, int(sector_id)
        

def check_order(word):
    return word == "".join(sorted(word))


if __name__ == "__main__":
    main()