
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

import data_loader_pavlov as pavlov_dl
import data_loader_wang as wang_dl
import fourier
import constants as const
import spectral_power as sp
import data_processing as dp
import bp_filter as bp
import classify


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


	tasks = np.array(['eyesopen', 'eyesclosed', 'memory', 'mathematic', 'music'])

	for i in range(len(tasks)):
		task = tasks[i]

		times, data = wang_dl.get_channel_data(1, 'Fz', task, 1)
		if i == 0:
			sp.plot_spectral_power(data, 'Wang Paper Results', const.WANG_SAMPLING_RATE, 2, 20, label=task, new_fig=True, show_theta=True, show_alpha=True)
		else:
			sp.plot_spectral_power(data, 'Wang Paper Results', const.WANG_SAMPLING_RATE, 2, 20, label=task, new_fig=False, show_theta=False, show_alpha=False)

		classify_wang(data)


	tasks = np.array(['rest', 'memory'])

	for i in range(len(tasks)):
		task = tasks[i]

		data = pavlov_dl.get_channel_data(43, 'Fz', task)
		if i == 0:
			sp.plot_spectral_power(data, 'Pavlov Paper Results', const.PAVLOV_SAMPLING_RATE, 2, 20, label=task, new_fig=True, show_theta=True, show_alpha=True)
		else:
			sp.plot_spectral_power(data, 'Pavlov Paper Results', const.PAVLOV_SAMPLING_RATE, 2, 20, label=task, new_fig=False, show_theta=False, show_alpha=False)

		classify_pavlov(data)


	#times, data = wang.get_channel_data(1, 'Fz', 'memory', 1)
	#classify_wang(data)
	#sp.plot_spectral_power(data, "wang-memory", const.WANG_SAMPLING_RATE, 2, 20,label='memory', new_fig=False, show_theta=True, show_alpha=True)


	
	#data = dl.get_channel_data(42, 'Fz', 'rest')
	#classify_pavlov(data)

	#data = dl.get_channel_data(42, 'Fz', 'memory')
	#classify_pavlov(data)


if __name__ == "__main__":
    main()





    