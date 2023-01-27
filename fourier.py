import data_processing as dp
import constants as const
import numpy as np


# Given a numpy array and sampling rate,
# returns numpy arrays of the frequencies and intensities
def fourier_transform(data, sampling_rate, plot=True, filename='', title='', smooth=0, label=''):

	dft = np.fft.fft(data)
	dft_freq = np.fft.fftfreq(data.size, 1/sampling_rate)
	dft = np.abs(dft)

	if smooth > 0:
		dft = dp.smooth_array(dft, smooth)

	
	return dft_freq[1:], dft[1:]


# Given an FFT plot and a frequency range, returns the
# average intensity of all signals within the frequency range.
def get_frequency_mean(fft_freqs, fft_data, min_freq, max_freq):
	
	min_index = np.where(fft_freqs==min_freq)[0][0]
	max_index = np.where(fft_freqs==max_freq)[0][0]

	mean = np.mean(fft_data[min_index:max_index])
	return mean





# Given an array, takes a sub-array from start to end.
# Then performs a Fourier transform and returns the 
# average intensity of signals within the given frequency range.
def get_wave_average(arr, start, end, min_freq, max_freq):

	sub_arr = arr[start:end]
	dft_freq, dft = fourier_transform(sub_arr, const.SAMPLING_RATE, plot=False)
	return get_frequency_mean(dft_freq, dft, min_freq, max_freq)


# Given an array, takes a sub-array from start to end.
# Then performs a Fourier transform and returns the 
# average intensity of theta waves.
def get_theta_average(arr, start, end):
	return get_wave_average(arr, start, end, const.THETA_MIN, const.THETA_MAX)


# Given an array, takes a sub-array from start to end.
# Then performs a Fourier transform and returns the 
# average intensity of alpha waves.
def get_alpha_average(arr, start, end):
	return get_wave_average(arr, start, end, const.ALPHA_MIN, const.ALPHA_MAX)


# Given a numpy array of data, returns two numpy arrays
# of the average alpha and theta wave intensities
# of each window, given a window size.
def get_alpha_theta_means(arr, window_size):

	alphas = np.array([])
	thetas = np.array([])
	
	start = 0
	length = len(arr)


	while(start + window_size < length):

		alphas = np.append(alphas, get_alpha_average(arr, start, start+window_size))
		thetas = np.append(thetas, get_theta_average(arr, start, start+window_size))

		start += window_size

	return alphas, thetas
