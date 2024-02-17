"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?
"""

vowels = ["a", "e", "i", "o", "u"]
naughty_strings = ["ab", "cd", "pq", "xy"]

input_file = open("day_05_input.txt", "r")
input_file_read = input_file.read()
input_data = input_file_read.splitlines()
# input_data = ["ugknbfddgicrmopn", "aaa", "jchzalrnumimnmhp", "haegwjzuvuyypxyu", "dvszwmarrgswjxmb"]


counter = 0
def twice_in_row(line):
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            return True
    return False


def count_vowels(line):
    counter = 0
    for i in range(len(line)):
        if line[i] in vowels:
            counter += 1
    if counter >=3:
        return True
    else:
        return False


def naughty_string(line):
    for i in range(len(line)-1):
        string = line[i]+line[i+1]
        if string in naughty_strings:
            return False
    return True

def naughty_or_not(line):
    if twice_in_row(line) and count_vowels(line) and naughty_string(line):
        return True
    else:
        return False


for i in range(len(input_data)):
    line = input_data[i]
    print(line)
    print(naughty_or_not(line))
    if naughty_or_not(input_data[i]):
        counter += 1
print(f"Number of nice strings: {counter}")