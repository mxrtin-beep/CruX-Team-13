import numpy as np
import constants as const


# ----------------------------------------- DATA PROCESSING ----------------------------------------------



# Smooths the array by taking the average of window_size data points at each point.
def smooth_array(arr, window_size, shift=1):
	new_arr = np.array([])

	for i in range(len(arr) - window_size):
		new_arr = np.append(new_arr, np.mean(arr[i:i+window_size]))

	return new_arr

# indexed at 0
def get_nth_second(arr, n, sampling_rate):

	start = sampling_rate * n
	end = sampling_rate * (n + 1)

	if end > len(arr):
		return arr[-sampling_rate:]

	return arr[start:end]