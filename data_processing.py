import numpy as np
import constants as const


# ----------------------------------------- DATA PROCESSING ----------------------------------------------



# Smooths the array by taking the average of window_size data points at each point.
def smooth_array(arr, window_size, shift=1):
	new_arr = np.array([])

	for i in range(len(arr) - window_size):
		new_arr = np.append(new_arr, np.mean(arr[i:i+window_size]))

	return new_arr


# Partitions array arr into chunks of size size.
def partition_array(arr, size):

	x = [arr[i:i+size] for i in range(0, len(arr), size)]

	return x