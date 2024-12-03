#day03.py

import re
from util.file_utils import read_file_to_array

file_path = 'day03.txt'

instructions = ''
with open(file_path, 'r') as file:
    instructions = file.read()

# Define the regex pattern to match mul(#,#)
# pattern = r'mul\((\d+),(\d+)\)'
pattern = r'(do\(\))|(don\'t\(\))|(mul\((\d+),(\d+)\))'

matches = re.findall(pattern, instructions)

total = 0
is_instructions_on = True
if matches:
    for match in matches:
        if match[0]:
            print(f'Match: do()')
            is_instructions_on = True
        elif match[1]:
            print(f'Match: don\'t()')
            is_instructions_on = False
        elif match[2] and is_instructions_on:
            num1, num2 = match[3], match[4]
            print(f'Match: mul({num1},{num2})')
            total += int(num1) * int(num2)

print (total)
print (len(matches))