
import mne
import constants as const
import matplotlib.pyplot as plt

DIRECTORY = "assets/Wang/"

# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9470564/



# subject: 1
# session: 1
# state: 'memory'
# channel: 'Fz'
# returns times and data as numpy arrays
def get_channel_data(subject, channel, state, session=1):
	file = get_filename(subject, session, state)

	print("Loading data..." + str(file))


	raw_data = mne.io.read_raw_brainvision(file, verbose=False)

	#print(raw_data.info)
	#print(raw_data.get_data(picks = [channel])[0])
	data, times = raw_data[channel, :]  

	return times, data[0]



def get_filename(subject, session, task):

	sub = "sub-0" + str(subject)
	ses = "ses-session" + str(session)
	tas = "task-" + task

	return DIRECTORY + sub + "_" + ses + "_eeg_" + sub + "_" + ses + "_" + tas + "_eeg" + ".vhdr"

