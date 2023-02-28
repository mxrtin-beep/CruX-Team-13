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

## Approach

### 1. Binary Classification

<b>Detailed Approach</b>

<b>Considerations and Alternatives</b>

### 2. Regression

<b>Detailed Approach</b>
* We will use Welch’s method with a window of two seconds to create a periodogram.
* Given clean data, we will analyze the absolute spectral power and focus on the theta waves, from 4 Hz to 7 Hz.
* We will store the average absolute theta wave power of a resting patient as a baseline.
* We will compare the average theta wave power from 4 Hz to 7 Hz to the baseline to gauge the degree of cognitive load. It will be judged as cognitive load if the average power is at least 20% greater than the baseline.
  * The Pavlov 2020 paper found a difference in as much as 40% between the memory task and retention task theta powers.4
  * The retention task achieved roughly 20% greater power than the baseline in the Pavlov 2020 paper.
* We will measure at the Fz electrode (frontal midline).


<b>Considerations and Alternatives</b>
* It is possible that different patients will have a different baseline spectral power to compare to. If we find that that is the case, we will incorporate a calibration period for each patient.
* It is possible that whether the patient’s eyes are closed or open complicates the theta power. The Pavlov 2022 paper utilized eyes-closed resting and observed no spike in theta power.3 However, the Wang paper tested both eyes-closed and eyes-open resting and observed a theta power spike in the eyes-closed trials.5 The paper found a spike in theta power for memory tasks relative to the eyes-open trials only. We will measure both eyes-open and eyes-closed to confirm the correct baseline.


### 3. Graphical User Interface

<b>Detailed Approach</b>

Participant (30 UCLA student volunteers → recruitment through request)
* 7-9 hours of sleep
* No alcohol or caffeine that day
* Age 18-21
* Native english speakers
* No history of neurological or mental diseases 
* No psychiatric drugs 3 months prior to recording 
* No history of head trauma 

Set up: A computer screen, dark room, and a comfortable chair. 

Experiment: Mimicking shopping online

Goal: Purchase 2 items (each item is numbered)

Clean website (control): 

Speed: 1.5 seconds
Color: White with black text 
Clutter: Cleaner version: (actions split into different sections)
1. Home page begins with a start button 
2. The user has the choice to choose from 5 rectangles (each are labeled with an item) 
3. If the user clicks on an item, they can click on the button “Add to Cart” to add the item to cart
4. After the user adds all their items to the cart and the lower corner will be a “buy” button
5. After they select buy it will bring them to another page that shows an order confirmation 

Make all 30 participants do all 3 trials (randomized order):
1. Alter loading speed of page when a change to the cart is made (Ideal loading time: 1-2 seconds)
  1. Slow speed (4 seconds) vs. Regular speed (1- 2 seconds) vs. Fast (<1 second) 
2. Inverted colors vs regular colors (Dark mode vs light mode)
  1. Dark text on white page
  2. White text on dark page
  3. Colors vs black and white
3. Alter amount of “clutter” (overstimulation with more buttons on a page) 
  1. Clutter (all buttons on the same page) vs. Cleaner (actions split into sections)

After each trial: questionnaire of self-reported user experience (ex. How easy was it to purchase the items)  

Build a mimic of the website with PsychoPy. 


<b>Considerations and Alternatives</b>
* May need to build the website with a different platform 
* Is it possible to randomize volunteers? 
* Alternative for Test #1 (loading speed) 
  * Have the users memorize the items they need to buy, then have them wait a duration, and ask them to purchase them (test retention) 
* Alternative for Test #2 (Inverted colors B/W)
  * If the inverse of colors does not invoke a measurable change in cognitive load, we could change the colors (complimentary colors vs. opposite colors) 
* Alternative for Test #3 (Clutter) 
  * We could add more items to purchase (more options → more buttons → more clutter)



### 4. Data Collection and Processing

<b>Detailed Approach</b>

<b>Considerations and Alternatives</b>

### 5. Real-Time Analysis

<b>Detailed Approach</b>

* Real-time analysis is important to efficiently pinpoint the causes of cognitive load by allowing researchers to classify cognitive load as it is occurring.
* In order to perform real-time analysis, the live EEG data will be segmented into chunks of 100-millisecond length and fed to the classification pipeline.
* The spectral power will be calculated using the method described in section 5 on that chunk.
* There will be a live spectral power graph maintained with the average of the last 1-second segment of data.
* The live spectral power graph will be used to classify the presence of cognitive load in the subject using the classification method in section 5.
* This approach should provide a second-by-second method of classification. Given that the experimental design in section 3 involves tests lasting more than one second, this method should be sufficient to match the cognitive load recorded with the task performed by the subject.


<b>Considerations and Alternatives</b>
* It is possible that the program may not be able to calculate the periodogram and classify the cognitive load every 0.1 seconds. In that case, the chunk length may be increased to at most one second and the rolling average spectral power may be increased to 5 seconds.
* It is possible that a rolling average spectral power that covers 1-5 seconds may average over the spike in theta power. In that case, a rolling max theta power may be used instead of the average.


### Winter Week-by-Week Timeline


1. Meet team
2. Meet team, set up meeting time, choose topic, begin literature review
3. More literature review, refine topic, finish concept map, begin setting up Python environment
4. Set up Python environment, finish project proposal, Begin attempting to replicate successful paper in topic
5. Begin independently exploring papers in Python
6. Continue exploring papers in Python, develop or choose memory tasks
7. Collect data
8. Collect data, analyze collected data
9. Collect data, analyze collected data
10. Collect data, analyze collected data


## References

Experience, World Leaders in Research-Based User. n.d. “Minimize Cognitive Load to Maximize Usability.” Nielsen Norman Group. Accessed February 21, 2023. https://www.nngroup.com/articles/minimize-cognitive-load/.
“Mobile Site Abandonment After Delayed Load Time.” n.d. Think with Google. Accessed February 21, 2023. https://www.thinkwithgoogle.com/consumer-insights/consumer-trends/mobile-site-load-time-statistics/.
Pavlov, Yuri G., Dauren Kasanov, Alexandra I. Kosachenko, Alexander I. Kotyusov, and Niko A. Busch. 2022. “Pupillometry and Electroencephalography in the Digit Span Task.” Scientific Data 9 (June): 325. https://doi.org/10.1038/s41597-022-01414-2.
Pavlov, Yuri G., and Boris Kotchoubey. 2020. “The Electrophysiological Underpinnings of Variation in Verbal Working Memory Capacity.” Scientific Reports 10. https://doi.org/10.1038/s41598-020-72940-5.
Wang, Yulin, Wei Duan, Debo Dong, Lihong Ding, and Xu Lei. 2022. “A Test-Retest Resting, and Cognitive State EEG Dataset during Multiple Subject-Driven States.” Scientific Data 9 (September): 566. https://doi.org/10.1038/s41597-022-01607-9.


### Guides

Getting Started: https://seen-operation-ac3.notion.site/Getting-Started-d62f6d181a9e4f5c9088045be5a7d4e7

Data Analysis: https://seen-operation-ac3.notion.site/Data-Analysis-0da1d64523814c13a1f45dc90edac1d8

Using Muse: https://seen-operation-ac3.notion.site/Using-Muse-Data-5a8e2658e0ce4a7a86da7b758e15c44c

Introduction to MNE: https://www.notion.so/Using-MNE-to-Analyze-CSV-Files-930cccee777149e285db625f75f1ef9c?pvs=4

Using MNE to Remove Artifacts: https://www.notion.so/Using-MNE-To-Remove-Artifacts-758cee13fd0d4ac0a3d2b4bc8885104c?pvs=4
