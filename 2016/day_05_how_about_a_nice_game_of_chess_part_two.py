"""
As the door slides open, you are presented with a second door that uses a slightly more inspired security mechanism. Clearly unimpressed by the last version (in what movie is the password decrypted in order?!), the Easter Bunny engineers have worked out a better solution.

Instead of simply filling in the password from left to right, the hash now also indicates the position within the password to fill. 
You still look for hashes that begin with five zeroes; 
however, now, the sixth character represents the position (0-7), 
and the seventh character is the character to put in that position.

A hash result of 000001f means that f is the second character in the password. Use only the first result for each position, and ignore invalid positions.

For example, if the Door ID is abc:

The first interesting hash is from abc3231929, which produces 0000015...; so, 5 goes in position 1: _5______.
In the previous method, 5017308 produced an interesting hash; however, it is ignored, because it specifies an invalid position (8).
The second interesting hash is at index 5357525, which produces 000004e...; so, e goes in position 4: _5__e___.
You almost choke on your popcorn as the final character falls into place, producing the password 05ace8e3.

Given the actual Door ID and this new method, what is the password? Be extra proud of your solution if it uses a cinematic "decrypting" animation.
Your puzzle input is still uqwqemis.
"""
import hashlib

def main():

    #05ace8e3
    # door_id = "abc"

    door_id = "uqwqemis"

    password = find_password(door_id)

    print(f"Password - {password}")


def find_password(door_id):
    counter = 0
    answer = ["","","","","","","",""]
    number_of_characters = 0

    while number_of_characters < 8:
        toHash = door_id + str(counter)
        door_id_encoded = hashlib.md5(toHash.encode())
        door_id_hex = door_id_encoded.hexdigest()
        if door_id_hex[:5] == "00000":
            position = door_id_hex[5]
            if position.isnumeric() and int(position) in range(0,8) and answer[int(position)] == "":
                answer[int(position)] = door_id_hex[6]
                print(answer)
                number_of_characters += 1
        counter +=1
    return "".join(answer)
    

if __name__ == "__main__":
    main()

