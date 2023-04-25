
#import muselsl
import os
from time import time, strftime, gmtime

import mne_processing as mnep

def get_muse_stream_data(n_seconds):

	data_source='EEG'
	filename = os.path.join(os.getcwd(), "%s_recording_%s.csv" %
                                (data_source,
                                 strftime('%Y-%m-%d-%H.%M.%S', gmtime())))

	muselsl.record(n_seconds)

	directory = ''
	print(mnep.load_csv_data(filename, directory))


def start_stream():
	muses = muselsl.list_muses()
	muselsl.stream(muses[0]['address'])