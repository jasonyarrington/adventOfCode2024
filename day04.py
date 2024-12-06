#day04.py

from util.file_utils import read_file_to_array
import re

file_path = 'day04.txt'

lines = read_file_to_array(file_path)

# Part 1
matches = 0
pattern = 'XMAS'

directions = [
    (1, 0), # right
    (1, 1), # up right
    (0, 1), # up
    (-1, 1), # up left
    (-1, 0), # left
    (-1, -1), # down left
    (0, -1), # down
    (1, -1) # down right
]

for line_index in range(len(lines)):
    for char_index in range(len(lines[line_index])):
        if (lines[line_index][char_index] == pattern[0]):
            # in each direction
            for direction in directions:
                test_string = ''
                test_string += pattern[0]
                # get next 3 characters
                for i in range(1, len(pattern)):
                    next_char_index = [line_index + direction[0] * i, char_index + direction[1] * i]
                    # test out of range
                    if (next_char_index[0] < 0 or next_char_index[0] >= len(lines) or next_char_index[1] < 0 or next_char_index[1] >= len(lines[next_char_index[0]])):
                        break
                    test_string += lines[next_char_index[0]][next_char_index[1]]
                
                print (test_string)
                if (test_string == pattern):
                    matches += 1
          
print ('part 1: ', matches)


# Part 2

# Match
# M - M
# - A -
# S - S

# Looked for A then got the four corners around A
# Then checked if there are 2 M and 2 S and at least one MM or SS

directions = [
    (1, 1), # up right
    (-1, 1), # up left
    (-1, -1), # down left
    (1, -1) # down right
]

matches = 0

for line_index in range(len(lines)):

    for char_index in range(len(lines[line_index])):
        if (lines[line_index][char_index] == 'A'):
            test_string = ''
            for direction in directions:
                next_char_index = [line_index + direction[0] * i, char_index + direction[1] * i]
                # test out of range
                if (next_char_index[0] < 0 or next_char_index[0] >= len(lines) or next_char_index[1] < 0 or next_char_index[1] >= len(lines[next_char_index[0]])):
                    break
                test_string += lines[next_char_index[0]][next_char_index[1]]
            if (test_string.count('M') == 2 and test_string.count('S') == 2 and (test_string.count('MM') == 1 or test_string.count('SS') == 1)):
                print (test_string)
                matches += 1 

print ('part 2: ', matches)