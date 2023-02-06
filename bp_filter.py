

import scipy.signal as sig

import constants as const




# ---------------------------------------------- BANDPASS ----------------------------------------------

# Takes raw data, not FFT.
def bandpass_filter(data, low_freq, high_freq, sampling_rate, steepness = 3):

	sos = sig.butter(steepness, [low_freq * 2/sampling_rate, high_freq * 2/sampling_rate], btype = "bandpass", output = "sos")
	filt_data = sig.sosfilt(sos, data)

	return filt_data