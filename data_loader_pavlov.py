import h5py
import pandas as pd

DIRECTORY = 'assets/Pavlov/'

# ---------------------------------------------- DATA ----------------------------------------------



# file: filename
# Returns object of type Database
def load_data(file):
	print("Loading data..." + str(file))
	return h5py.File(file)






# Given an object of type Database and a timestamp,
# returns a numpy array of all channel values at that time.
def get_one_timestamp(database, timestamp):
	return database['data'][timestamp]

# Given an object of type Database and a channel number,
# returns a numpy array of the entire recording of that channel.
def get_one_channel(database, channel):
	#print("Acquiring channel " + str(get_channel_name(channel)) + " from database " + str(database))
	return database['data'][:, channel]







# Given a channel number, gives you the name (Fz, Pz, etc.)
def get_channel_name(channel_index):

	data=pd.read_csv(DIRECTORY + 'channels.tsv',sep='\t')

	return data['name'].iloc[channel_index]


# Given a channel name (Fz, Pz), returns the channel index (0, 1, 2, etc)
def get_channel_index(channel_name):

	data=pd.read_csv(DIRECTORY + 'channels.tsv',sep='\t')

	return data[data['name'] == channel_name].index.item()






# Returns the data for one channel given a subject (int) and channel name.
# Task is "memory" or "rest"
def get_channel_data(subject, channel_name, task):

	channel = get_channel_index(channel_name)
	filename = get_filename(subject, task)
	data = load_data(filename)
	return get_one_channel(data, channel)


# Given a subject (number) and task (memory or rest), returns the name of the file for that.
def get_filename(subject, task):
	filename = DIRECTORY + "sub-0" + str(subject) + "_eeg_sub-0" + str(subject) + "_task-" + task + "_eeg.set"
	return filename
