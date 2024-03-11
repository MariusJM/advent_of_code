"""
--- Day 6: Signals and Noise ---
Something is jamming your communications with Santa. Fortunately, your signal is only partially jammed, and protocol in situations like this is to switch to a simple repetition code to get the message through.

In this model, the same message is sent repeatedly. You've recorded the repeating message signal (your puzzle input), but the data seems quite corrupted - almost too badly to recover. Almost.

All you need to do is figure out which character is most frequent for each position. For example, suppose you had recorded the following messages:

eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
The most common character in the first column is e; in the second, a; in the third, s, and so on. Combining these characters returns the error-corrected message, easter.

Given the recording in your puzzle input, what is the error-corrected version of the message being sent?
"""

def main():
    input_data = get_data("day_06_input.txt")

    error_corrected_message = count_characters(input_data)
    
    print(f"Error-corrected message: {error_corrected_message}")


def count_characters(data):
    characters_by_position = []
    for i in range(len(data[0])):
        characters = {}
        for j in range(len(data)):
            if data[j][i] not in characters:
                characters[data[j][i]] = 1
            else:
                characters[data[j][i]] += 1
        max_key = max(characters, key=characters.get)
        characters_by_position.append(max_key)

    return "".join(characters_by_position)


def get_data(file_name):
    with open(file_name, "r") as input_file:
        input_data = input_file.read().splitlines()
    return input_data


if __name__ == "__main__":
    main()