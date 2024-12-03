#day03.py

import re
from util.file_utils import read_file_to_array

file_path = 'day03-test.txt'

instructions = ''
with open(file_path, 'r') as file:
    instructions = file.read()

# Define the regex pattern to match mul(#,#)
# pattern = r'mul\((\d+),(\d+)\)'
pattern = r'mul\((\d+),(\d+)\)'

matches = re.findall(pattern, instructions)

total = 0
if matches:
    for match in matches:
        num1, num2 = match[0], match[1]
        print(f'Match: mul({num1},{num2})')
        total += int(num1) * int(num2)

print (total)
print (len(matches))