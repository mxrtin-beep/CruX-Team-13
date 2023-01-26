
'''
The data

240441 time points (rest)
64 electrodes



'''
import matplotlib.pyplot as plt
import numpy as np
import h5py
import pandas as pd
import scipy.signal as sig


N_CHANNELS = 64
SAMPLING_RATE = 1000
ALPHA_MIN = 8
ALPHA_MAX = 12
THETA_MIN = 4
THETA_MAX = 7
STATES = ['memory', 'rest']
DIRECTORY = "charts/"



# ---------------------------------------------- DATA ----------------------------------------------

# file: filename
# Returns object of type Database
def load_data(file):
	print("Loading data..." + str(file))
	return h5py.File(file)






# Given an object of type Database and a timestamp,
# returns a numpy array of all channel values at that time.
def get_one_timestamp(database, timestamp):
	return database['data'][timestamp]

# Given an object of type Database and a channel number,
# returns a numpy array of the entire recording of that channel.
def get_one_channel(database, channel):
	#print("Acquiring channel " + str(get_channel_name(channel)) + " from database " + str(database))
	return database['data'][:, channel]







# Given a channel number, gives you the name (Fz, Pz, etc.)
def get_channel_name(channel_index):

	data=pd.read_csv('assets/channels.tsv',sep='\t')

	return data['name'].iloc[channel_index]


# Given a channel name (Fz, Pz), returns the channel index (0, 1, 2, etc)
def get_channel_index(channel_name):

	data=pd.read_csv('assets/channels.tsv',sep='\t')

	return data[data['name'] == channel_name].index.item()






# Returns the data for one channel given a subject (int) and channel number.
# Task is "memory" or "rest"
def get_channel_data(subject, channel, task):

	filename = get_filename(subject, task)
	data = load_data(filename)
	return get_one_channel(data, channel)


# Given a subject (number) and task (memory or rest), returns the name of the file for that.
def get_filename(subject, task):
	filename = "assets/sub-0" + str(subject) + "_eeg_sub-0" + str(subject) + "_task-" + task + "_eeg.set"
	return filename

# ----------------------------------------- DATA PROCESSING ----------------------------------------------


# Smooths the array by taking the average of window_size data points at each point.
def smooth_array(arr, window_size, shift=1):
	new_arr = np.array([])

	for i in range(len(arr) - window_size):
		new_arr = np.append(new_arr, np.mean(arr[i:i+window_size]))

	return new_arr



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

		alphas = np.append(alphas, get_alpha_average(arr, start, start+window_size))
		thetas = np.append(thetas, get_theta_average(arr, start, start+window_size))

		start += window_size

	return alphas, thetas



# ----------------------------------------- PLOTTING ----------------------------------------------


def save_plot(filename, arr, title = '', xlabel = '', ylabel = ''):
    #plt.switch_backend('Agg')
    plt.plot(arr)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.savefig(DIRECTORY + filename + ".png")
    plt.figure()
 
def save_raw(filename, arr, title):

	save_plot(filename, arr, title, xlabel="Time (s)", ylabel="Signal (mV)")


def create_bar_chart(subject, channel_name, size=5000, alpha=True, theta=True):

	channel = get_channel_index(channel_name)

	memory_channel = get_channel_data(subject, channel, 'memory')
	rest_channel = get_channel_data(subject, channel, 'rest')

	rest_alphas, rest_thetas = get_alpha_theta_means(rest_channel, size)
	memory_alphas, memory_thetas = get_alpha_theta_means(memory_channel, size)

	if alpha:
		plt.bar(1, np.mean(rest_alphas), label="Rest Alpha Average")
		plt.bar(3, np.mean(memory_alphas), label="Memory Alpha Average")

	if theta: 
		plt.bar(2, np.mean(rest_thetas), label="Rest Theta Average")
		plt.bar(4, np.mean(memory_thetas), label="Memory Theta Average")
	plt.legend()
	title_string = "Rest and Memory Avg. Alpha and Theta Intensities: Subject " + str(subject) + "; Channel " + str(channel_name) 
	plt.title(title_string)
	plt.ylabel("Average Intensity")
	fig_string = "Bar-Subject-" + str(subject) + "-Channel-" + str(channel_name)
	plt.savefig(DIRECTORY + fig_string)
	plt.figure()

# ----------------------------------------- FOURIER TRANSFORM ----------------------------------------------



# Given a numpy array and sampling rate,
# returns numpy arrays of the frequencies and intensities
def fourier_transform(data, sampling_rate, plot=True, filename='', title='', smooth=0, label=''):

	dft = np.fft.fft(data)
	dft_freq = np.fft.fftfreq(data.size, 1/sampling_rate)
	dft = np.abs(dft)

	if smooth > 0:
		dft = smooth_array(dft, smooth)

	if plot:
		plt.plot(dft_freq[0:len(dft)], dft, label=label)
		plt.legend()
		plt.xlim([1, 35])
		plt.ylim([0, 10000])
		plt.xlabel('Frequency (Hz)')
		plt.ylabel('Intensity')
		plt.title(title)
		plt.savefig(DIRECTORY + filename + ".png")

	
	return dft_freq[1:], dft[1:]


