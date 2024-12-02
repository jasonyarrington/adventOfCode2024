#day02.py

from util.file_utils import read_file_to_array

# Read data

file_path = 'day02-test.txt'
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

def report_is_safe(levels, dampener = 0):
        previous_level = int(levels[0])
        previous_direction = None  # Initialize previous_direction

        unsafe_count = 0
        for level_index, level in enumerate(levels[1:], start=1):
            level = int(level)
            d = direction(level, previous_level)
            diff = difference(level, previous_level)
            is_safe = safety(d, previous_direction, diff)
            if not is_safe:
                unsafe_count += 1

                if unsafe_count > dampener:
                    break

                # Stop testing and retest without this element
                if (level_index > 1):
                    levels.pop(level_index)
                    # print ("Levels after pop", levels)
                    is_safe = report_is_safe(levels, dampener - 1)
                    break

            previous_level = level
            previous_direction = d

        return is_safe

def dampener(reports, dampener = 0):
    # Iterate over reports
    report_safety = []

    for report in reports:
        levels = report.split()
        is_safe = report_is_safe(levels, dampener)
        report_safety.append(is_safe)   
    return report_safety
  
report_safety = dampener(reports) 
print("Safe reports:", report_safety)
print("Number of safe reports:", report_safety.count(True))

report_safety_with_dampener = dampener(reports, 1)
# print("Safe reports with dampener:", report_safety_with_dampener)
print("Number of safe reports with dampener:", report_safety_with_dampener.count(True))