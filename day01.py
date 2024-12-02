# day1.py
from util.file_utils import read_file_to_array

# Example usage
file_path = 'day01.txt'
array = read_file_to_array(file_path)

left_list = []
right_list = []

# Split int two lists
for line in array:
    parts = line.split()
    if (len(parts) > 1):
        left_list.append(int(parts[0]))
        right_list.append(int(parts[1]))

# # Sort lists
left_list.sort()
right_list.sort()

distances = []

for i in range(len(left_list)):
    distances.append(abs(right_list[i] - left_list[i]))

# print("Distances:", distances)

# # Sum of distances
sum_distances = sum(distances)

print("Sum of distances:", sum_distances)

# # Add number of times the number shows up in the second list
left_list_instances = {}

for i in range(len(left_list)):
    value = left_list[i]
    if left_list_instances.get(value):
        exit
    else:    
        left_list_instances[value] = right_list.count(value)
        

print("Left list instances:", left_list_instances)

similarity_score = 0

for i in range(len(left_list)):
    value = left_list[i]
    similarity_score += value * left_list_instances[value]

print("Similarity score:", similarity_score)
