import numpy as np

# Need to go through two lists, pair up the smallest up to largest, and get sum of difs
file_path = "Day 2/part_one_data.txt"



def check_safe(int_list):
    # Read in the list and check if it's safe or not
    # First check if increase or decrease
    increment_sign = np.sign(int_list[1]-int_list[0])
    # If positive, it's increasing
    for i in range(1,len(int_list)):
        dif = int_list[i] - int_list[i-1]
        if dif/increment_sign < 4 and dif/increment_sign > 0:
            # We're good, keep going
            pass
        else:
            return 0
    return 1

     
# Function to read and process the data file
with open(file_path, "r") as file:
    sum = 0
    for line in file:
        # Process the line
        number_list = line.strip()
        number_list = number_list.split(" ")
        # Convert to int
        c = [int(x) for x in number_list]
        # Now check if the numbers are increasing or decreasing
        sum += check_safe(c)
    print(sum)
