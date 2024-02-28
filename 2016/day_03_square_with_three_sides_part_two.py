"""
Now that you've helpfully marked up their design documents, 
it occurs to you that triangles are specified in groups of three vertically. 
Each set of three numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:

101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?
"""

def main():
    input_file = open("day_03_input.txt", "r")
    input_file_read = input_file.read()
    input_data = input_file_read.splitlines()
    row_data = [list(map(int, row.split())) for row in input_data]
    # print(row_data)
    column_data = list(map(list, zip(*row_data)))
    # print(column_data[0])
    valid_triangles = 0
    for column in column_data:
        for i in range(0, len(column), 3):
            triangle_data = sorted(column[i:i+3])
            if triangle_data[0] + triangle_data[1] > triangle_data[2]:
                valid_triangles += 1

    print(f"Number of valid triangles: {valid_triangles}")

if __name__ == "__main__":
    main()