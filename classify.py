

import constants as const
import spectral_power as sp
import data_processing as dp
import bp_filter as bp

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps


# raw_data: numpy array
# n_seconds: number of seconds to chunk
# fs: sampling rate
# wave: 'alpha' or 'theta'
# metric: 'absolute spectral' or 'relative spectral'
# cutoff: cutoff metric above which is classified as cognitive load
# filename: filename for plots
# verbose: set to True to print every chunk
def classify_cognitive_load(raw_data, n_seconds, fs, wave, metric, cutoff, filename = '', verbose = False):

	size = n_seconds * fs

	part_data = dp.partition_array(raw_data, size)

	average = 0
	max_power = 0

	powers = np.empty(len(part_data))


	if wave == 'theta':
		w_min = const.THETA_MIN
		w_max = const.THETA_MAX

	elif wave == 'alpha':
		w_min = const.ALPHA_MIN
		w_max = const.ALPHA_MAX

	for i in range(len(part_data)):

		partition = part_data[i]

		filt_data = bp.bandpass_filter(partition, w_min, w_max, fs)
		power = sp.relative_band_power(filt_data, fs, wave)

		if verbose:
			print("Partition\t", i, "\tMax Power\t", round(max_power, 2))
		average += power

		if power > max_power:
			max_power = power

		powers[i] = power

	average = round(average / len(part_data), 3)
	max_power = round(max_power, 3)

	print(wave, ": Average relative power\t", average)
	print(wave, ": Max relative power\t", max_power)


	if filename != '':
		plt.plot(powers[1: -1])
		plt.title("Spectral Powers")
		plt.ylabel("Power (V/m^2)")
		plt.xlabel("Time (s)")
		plt.savefig(const.CHART_DIRECTORY + filename + ".png")


	if max_power > cutoff:
		print("Classified as COGNITIVE LOAD")
		return True

	print("Classified as REST")
	return False

	


def classify_pavlov(raw_data, cutoff, filename, verbose, n_seconds = 2):

	return classify_cognitive_load(raw_data, n_seconds, const.PAVLOV_SAMPLING_RATE, wave='theta', metric='relative spectral', cutoff=cutoff, filename=filename, verbose=verbose)



def classify_wang(raw_data, cutoff, filename='',  n_seconds = 4, label=''):

	#times, data = wang.get_channel_data(1, 'Fz', 'memory', 1)

	freqs, psd = sp.spectral_power(raw_data, const.WANG_SAMPLING_RATE, n_seconds)

	alpha_range = np.logical_and(freqs >= const.ALPHA_MIN, freqs <= const.ALPHA_MAX)

	freq_res = freqs[1] - freqs[0]

	abs_power = simps(psd[alpha_range], dx=freq_res)

	print(abs_power)

	if filename != '':
		plt.plot(freqs[3:160], psd[3:160], label=label)
		plt.ylim(0, 40)
		plt.xlim(0, 20)
		plt.legend()
		plt.savefig(const.CHART_DIRECTORY + filename + '.png')

	if abs_power >= cutoff:
		print("Classified as COGNITIVE LOAD")
		return True

	print("Classified as REST")
	return False


def general_classify(raw_data, sampling_rate, cutoff = 0, n_seconds=3):

	freqs, psd = sp.spectral_power(raw_data, sampling_rate, n_seconds)

	theta_range = np.logical_and(freqs >= const.THETA_MIN, freqs <= const.THETA_MAX)

	freq_res = freqs[1] - freqs[0]

	abs_power = simps(psd[theta_range], dx=freq_res)

	print("Absolute Power: " + abs_power)
	#cutoff = 0.5*(10**(-12))
	if abs_power >= cutoff:
		print("Classified as COGNITIVE LOAD")
		return True

	print("Classified as REST")
	return False