# Given an FFT plot and a frequency range, returns the
# average intensity of all signals within the frequency range.
def get_frequency_mean(fft_freqs, fft_data, min_freq, max_freq):
	
	min_index = np.where(fft_freqs==min_freq)[0][0]
	max_index = np.where(fft_freqs==max_freq)[0][0]

	mean = np.mean(fft_data[min_index:max_index])
	return mean



def plot_fourier(subject, channel_name, state, start=0, stop=10000, smooth=0):

	channel = get_channel_index(channel_name)
	data = get_channel_data(subject, channel, state)

	name = "Subject-" + str(subject) + "-Channel-" +str(channel_name) + "; " + state
	fourier_transform(data[start:stop], SAMPLING_RATE, name, name, smooth=smooth, label=state)




def plot_barcharts(subjects, channels, states):
	plt.figure()
	for subject in subjects:
		for channel in channels:
			for state in states:
				create_bar_chart(subject, channel, alpha=False)
				plt.figure()
	plt.figure()


# ---------------------------------------------- BANDPASS ----------------------------------------------

def bandpass_filter(data, low_freq, high_freq, steepness = 3, sampling_rate=SAMPLING_RATE):

	sos = sig.butter(steepness, [low_freq * 2/sampling_rate, high_freq * 2/sampling_rate], btype = "bandpass", output = "sos")
	filt_data = sig.sosfilt(sos, data)

	return filt_data


# ---------------------------------------------- PIPELINE ----------------------------------------------


# Creates a 4-dimensional array
def pipeline(subjects, channels, states, waves, start=0, stop=10000, smooth=0):
	
	fft_arr = np.ndarray(shape=( len(subjects),len(channels), len(states), len(waves) ))
	bp_arr = np.ndarray(shape=( len(subjects),len(channels), len(states), len(waves) ))

	for i in range(len(subjects)):
		subject = subjects[i]

		for j in range(len(channels)):
			channel_name = channels[j]

			for k in range(len(states)):
				state = states[k]

				for m in range(len(waves)):
					wave = waves[m]
					print("\n")
					print("Analyzing... \nSubject: " + str(subject) + " \nChannel: " + channel_name + " \nState: " + state + " \nWave: " + wave)

					channel = get_channel_index(channel_name)
					raw_data = get_channel_data(subject, channel, state)

					if wave=='alpha':
						bandpass_data = bandpass_filter(raw_data, low_freq=ALPHA_MIN, high_freq=ALPHA_MAX)
					elif wave=='theta':
						bandpass_data = bandpass_filter(raw_data, low_freq=THETA_MIN, high_freq=THETA_MAX)

					#fft_data = fourier_transform(raw_data, SAMPLING_RATE, filename=str, title=str, smooth=smooth, label=state)

					if wave == 'alpha':
						fft_arr[i, j, k, m] = get_alpha_average(raw_data, start, stop)
						bp_arr[i, j, k, m] = get_alpha_average(bandpass_data, start, stop)

					elif wave == 'theta':
						fft_arr[i, j, k, m] = get_theta_average(raw_data, start, stop)
						bp_arr[i, j, k, m] = get_theta_average(bandpass_data, start, stop)
				

	return fft_arr, bp_arr



# Gets a specific data point from an array generated by the pipeline function.
def get_data_point(arr, subjects, channels, states, waves, subject, channel, state, wave):

	
	subject_index = np.where(subjects == subject)[0]
	channel_index = np.where(channels == channel)[0]
	state_index = np.where(states == state)[0]
	wave_index = np.where(waves == wave)[0]

	return arr[subject_index, channel_index, state_index, wave_index][0]




def main():

	size = 5000


	start = 0
	stop = 100000
	smooth = int((stop-start)
		/1000)

	subjects = np.array([32, 42, 43])
	channels = np.array(["Fz"])
	states = np.array(['memory', 'rest'])
	waves = np.array(['theta'])

	fft_arr, bp_arr = pipeline(subjects, channels, states, waves)


	for subject in subjects:
		print("\n")
		print("Subject ", str(subject), " Channel Fz, Theta wave")
		memory = get_data_point(fft_arr, subjects, channels, states, waves, subject, "Fz", 'memory', 'theta')
		rest = get_data_point(fft_arr, subjects, channels, states, waves, subject, "Fz", 'rest', 'theta')
		print("Memory (Raw): ", round(memory, 2), "; Rest (Raw): ", round(rest, 2))
		memory = get_data_point(bp_arr, subjects, channels, states, waves, subject, "Fz", 'memory', 'theta')
		rest = get_data_point(bp_arr, subjects, channels, states, waves, subject, "Fz", 'rest', 'theta')
		print("Memory (BP): ", round(memory, 2), "; Rest (BP): ", round(rest, 2))

	
	print("Hello World!")

if __name__ == "__main__":
    main()