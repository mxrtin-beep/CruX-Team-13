
import mne
import constants as const
import pandas as pd
import numpy as np


# Returns Raw Data Type
def load_csv_data(filename, directory, montage='standard_1020' ):
	df = pd.read_csv(directory+filename, sep=',', index_col=None) 
	data = df.transpose().to_numpy(dtype= np.float64)

	ch_names = ['timestamps','TP9','AF7','AF8','TP10','Right AUX']
	ch_types = ['misc', 'eeg', 'eeg', 'eeg', 'eeg', 'misc']

	fs = 256

	info = mne.create_info(ch_names= ch_names, ch_types= ch_types, sfreq= fs)
	raw = mne.io.RawArray(data, info)

	if montage != '':
		ten_twenty_montage = mne.channels.make_standard_montage(montage)
		raw.set_montage(ten_twenty_montage)

	return raw


def load_raw_data(filename, directory, montage='standard_1020'):
	raw = mne.io.read_raw_brainvision(directory + filename, preload=True)
	ten_twenty_montage = mne.channels.make_standard_montage(montage)
	raw.set_montage(ten_twenty_montage)

	return raw

def filter_data(raw, low_freq, high_freq):
	return raw.copy().filter(low_freq, high_freq)


# duration in seconds
def get_epochs(raw, duration = 1.0):

	events = mne.make_fixed_length_events(raw, duration=duration)
	epochs = mne.Epochs(raw, events,
	                        tmin=0.0, tmax=duration,
	                        baseline=None,
	                        preload=True)

	return epochs


# Takes Raw object, returns Epochs
def get_clean_data(raw, low_freq, high_freq, epoch_duration, plot=True, save_ica=False):
	
	#raw = load_data(filename, directory)
	raw_ica = filter_data(raw, low_freq, high_freq)
	epochs_ica = get_epochs(raw_ica, epoch_duration)

	reject = 0.000108
	random_state = 42   # ensures ICA is reproducable each time it's run
	ica_n_components = .99     # Specify n_components as a decimal to set % explained variance

	ica = mne.preprocessing.ICA(n_components=ica_n_components,
	                            random_state=random_state,
	                            )
	ica.fit(epochs_ica,
	        reject=reject,
	        tstep=epoch_duration)


	ica_z_thresh = 1.96 
	eog_indices, eog_scores = ica.find_bads_eog(raw_ica, 
	                                            ch_name=['Fp1', 'F8'], 
	                                            threshold=ica_z_thresh)
	ica.exclude = eog_indices


	if save_ica:
		p_id = 'test_ica'
		ica.save(directory + '/' + p_id + '-ica.fif', overwrite=True)

	epochs_postica = ica.apply(epochs_ica.copy())

	if plot:
	
		pre = epochs_ica.average().plot_psd(fmax = 25, picks=['AF7'], spatial_colors=True)
		post = epochs_postica.average().plot_psd(fmax = 25, picks=['AF7'], spatial_colors=True)


		pre.savefig(const.CHART_DIRECTORY + 'pre.png')
		post.savefig(const.CHART_DIRECTORY + 'post.png')


	return epochs_postica





