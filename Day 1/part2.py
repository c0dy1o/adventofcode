import numpy as np

# Need to go through two lists, and sum up the similarity scores
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
        # Get the similarity score
        count = np.count_nonzero(right_list == left_list[i])
        sum += left_list[i]*count
    print(sum)
else:
    print("Failed to load data.")