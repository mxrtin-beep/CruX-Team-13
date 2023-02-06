

import matplotlib.pyplot as plt
from scipy.integrate import simps
import constants as const
import numpy as np
from scipy import signal

LOWEST_FREQ = 1
MIN_CYCLES = 2
WINDOW_LENGTH = MIN_CYCLES / LOWEST_FREQ

# ----------------------------------------- SPECTRAL POWER ----------------------------------------------

def spectral_power(data, sampling_rate, window_length = WINDOW_LENGTH):

	win = window_length * sampling_rate # window length: 2 seconds
	freqs, psd = signal.welch(data, sampling_rate, nperseg=win)

	return freqs, psd


def plot_spectral_power(data, filename, sampling_rate, label='', newFig = True):

	if newFig:
		plt.figure()

	freqs, psd = spectral_power(data, sampling_rate)
	plt.plot(freqs, psd, label=label)
	plt.xlabel('Frequency (Hz)')
	plt.ylabel('Power spectral density (V^2 / Hz)')
	plt.title("Welch's periodogram")
	name = const.DIRECTORY + filename + '.png'
	plt.savefig(name)

	if newFig:
		plt.figure()


def abs_band_power(data, sampling_rate, wave, window_length=WINDOW_LENGTH):

	freqs, psd = spectral_power(data, sampling_rate, window_length=window_length)

	freq_res = freqs[1] - freqs[0]

	if wave == 'alpha':
		low = const.ALPHA_MIN
		high = const.ALPHA_MAX

	if wave == 'theta':
		low = const.THETA_MIN
		high = const.THETA_MAX

	idx = np.logical_and(freqs >= low, freqs <= high)

	abs_power = simps(psd[idx], dx=freq_res)

	return abs_power


def relative_band_power(data, sampling_rate, wave, window_length=WINDOW_LENGTH):

	freqs, psd = spectral_power(data, sampling_rate, window_length=window_length)

	freq_res = freqs[1] - freqs[0]

	if wave == 'alpha':
		low = const.ALPHA_MIN
		high = const.ALPHA_MAX

	if wave == 'theta':
		low = const.THETA_MIN
		high = const.THETA_MAX

	idx = np.logical_and(freqs >= low, freqs <= high)

	abs_power = simps(psd[idx], dx=freq_res)
	
	total_power = simps(psd, dx=freq_res)

	rel_power = abs_power / total_power

	return rel_power

