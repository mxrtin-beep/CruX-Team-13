
'''
The data

240441 time points (rest)
64 electrodes

https://raphaelvallat.com/bandpower.html
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9206021/
https://openneuro.org/datasets/ds003838/versions/1.0.0

'''
import matplotlib.pyplot as plt
import numpy as np
#import muselsl
import os
from time import time, strftime, gmtime


import data_loader_pavlov as pavlov_dl
import data_loader_wang as wang_dl
import fourier
import constants as const
import spectral_power as sp
import data_processing as dp
import bp_filter as bp
import classify
import mne_processing as mnep
import stream


# ----------------------------------------- PLOTTING ----------------------------------------------


def save_plot(filename, arr, title = '', xlabel = '', ylabel = '', label = ''):
    #plt.switch_backend('Agg')
    plt.plot(arr, alpha=0.5, label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.savefig(const.CHART_DIRECTORY + filename + ".png")
 







def clear_file(filename):
	f = open(filename, "w")
	f.write('')
	f.close()


def classify_wang(data):
	
	base_times, base_data = wang_dl.get_channel_data(1, 'Fz', 'eyesopen', 1)

	base = sp.abs_band_power(base_data, const.WANG_SAMPLING_RATE, 'theta', const.WANG_SECONDS)

	return classify.general_classify(data, const.WANG_SAMPLING_RATE, cutoff=(const.CUTOFF*base), n_seconds=const.WANG_SECONDS)


def classify_pavlov(data):
	
	base_data = pavlov_dl.get_channel_data(42, 'Fz', 'rest')

	base = sp.abs_band_power(base_data, const.PAVLOV_SAMPLING_RATE, 'theta', const.PAVLOV_SECONDS)
	print("Base: ", base)

	return classify.general_classify(data, const.PAVLOV_SAMPLING_RATE, cutoff=(const.CUTOFF*base), n_seconds=const.PAVLOV_SECONDS)



def main():

	filename = 'sub-042_eeg_sub-042_task-rest_eeg.set'
	directory = 'assets/Pavlov/'

	rest_Fz = pavlov_dl.get_channel_data(42, 'Fz', 'rest')
	mem_Fz = pavlov_dl.get_channel_data(42, 'Fz', 'memory')

	filt_rest = bp.bandpass_filter(rest_Fz, 4.5, 50, 1000)
	filt_mem = bp.bandpass_filter(mem_Fz, 4.5, 50, 1000)

	sp.plot_spectral_power(filt_rest, 'img', 1000, label = 'Fz, Rest', show_theta=True, new_fig=False, max_freq=20)
	sp.plot_spectral_power(filt_mem, 'img2', 1000, label = 'Fz, Memory', show_theta=True, new_fig=False, max_freq=20)
	#plt.savefig

	'''
	tasks = np.array(['eyesopen', 'eyesclosed', 'memory', 'mathematic', 'music'])

	for i in range(len(tasks)):
		task = tasks[i]

		times, data = wang_dl.get_channel_data(1, 'AF7', task, 1)
		if i == 0:
			sp.plot_spectral_power(data, 'Wang Paper Results', const.WANG_SAMPLING_RATE, 2, 20, label=task, new_fig=True, show_theta=True, show_alpha=True)
		else:
			sp.plot_spectral_power(data, 'Wang Paper Results', const.WANG_SAMPLING_RATE, 2, 20, label=task, new_fig=False, show_theta=False, show_alpha=False)

		classify_wang(data)


	tasks = np.array(['rest', 'memory'])

	for i in range(len(tasks)):
		task = tasks[i]

		data = pavlov_dl.get_channel_data(43, 'AF7', task)
		if i == 0:
			sp.plot_spectral_power(data, 'Pavlov Paper Results', const.PAVLOV_SAMPLING_RATE, 2, 20, label=task, new_fig=True, show_theta=True, show_alpha=True)
		else:
			sp.plot_spectral_power(data, 'Pavlov Paper Results', const.PAVLOV_SAMPLING_RATE, 2, 20, label=task, new_fig=False, show_theta=False, show_alpha=False)

		classify_pavlov(data)
	'''
	
	'''
	filename = 'sub-01_ses-session1_eeg_sub-01_ses-session1_task-eyesclosed_eeg.vhdr'
	directory = 'assets/Wang/'

	raw = mnep.load_raw_data(filename, directory)
	clean = mnep.get_clean_data(raw, 1.0, 30.0, 0)
	print(clean)
	print(clean.ch_names)
	print(clean.info)
	print(clean.times)

	# numpy array of shape (n_epochs, n_channels, n_times)
	print(clean.get_data(picks=['AF7']))
	'''
	
	
	#raw1 = stream.get_muse_stream_data(2)
	#raw2 = stream.get_muse_stream_data(2)

	

	#filename = 'example_data.csv'
	#directory = 'assets/'

	#print(mnep.load_csv_data(filename, directory))

if __name__ == "__main__":
    main()





    