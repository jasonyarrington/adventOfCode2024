#day5.py

file_path = 'day05.txt'

def read_file_to_array(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content.split('\n\n')

def middle_element(array):
    middle_index = 0
    if len(array) % 2 == 0:
        middle_index = ( len(array) // 2 - 1 )  
    else: 
        middle_index = ( len(array) - 1) // 2
    return array[middle_index]
# Read the file and split on two carriage returns
sections = read_file_to_array(file_path)

rules = sections[0].split('\n')
for i, rule in enumerate(rules):
    rules[i] = rule.split('|')

updates = sections[1].split('\n')

# Part 1
# For each update see if the update is in order
good_updates = []
bad_updates = []

for i, update in enumerate(updates):
    is_update_good = True
    for page_num, page in enumerate(update.split(',')):
        if page_num == 0:
            continue
        for rule in rules :
            if (rule[0] != page):
                continue
            if (rule[1] in update.split(',')[:page_num]):
                is_update_good = False
                break
        if not is_update_good:
            break
    if is_update_good:
        good_updates.append(update)
    else:
        bad_updates.append(update)
        # for rule in rules:

print (good_updates) 

answer = 0
for update in good_updates:
    update_array = update.split(',')
    
    print (middle_element(update_array))
    mid = middle_element(update_array)
    answer += int(mid)

print (answer)
print ('---')

# Part 2

# For each bad update, re-order them


for i, bad_update in enumerate(bad_updates):
    update = bad_update.split(',')
    print ('Update')
    print (update)
    page_num = 0
    for len_update in range(len(update)):
        for page_num, page in enumerate(update):
            print ('Page Num', page_num)
            if page_num == 0:
                continue
            for rule in rules :
                if (rule[0] != page): # rule doesn't apply
                    continue
                if (rule[1] in update[:page_num]): # rule applies and violated
                    index = update.index(rule[1])
                    print ('Index', index)
                    print ('Page Num', page_num)
                    update[page_num], update[index] = update[index], update[page_num]
                    break

    print (update)
    bad_updates[i] = update
    print ('---')

# print (bad_updates)

answer = 0
for update in bad_updates:
    
    print (middle_element(update))
    mid = middle_element(update)
    answer += int(mid)

print (answer)