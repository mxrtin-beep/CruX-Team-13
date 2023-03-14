<h1 align="center">
ThetaFlow Project Proposal
</h1>

<p align="center">
Measuring cognitive load with BCI.
</p>

<p align="center">
Martin Bourdev, Daniel Bielin, Kyra Sunil, Amanda Dankberg, Akshyae Singh, Alex Rayo, Adelyne Tran, Kylie Bach
</p>

## Narrative
Intuitive and easy user experience is the cornerstone of any product or service.[<sup>1</sup>](https://www.nngroup.com/articles/minimize-cognitive-load/) When design fails, users must tap into their limited processing power and take on cognitive load, leading to disorganization, discouragement, and poor user experience. We aim to use EEG signals to objectively measure and quantify the cognitive load experienced by a user to test and improve the usability of products and services.

## Overall Aim
We will build a program to use EEG data to measure cognitive load in real time to aid in product design.

## Specific Aims
1. Develop a method to classify cleaned literature data as the product of cognitive load or rest in a binary way.
2. Develop a method to quantify degrees of cognitive load from cleaned literature data.
3. Build a graphical user interface that can incite cognitive load in test subjects.
4. Record our own data and develop a method to remove artifacts such as blinks and facial movements from raw EEG data such that it matches the literature data.
5. Perform steps 1 and 2 with live data. Evaluate the system by performing live tests of rest and memory tasks of varying degrees of difficulty. 

## Significance

* Good product design demands as little cognitive effort from the user as possible.
* Poor design characteristics, such as long load times, clutter, unintuitive functionality, hidden information, poor feedback, and clashing colors can cause cognitive strain and turn users away from products.
* Data study from 2016 shows that over half of visits to a mobile site are abandoned if the loading time is greater than three seconds, a 32% increase in abandonment from a one-second load time.2 As load time increases to six seconds, the chance of abandonment doubles, a 200% increase in abandonment from a one-second load time.2
* ThetaFlow will allow companies to objectively measure cognitive load suffered by users and improve design.

## Approach

### 1. Binary Classification

<b>Detailed Approach</b>

* We will attempt binary classification on the Pavlov 2022 dataset.3 
 * The data is cleaned and filtered.
 * The dataset includes 77 patients with EEG data. The researchers used Fpz as the ground and FCz as the reference and sampled at 1000 Hz.
 * Each patient includes a rest and memory .set file, requiring the python h5py package to open. Each session includes detailed labels for the event occurring at any time. 
* We will also attempt binary classification on the Wang 2022 dataset.7
 * The data is cleaned and filtered. The team used FCz as the reference electrode and sampled at 500 Hz.
 * The dataset includes 60 patients with EEG data. Each patient has 3 sessions.
 * Each session includes .eeg, .vhdr, and .vmrk files for tasks, requiring the python MNE package to open. The session includes resting with eyes closed and open, as well as math, memory, and music tasks.
 * The Wang dataset does not include detailed labels for each moment of time.
* We will use Welch’s method with a window of four seconds to create a periodogram.
* Given clean data, we will analyze the absolute spectral power and focus on the theta waves, from 4 Hz to 7 Hz.
* We will store the average absolute and relative theta wave power of a resting patient as a baseline.
* We will compare the average theta wave power from 4 Hz to 7 Hz to the baseline to gauge whether or not cognitive load is present. It will be judged as cognitive load if the average power is at least 15% greater than the baseline.
 * The retention task achieved roughly 20% greater power than the baseline in the Pavlov 2020 paper, which used relative power.
 * The baseline will be measured by having subjects stare at a fixation point on the screen for 30 seconds with their eyes open.
* We will measure at the Fz electrode (frontal midline).


<b>Considerations and Alternatives</b>

* It is possible that comparing each patient’s readings to their own baseline does not provide useful information or is not feasible. In that case, we will compare readings to a baseline level composed of the average of several patients.
* It is possible that whether the patient’s eyes are closed or open complicates the theta power. The Pavlov 2022 paper utilized eyes-closed resting and observed no spike in theta power.4 However, the Wang paper tested both eyes-closed and eyes-open resting and observed a theta power spike in the eyes-closed trials.6 The paper found a spike in theta power for memory tasks relative to the eyes-open trials only. We will measure both eyes-open and eyes-closed to confirm the correct baseline.

### 2. Regression

<b>Detailed Approach</b>

* The Pavlov dataset will be used.
 * The Pavlov dataset includes the same task of retention with different difficulty levels, which will make multi-class classification based on task difficulty possible. Each session includes labels of the specific task ongoing at each moment with the success or failure of the subject.
 * The Wang dataset is unfit for multi-class classification, because the tasks tested are not objectively comparable in difficulty.
* The multi-class classification approach is very similar to the binary classification approach.
* We will use Welch’s method with a window of four seconds to create a periodogram.
* Given clean data, we will analyze the absolute spectral power and focus on the theta waves, from 4 Hz to 7 Hz.
* We will store the average absolute theta wave power of a resting patient as a baseline.
* We will compare the average theta wave power from 4 Hz to 7 Hz to the baseline to gauge the degree of cognitive load. The degree of cognitive load will be separated into 4 classes based on the percent increase in theta wave power from baseline:
 1. 10%-20%
 2. 20%-30%
 3. 30%-40%
 4. >40%
* We will measure at the Fz electrode (frontal midline).



<b>Considerations and Alternatives</b>
* It is possible that different patients will have a different baseline spectral power to compare to. If we find that that is the case, we will incorporate a calibration period for each patient.
* It is possible that whether the patient’s eyes are closed or open complicates the theta power. The Pavlov 2022 paper utilized eyes-closed resting and observed no spike in theta power.4 However, the Wang paper tested both eyes-closed and eyes-open resting and observed a theta power spike in the eyes-closed trials.6 The paper found a spike in theta power for memory tasks relative to the eyes-open trials only. We will measure both eyes-open and eyes-closed to confirm the correct baseline.
* It is possible that the cognitive load, in addition to being a function of the patient, is a function of both the difficulty of the task as well as the effort exerted by the patient, self-reported after the trial. If that is true, then the same task may elicit very different levels of cognitive load from patients, and different tasks may elicit the same cognitive load from different patients. We will gauge from our own trials how and if measured theta wave power is a function of both task difficulty, task success, and reported difficulty.
* It is possible that multi-class classification may be unrealistic for the Wang dataset. It may be impossible to objectively rank completely different tasks in difficulty level and therefore expected cognitive load. The tasks with the highest and lowest theta wave power may differ depending on the person. 
 * This is unlike the Pavlov task, where each higher difficulty level is quantitatively more challenging. Everyone should struggle more on the longer memory task than the shorter one. In contrast, some people may struggle more with the music task in the Wang experiment, whereas some people may struggle more with the arithmetic task.


### 3. Graphical User Interface

<b>Detailed Approach</b>

Participant overview: 
(30 UCLA student volunteers → recruitment through request)
* 7-9 hours of sleep the previous day
* No alcohol or caffeine that day
* Age 18-21
* Native english speakers
* No history of neurological or mental diseases 
* No psychiatric drugs 3 months prior to recording 
* No history of head trauma 

Set up: A computer screen, dark room, and a comfortable chair. 
Experiment: Mimicking shopping online
Goal: Purchase 2 items from 5 totals items (each item is numbered)

Website overview:
1. Home page begins with a start button 
2. The user has the choice to choose from 5 rectangles (each are labeled with an item) 
3. If the user clicks on an item, they can click on the button “Add to Cart” to add the item to cart
4. After the user adds all their items to the cart and the lower corner will be a “buy” button
5. After they select buy it will bring them to another page that shows an order confirmation 

Hypothesis: Faster loading speed, white background with black text, and actions split into different sections will cause the least cognitive load.

Control website:
* Speed: 1.5 seconds
* Color: White with black text 
* Clutter: 
 * Fewer buttons on a single page 
 * Actions are split into different sections
 * Each page will have a “Next” button to load the following page
 
Figure 1. The control shopping simulation will be split up into four pages. The first page will have just a start button. The second page will have all of the items available for purchase and the participant can add items in their cart. The third page will list the items in the participant’s cart. The last page will be a confirmation page.

Detailed procedure:

1. All thirty participants are invited to sit in a comfortable chair in a dark room and stare at a blank white computer screen with a black fixation cross in the center for 30 seconds with their eyes open in order to collect baseline brain activity.
 a. Participants are recorded to capture the timing of blinks and to capture any divergences from the fixation cross.
2. Participants are numbered, and randomly put into 3 groups of 10 each. We number the groups Group 1, Group 2, and Group 3.
3. We instruct the participants to treat the website like an online shopping experience. We number the items 1-5 and randomly select two items for each participant to “buy”. We instruct the participants to purchase the two items by name. We then wait 30 seconds before allowing participants to start the simulation.
4. All participants go through the control shopping simulation.
 a. Fast loading speed.
 b. Light mode.
 c. No clutter.
5. After a 30 second break, participants will all complete a questionnaire about the control shopping simulation.
6. Participants are then given a 2 minute break.
7. Group 1 will go through the loading time experimental simulation. Each participant will perform the task with the medium and slow loading speed.
8. Group 2 will go through the dark mode experimental simulation. We repeat steps 3-6.
9. Group 3 will go through the clutter experimental simulation. We repeat steps 3, 5, and 6.

Experimental websites:
1. Alter loading speed of page when a change to the cart is made.
 a. Slow speed (4 seconds) vs. Regular speed (1-2 seconds) vs. Fast (<1 second) 
2. Inverted colors vs regular colors (Dark mode vs light mode).
 a. Dark text on white page
 b. White text on dark page
 c. Colors vs black and white
3. Alter amount of clutter (More buttons on a page causes overstimulation).
 a. Cluttered page (all buttons on the same page)
 b. Cleaner page (actions split into sections)
 
Questionnaire 
* Self-reported user experience 
* Goal: Do users detect conscious differences (ex. frustration, ease/difficulty)? 

Questions:
1. On a scale of 1-5, how easy was it to purchase the items?
2. What aspects do you like or dislike about the website?
3. What would you improve?
4. (After experimental simulation only) Which website did you prefer? Why?

Build a mimic of the website with PsychoPy. 


<b>Considerations and Alternatives</b>

* Thirty participants split into three groups may be too ambitious for one quarter.
 * If so, we will test five subjects.
 * We will only test the loading time variable.
 * Each participant will complete the baseline task, the control (fast), medium, and slow loading time tasks, and the questionnaire.
* We may need to build the website with a different platform 
* We must find a way to randomize volunteers 
* It is possible that we do not detect any cognitive load in any of the trials
* Alternative for Test #1 (loading speed) 
 * Have the users memorize the items they need to buy, then have them wait a duration, and ask them to purchase them (test retention) 
* Alternative for Test #2 (Inverted colors B/W)
 * If the inverse of colors does not invoke a measurable change in cognitive load, we could change the colors (complimentary colors vs. opposite colors) 
* Alternative for Test #3 (Clutter) 
 * We could add more items to purchase (more options → more buttons → more clutter)


### 4. Data Collection and Processing

<b>Detailed Approach</b>

* The cyton will be used to collect and amplify EEG data.
* The USB dongle communicates with the amplifier and makes data available to the relevant software.
* The OpenBCI GUI can be used to graphically interface with the connected BCI amplifier’s channels (in this case to show the signal corresponding with cognitive strain)
* General procedure: 
 * Connect the bluetooth dongle to the laptop and set the switch to GPIO_6.
 * Connect power source and desired electrodes to Cyton channels and toggle to PC.
  * Use FCz as the reference electrode.
  * Connect the ground electrode to the Fpz electrode (forehead).
  * Measure Fz electrode (frontal midline).
 * Launch the OpenBCI GUI.
 * Put on the OpenBCI cap with the strap on the chin to ensure tight connection between frontal electrodes and head.
 * Put gel on electrodes and monitor impedances.
 * Cyton Live → Serial (from Dongle) → Auto-Connect
* Impedance will be maintained below 25 kOm

The signal processing will begin with the removal of artifacts such as eye blinks, jaw clenches, eyebrow movements etc. This will be partially achieved by using a bandpass filter of data with large spikes that cannot be caused purely by EEG. A high-pass filter will be applied to the raw data to remove noise below 1 Hz. A lowpass filter will also be applied to remove frequencies above 40 Hz.

* One method is independent component analysis (ICA), which has been used extensively in the literature to identify and remove artifacts in EEG signals. ICA is a signal processing technique that separates a multivariate signal into independent, non-Gaussian components. In the case of EEG signals, ICA can be used to identify and remove artifacts. The procedure involves identifying the components that are clearly related to blinks and eye movements and then removing them after visual exploration of the data. To perform ICA, we will use the MNE algorithm, which is a commonly used tool in EEG signal processing. The code includes the "create_eog_epochs" function, which chooses an electrode near the forehead and applies an algorithm to find the epochs with artifacts.
* Finally, after removing artifacts using these techniques, the data will be visually inspected for any remaining artifacts. Epochs still containing artifacts will be visually identified and discarded. This ensured that the final data is as clean as possible and could be used for accurate analysis.


<b>Considerations and Alternatives</b>

* We may encounter railed electrodes in data collection.
 * Inject gel into electrode with syringe.
 * Make sure the ground electrode is attached well, since it removes noise.
 * Adjust the reference electrode.
* In addition to ICA analysis and bandpass filtering of EEG signals, there are other alternatives such as adaptive filtering, regression-based methods etc. that are used to remove artifacts.
* If the ICA method of removing artifacts is unsuccessful, MNE also provides a method to manually remove epochs that fail to meet certain criteria of maximum and minimum peak-to-peak amplitudes of the data. This will remove potentially useful signal, but it will also simply remove the epochs with artifacts instead of subtracting out artifacts and altering the data.
* Manual removal of artifacts is time consuming and might include error in the form of removal of useful epochs. It also limits the capability of real-time analysis.


### 5. Real-Time Analysis

<b>Detailed Approach</b>

* Real-time analysis is important to efficiently pinpoint the causes of cognitive load by allowing researchers to classify cognitive load as it is occurring.
* In order to perform real-time analysis, the live EEG data will be segmented into chunks of four seconds and fed to the classification pipeline.
* The spectral power will be calculated using the method described in section 1 on that chunk.
* There will be a live spectral power graph maintained with the average of the last four-second segment of data.
* The live spectral power graph will be used to classify the presence of cognitive load in the subject using the classification method in section 1.
* This approach should provide a method of classification every 4 seconds. Given that the experimental design in section 3 involves tests lasting a multiple of 4 seconds, this method should be sufficient to match the cognitive load recorded with the task performed by the subject.


<b>Considerations and Alternatives</b>
* It is possible that the program may not be able to calculate the periodogram and classify the cognitive load every four seconds. In that case, the chunk length may be increased.
* It is possible that a rolling average spectral power that covers 1-5 seconds may average over the spike in theta power. In that case, a rolling max theta power may be used instead of the average.


## Figures

<p align="center">
 <img width=50% src="https://user-images.githubusercontent.com/52719688/225146607-6a4d7f89-150d-4e71-84a6-49375d744c3e.png">
</p>

<p align="center"><i>Data Flow Flowchart</i></p>


<p align="center">
 <img width=50% src="https://user-images.githubusercontent.com/52719688/225146239-c6dfebff-53e9-48c0-bc15-8ca34b6ceae7.png">
</p>

<p align="center"><i>Data Processing Flowchart</i></p>


<p align="center">
 <img width=70% src="https://user-images.githubusercontent.com/52719688/225147950-3162b565-06f1-47d1-a005-e3955c13f630.png">
</p>

<p align="center"><i>GUI Flowchart</i></p>


<p align="center">
 <img width=50% src="https://user-images.githubusercontent.com/52719688/225145819-83e22562-3e17-4e51-bff2-6e50af99bf50.png">
</p>

<p align="center"><i>Expected Results</i></p>


## References

1. Experience, World Leaders in Research-Based User. n.d. “Minimize Cognitive Load to Maximize Usability.” Nielsen Norman Group. Accessed February 21, 2023. https://www.nngroup.com/articles/minimize-cognitive-load/.
2. “Mobile Site Abandonment After Delayed Load Time.” n.d. Think with Google. Accessed February 21, 2023. https://www.thinkwithgoogle.com/consumer-insights/consumer-trends/mobile-site-load-time-statistics/.
3. Pavlov, Yuri G., Dauren Kasanov, Alexandra I. Kosachenko, and Alexander I. Kotyusov. 2022. “EEG, Pupillometry, ECG and Photoplethysmography, and Behavioral Data in the Digit Span Task.” Openneuro. https://doi.org/10.18112/OPENNEURO.DS003838.V1.0.3.
4. Pavlov, Yuri G., Dauren Kasanov, Alexandra I. Kosachenko, Alexander I. Kotyusov, and Niko A. Busch. 2022. “Pupillometry and Electroencephalography in the Digit Span Task.” Scientific Data 9 (1): 325. https://doi.org/10.1038/s41597-022-01414-2.
5. Pavlov, Yuri G., and Boris Kotchoubey. 2020. “The Electrophysiological Underpinnings of Variation in Verbal Working Memory Capacity.” Scientific Reports 10. https://doi.org/10.1038/s41598-020-72940-5.
6. Wang, Yulin, Wei Duan, Debo Dong, Lihong Ding, and Xu Lei. 2022. “A Test-Retest Resting, and Cognitive State EEG Dataset during Multiple Subject-Driven States.” Scientific Data 9 (September): 566. https://doi.org/10.1038/s41597-022-01607-9.
7. Yulin Wang, Wei Duan, Lihong Ding, Debo Dong, and Xu Lei. 2022. “A Test-Retest Resting and Cognitive State EEG Dataset.” Openneuro. https://doi.org/10.18112/OPENNEURO.DS004148.V1.0.1.


### Guides

Getting Started: https://seen-operation-ac3.notion.site/Getting-Started-d62f6d181a9e4f5c9088045be5a7d4e7

Data Analysis: https://seen-operation-ac3.notion.site/Data-Analysis-0da1d64523814c13a1f45dc90edac1d8

Using Muse: https://seen-operation-ac3.notion.site/Using-Muse-Data-5a8e2658e0ce4a7a86da7b758e15c44c

Introduction to MNE: https://www.notion.so/Using-MNE-to-Analyze-CSV-Files-930cccee777149e285db625f75f1ef9c?pvs=4

Using MNE to Remove Artifacts: https://www.notion.so/Using-MNE-To-Remove-Artifacts-758cee13fd0d4ac0a3d2b4bc8885104c?pvs=4
