#day02.py

from util.file_utils import read_file_to_array
from util.print_status import print_status
from util.colorize import colorize
# Read data

file_path = 'day02.txt'
reports = read_file_to_array(file_path)

def direction(level, previous_level):
    if level > previous_level:
        return 'U'
    elif level < previous_level:
        return 'D'
    else:
        return 'S'
    
def difference(level, previous_level):
    return abs(level - previous_level)

def safety(direction, previous_direction, difference):
    
    if (previous_direction == None or direction == previous_direction) and difference <= 3 and direction != 'S':
        return True
    else:
        return False

def report_is_safe(levels):
        previous_level = int(levels[0])
        previous_direction = None  # Initialize previous_direction

        for level_index, level in enumerate(levels[1:], start=1):
            level = int(level)
            d = direction(level, previous_level)
            diff = difference(level, previous_level)
            is_safe = safety(d, previous_direction, diff)
            if not is_safe:
                break

            previous_level = level
            previous_direction = d

        return is_safe, level_index

def dampener(reports, dampener = 0):
    # Iterate over reports
    report_safety = []
    level_indices = []
    for report in reports:
        levels = report.split()
        is_safe, level_index = report_is_safe(levels)

        if not is_safe:
            level_indices.append(level_index)
        else:
            level_indices.append(None)

        if not is_safe:
            new_list = levels.copy()
            new_list.pop(level_index)
            is_safe, level_index_new = report_is_safe(new_list)

        if not is_safe and level_index > 0:
            new_list = levels.copy()
            new_list.pop(level_index - 1)
            is_safe, level_index_new = report_is_safe(new_list)

        if not is_safe and level_index > 1:
            new_list = levels.copy()
            new_list.pop(level_index - 2)
            is_safe, level_index_new = report_is_safe(new_list)

        report_safety.append(is_safe)   
    return report_safety, level_indices

# Part 1  
report_safety = []
for report in reports:
    levels = report.split()
    is_safe, level_index = report_is_safe(levels)
    report_safety.append(is_safe)

report_safety_with_dampener, level_indices = dampener(reports, 1)

for i, report in enumerate(reports):
    if (not report_safety[i] and not report_safety_with_dampener[i] or 1 == 1):
        print_status(report_safety[i], '')
        print_status(report_safety_with_dampener[i], '')
        levels = report.split()
        for j, level in enumerate(levels):
            if j == level_indices[i]:
                colorize('red', level)
            else:
                print(level, end = ' ')
        print()

print("Number of safe reports:", report_safety.count(True))
print("Number of safe reports with dampener:", report_safety_with_dampener.count(True))