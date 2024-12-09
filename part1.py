import numpy as np

# Need to go through two lists, pair up the smallest up to largest, and get sum of difs
file_path = "part_one_data.txt"

# Function to read and process the data file
def read_data(file_path):
    """
    Reads a file with columns of numbers and returns the data as a NumPy array.

    Parameters:
        file_path (str): Path to the file to read.

    Returns:
        numpy.ndarray: Array containing the data from the file.
    """
    try:
        # Load the data using NumPy's loadtxt function
        data = np.loadtxt(file_path)
        return data
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None
    
data = read_data(file_path)

if data is not None:
    print("Data loaded successfully:")
    left_list = data[:,0]
    right_list = data[:,1]
    sum = 0
    for i in range(len(left_list)):
        [num_1,idx_1] = [np.min(left_list),np.argmin(left_list)]
        [num_2,idx_2] = [np.min(right_list),np.argmin(right_list)]
        left_list = np.delete(left_list,idx_1)
        right_list = np.delete(right_list,idx_2)
        sum += abs(num_1-num_2)
    print(sum)
else:
    print("Failed to load data.")