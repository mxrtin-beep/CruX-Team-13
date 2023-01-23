
'''
The data

240441 time points (rest)
64 electrodes



'''
import matplotlib.pyplot as plt
import numpy as np
import h5py


SAMPLING_RATE = 1000
ALPHA_MIN = 8
ALPHA_MAX = 12
THETA_MIN = 4
THETA_MAX = 7



def save_plot(filename, arr, title = '', xlabel = '', ylabel = ''):
    #plt.switch_backend('Agg')
    plt.plot(arr)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.savefig(filename + ".png")
    plt.figure()
 

# file: filename
# Returns object of type Database
def load_data(file):
	print("Loading data " + file)
	return h5py.File(file)

# Given an object of type Database and a timestamp,
# returns a numpy array of all channel values at that time.
def get_one_timestamp(database, timestamp):
	return database['data'][timestamp]

# Given an object of type Database and a channel,
# returns a numpy array of the entire recording of that channel.
def get_one_channel(database, channel):
	print("Acquiring channel " + str(channel) + " from database " + str(database))
	return database['data'][:, channel]


# Given a numpy array and sampling rate,
# returns numpy arrays of the frequencies and intensities
def fourier_transform(data, sampling_rate, plot=True, filename='', title=''):

	dft = np.fft.fft(data)
	dft_freq = np.fft.fftfreq(data.size, 1/sampling_rate)
	dft = np.abs(dft)

	if plot:
		plt.figure(figsize = (8, 8))
		plt.plot(dft_freq, dft)
		plt.xlim([1, 35])
		plt.ylim([0, 10000])
		plt.xlabel('Frequency (Hz)')
		plt.ylabel('Intensity')
		plt.title(title)
		plt.savefig(filename + ".png")
		plt.figure()

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
	dft_freq, dft = fourier_transform(sub_arr, SAMPLING_RATE, plot=False)
	return get_frequency_mean(dft_freq, dft, min_freq, max_freq)


# Given an array, takes a sub-array from start to end.
# Then performs a Fourier transform and returns the 
# average intensity of theta waves.
def get_theta_average(arr, start, end):
	return get_wave_average(arr, start, end, THETA_MIN, THETA_MAX)


# Given an array, takes a sub-array from start to end.
# Then performs a Fourier transform and returns the 
# average intensity of alpha waves.
def get_alpha_average(arr, start, end):
	return get_wave_average(arr, start, end, ALPHA_MIN, ALPHA_MAX)


# Given a numpy array of data, returns two numpy arrays
# of the average alpha and theta wave intensities
# of each window, given a window size.
def get_alpha_theta_means(arr, window_size):

	alphas = np.array([])
	thetas = np.array([])
	
	start = 0
	length = len(arr)


	while(start + window_size < length):

		print("Analyzing Window " + str(start / window_size))
		alphas = np.append(alphas, get_alpha_average(arr, start, start+window_size))
		thetas = np.append(thetas, get_theta_average(arr, start, start+window_size))

		start += window_size

	return alphas, thetas


def main():

	size = 5000
	start = 50000

	memory_data = load_data("assets/sub-042_eeg_sub-042_task-memory_eeg.set")
	rest_data = load_data("assets/sub-042_eeg_sub-042_task-rest_eeg.set")

	#print(rest_data.keys())

	rest_channel_0 = get_one_channel(rest_data, 0)
	memory_channel_0 = get_one_channel(memory_data, 0)
	
	#save_plot('rest_channel_0', rest_channel_0, title='Resting Channel 0', xlabel='Time', ylabel='Signal')
	#save_plot('memory_channel_0', memory_channel_0, title='Memory Channel 0', xlabel='Time', ylabel='Signal')

	#rest_dft_freq, rest_dft = fourier_transform(rest_channel_0, SAMPLING_RATE, filename='Rest_DFT', title='Rest_DFT')
	#memory_dft_freq, memory_dft = fourier_transform(memory_channel_0, SAMPLING_RATE, filename='Memory_DFT', title='Memory_DFT')

	rest_alphas, rest_thetas = get_alpha_theta_means(rest_channel_0, size)
	memory_alphas, memory_thetas = get_alpha_theta_means(memory_channel_0, size)

	plt.bar(1, np.mean(rest_alphas), label="Rest Alpha Average")
	plt.bar(2, np.mean(rest_thetas), label="Rest Theta Average")
	plt.bar(3, np.mean(memory_alphas), label="Memory Alpha Average")
	plt.bar(4, np.mean(memory_thetas), label="Memory Theta Average")
	plt.legend()
	plt.title("Rest and Memory Average Alpha and Theta Intensities")
	plt.ylabel("Average Intensity")
	plt.savefig("Bar.png")
	plt.figure()

	print("Hello World!")

if __name__ == "__main__":
    main()