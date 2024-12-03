def ifCliff(value):

    # value is double digits
    if value > 9:
        return True
    
    # value is even
    if value % 2 == 0:
        return True
    
    return False


# data
myValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# For each value in myValues
for value in myValues:
    # Check if value is a cliff
    if ifCliff(value):
        print(f"{value} is a cliff")
    else:
        print(f"{value} is not a cliff")