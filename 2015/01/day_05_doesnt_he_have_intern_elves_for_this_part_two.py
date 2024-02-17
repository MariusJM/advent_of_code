"""
--- Part Two ---
Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
How many strings are nice under these new rules?
"""

input_file = open("day_05_input.txt", "r")
input_file_read = input_file.read()
input_data = input_file_read.splitlines()
counter = 0
# input_data = ["ugknbfddgicrmopn", "aaa", "jchzalrnumimnmhp", "haegwjzuvuyypxyu", "dvszwmarrgswjxmb"]
# line = "ieodomkazucvgmuy"

def find_pair(line):
    for i in range(len(line)-1):
        pair = line[i]+line[i+1]
        if line.count(pair) == 2:
            return True
    return False

def repeating_letter(line):
    for i in range(len(line)-2):
        if line[i] == line[i+2]:
            return True
    return False


for i in range(len(input_data)):
    if find_pair(input_data[i]) and repeating_letter(input_data[i]):
        counter += 1
print(f"Number of nice strings: {counter}")
