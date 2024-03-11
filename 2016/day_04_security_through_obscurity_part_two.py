"""
With all the decoy data out of the way, it's time to decrypt this list and get moving.

The room names are encrypted by a state-of-the-art shift cipher, 
which is nearly unbreakable without the right software. 
However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.

To decrypt a room name, 
rotate each letter forward through the alphabet a number of times equal to the room's sector ID.
A becomes B, 
B becomes C, 
Z becomes A, and so on. 
Dashes become spaces.

For example, the real name for 
qzmt-zixmtkozy-ivhz-343 is 
very encrypted name.

What is the sector ID of the room where 
North Pole objects are stored?
"""
import re
from collections import Counter


def main():

    input_data = get_data("day_04_input.txt")
    # input_data = "qzmt-zixmtkozy-ivhz-343"
    # input_data = "abcz1"
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for data_entry in input_data:
        name, sector_id = get_name_id(data_entry)
        decoded_name = decode_name(name, sector_id, alphabet)
        if "object" in decoded_name:
            print(f"{decoded_name} Sector ID: {sector_id}")


def decode_name(name, sector_id, alphabet):
    decoded_name = ""
    for i in range(len(name)):
        if name[i] == " ":
            decoded_name += " "
        else:
            character_index = alphabet.index(name[i])
            new_character_index = (character_index+sector_id)%26
            decoded_name += alphabet[new_character_index]
    return decoded_name.split(" ")


def get_name_id(input_data):
    name = ""
    sector_id = ""
    for i in range(len(input_data)):
        if input_data[i].isalpha():
            name += input_data[i]
        elif input_data[i].isnumeric():
            sector_id += input_data[i]
        elif input_data[i] == "-":
            name += " "
        elif input_data[i] == "[":
            break
    return name, int(sector_id)


def get_data(file_name):
    input_file = open(file_name, "r")
    input_file_read = input_file.read()
    input_data = input_file_read.splitlines()
    return input_data


if __name__ == "__main__":
    main()