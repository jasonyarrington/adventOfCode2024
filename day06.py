#day06.py

file_path = 'day06-test.txt'

def read_file_to_array(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content.split('\n\n')

map = read_file_to_array(file_path)

for i, group in enumerate(map):
    map[i] = list(group)

print (map)