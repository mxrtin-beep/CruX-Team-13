

import matplotlib.pyplot as plt
from scipy.integrate import simps
import constants as const
import numpy as np
from scipy import signal

LOWEST_FREQ = 1
MIN_CYCLES = 2
WINDOW_LENGTH = MIN_CYCLES / LOWEST_FREQ

# ----------------------------------------- SPECTRAL POWER ----------------------------------------------


# Fourier transform changes data from time to frequency domain.
# Spectral power calculates power or strength of frequency content.
# Magnitude normalized to a single hertz bandwidth.

def spectral_power(data, sampling_rate, window_length = WINDOW_LENGTH):

	win = window_length * sampling_rate # window length: 2 seconds
	freqs, psd = signal.welch(data, sampling_rate, nperseg=win)

	return freqs, psd


def plot_spectral_power(data, filename, sampling_rate, min_freq = 0, max_freq = 60, label='', new_fig = True, show_theta = False, show_alpha = False):

	if new_fig:
		plt.figure()

	freqs, psd = spectral_power(data, sampling_rate)


	if show_theta:
		plt.vlines(x = [const.THETA_MIN, const.THETA_MAX], ymin = 0, ymax = np.max(psd[min_freq+2:max_freq])*1.5,
           colors = 'purple',
           label = 'Theta Range')
	if show_alpha:
 		plt.vlines(x = [const.ALPHA_MIN, const.ALPHA_MAX], ymin = 0, ymax = np.max(psd[min_freq+2:max_freq])*1.5,
           colors = 'red',
           label = 'Alpha Range')

	plt.plot(freqs, psd, label=label)
	plt.xlim(min_freq, max_freq)
	plt.ylim(0, np.max(psd[min_freq+2:max_freq])*1.5)
	plt.xlabel('Frequency (Hz)')
	plt.ylabel('Power spectral density (V^2 / Hz)')
	plt.title("Welch's periodogram")


	

	name = const.CHART_DIRECTORY + filename + '.png'
	plt.legend()
	plt.savefig(name)

	


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

