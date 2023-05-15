
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
import pandas as pd


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

fs = 250

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


def pipeline(text, filename):
	pz = text[' EXG Channel 1'][fs*2:]
	cz = text[' EXG Channel 4'][fs*2:]
	fz = text[' EXG Channel 5'][fs*2:]	# Adelyne: 5; Amanda: 7
	min_freq = 3
	max_freq = 15
	
	#sp.plot_spectral_power(pz, 'pz'+filename, fs, label='pz', min_freq=min_freq, max_freq=max_freq, new_fig=True, show_theta=True, show_alpha=True)
	#sp.plot_spectral_power(cz, 'cz'+filename, fs, label='cz', min_freq=min_freq, max_freq=max_freq, new_fig=False, show_theta=True, show_alpha=True)
	#sp.plot_spectral_power(fz, 'fz'+filename, fs, label='fz', min_freq=min_freq, max_freq=max_freq, new_fig=False, show_theta=True, show_alpha=True)

	pz_power = sp.relative_band_power(pz, fs, 'theta')
	cz_power = sp.relative_band_power(cz, fs, 'theta')
	fz_power = sp.relative_band_power(fz, fs, 'theta')

	print(f'Task: {filename}\t Fz Power: {round(fz_power*100, 2)}')

	return fz_power*100

def main():

	subject = 'adelyne'
	amanda_tasks = {'eyesclosed':3, 'eyesopen':3, 'sequencememory':2, 'chimp':1, 'numbermemory':2, 'verbalmemory':3}
	adelyne_tasks = {'eyesclosed':2, 'eyesopen':1,
	'alphabetbackwards':1, 'alphabetskipone':1, 'capitals':1, 'chimp':1, 'mentalmath':3, 'numbermemory':2, 'verbalmemory':1}

	directory = 'session1'
	tasks = adelyne_tasks

	for task in tasks.keys():
		for i in range(1, tasks[task] + 1):
			filename = directory + '/' + subject + '/' + subject + '_' + task + '_' + str(i) + '.txt'
			text = pd.read_csv(filename, skiprows=4)
			power = pipeline(text, subject + '_' + task + '_' + str(i))
			plt.bar(task + '_' + str(i), round(power, 3), color='green')

	#fig, ax = plt.subplots()
	#plt.xticks(rotation=30)
	plt.xticks(rotation=30, ha='right')
	plt.title(subject + ' Relative Theta Power Times 100, Fz Electrode')
	plt.subplots_adjust(bottom=0.25)
	plt.savefig('charts/bar1.png')


if __name__ == "__main__":
    main()





    