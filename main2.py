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



def pipeline(text, filename, task, i):

	fz = text[' EXG Channel 7'][fs*2:]	# Adelyne: 5; Amanda: 7
	min_freq = 3
	max_freq = 15
	#fz_power = sp.relative_band_power(fz, fs, 'theta')
	sp.plot_spectral_power(fz, 'fz'+filename, fs, label=task + '_' + str(i), min_freq=min_freq, max_freq=max_freq, new_fig=False, show_theta=False, show_alpha=False)


def main():

	subject = 'amanda'
	amanda_tasks = {
		'eyesclosed':3, 'eyesopen':3, 
		#'sequencememory':2, 'chimp':1, 'numbermemory':2, 'verbalmemory':3
	}
	adelyne_tasks = {'eyesclosed':2, 'eyesopen':1,'chimp':1, 'mentalmath':3, 'numbermemory':2, 'verbalmemory':1,
		#'alphabetbackwards':1, 'alphabetskipone':1, 'capitals':1
	}

	directory = 'session1'
	tasks = amanda_tasks

	for task in tasks.keys():
		for i in range(1, tasks[task] + 1):
			filename = directory + '/' + subject + '/' + subject + '_' + task + '_' + str(i) + '.txt'
			text = pd.read_csv(filename, skiprows=4)
			power = pipeline(text, subject + '_' + task + '_' + str(i), task, i)
			

	#fig, ax = plt.subplots()
	#plt.xticks(rotation=30)
	plt.xticks(rotation=30, ha='right')
	plt.title(subject + ' Spectral Powers')
	plt.subplots_adjust(bottom=0.25)
	plt.xlim(3, 8)
	plt.ylim(0, 3e6)
	plt.vlines(x = [const.THETA_MIN, const.THETA_MAX], ymin = 0, ymax = 7e6,
           colors = 'purple',
           label = 'Theta Range')
	plt.savefig('charts/amanda4.png')


if __name__ == "__main__":
    main()
