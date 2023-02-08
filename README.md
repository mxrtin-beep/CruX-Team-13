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

## Specific Aims
We propose a method to measure and quantify the cognitive load of a patient performing a working memory task.

Cognitive load is an intrinsic problem in the field of user experience (UX) design. The Nielsen Norman Group, a UX research organization, offers guidelines for web design with the aim of reducing cognitive load. Concepts such as avoiding visual clutter, following users’ mental models of websites, and offloading tasks that require user memory are all aimed at reducing cognitive load of customers. Even something as simple as webpage load time has a huge impact on usability; a Google Data study from 2016 shows that over half of visits to a mobile site are abandoned if the loading time is greater than three seconds, a 32% increase in abandonment from a one-second load time.[<sup>2</sup>](https://www.nngroup.com/articles/minimize-cognitive-load) As load time increases to six seconds, the chance of abandonment doubles. Users required to remember information for more time will cause more cognitive strain, increasing the chances of abandonment. A couple seconds can cost a company half of its users before they even see the website.

In 2022, Yuri G. Pavlov et. al. demonstrated that it is possible to qualitatively detect cognitive load from a digit span task using EEG data.[<sup>3</sup>](https://www.thinkwithgoogle.com/consumer-insights/consumer-trends/mobile-site-load-time-statistics/) The task involved patients memorizing sequences of 5, 9, or 13 digits. The team found an increase in theta wave power in EEG data from the memory task as opposed to the control. The increase occurred in the frontal midline area at the Fz electrode.

In 2020, Pavlov’s team considered both retention and manipulation of a string of letters.[<sup>4</sup>](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7527344/) They found that theta activity increases for both types of tasks, with a higher increase for the more difficult manipulation task. This supports the idea of measuring relative levels of cognitive strain, as opposed to the simple qualitative presence of cognitive strain.

Furthermore, Yulin Wang’s team in 2022 dove further into variations of the tests that Pavlov’s team conducted.[<sup>5</sup>](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9470564/) Pavlov’s team compared a closed-eyed rest with a digit span memory task in 2022. Wang’s team tested open- and closed-eyed resting periods, as well as three types of cognitive tasks: memory, music, and subtraction. The team was able to use theta wave power to distinguish between different states.

We aim to expand upon the research by Pavlov’s and Wang’s teams. for the purposes of UX design. Our technique will be able to detect cognitive load live, as opposed to post-experiment, in order to better identify the task and moment that incited the cognitive load. Our technique will also quantitatively measure cognitive load, as opposed to qualitatively detect it. Quantitative results will allow designers and researchers to compare different designs and A/B tests to find the one that elicits the least strain from the user. Finally, our experiment will expand the methods of testing cognitive strain. The Pavlov paper utilizes a digit span test of memorizing several digits every two seconds. We will incorporate other tests, such as memorizing several digits for certain amounts of time, simulating the wait for a web page to load. It may also be interesting to explore the similarities and differences between numerical, verbal, and visual memory tests.

Our experiment will allow user experience researchers to quantify cognitive load in real time. Designers will be able to adjust design choices to improve user flow, avoid frustration and abandonment, and improve customer satisfaction and retention.

### Specific Aims:
1. Develop a method to classify cleaned literature data as the product of cognitive load or rest in a binary way.
2. Develop a method to quantify degrees of cognitive load from cleaned literature data.
3. Record our own data and develop a method to remove artifacts such as blinks and facial movements from raw EEG data such that it matches the literature data.
4. Build a graphic interface that can incite cognitive load in test subjects.
5. Perform steps 1-3 with live data. Evaluate the system by performing live tests of rest and memory tasks of varying degrees of difficulty. 

<p align="center">
<img width="800" alt="image5" src="https://user-images.githubusercontent.com/52719688/217158775-09259d36-1e31-4ae8-90cb-ba6f4b3b3255.png">
</p>

<p align="center"> <i>
Our Project Workflow.
</p> </i>

## Research Strategy
### Data Acquisition

The Pavlov papers utilize frontal midline theta activity to discriminate between restful and memory EEG data, specifically electrode Fz. The Muse 2 headset includes electrodes AF7, AF8, and Fpz, so it may be possible to use the Muse 2 headset to acquire usable data from the Fpz electrode. If not, a headset with channel Fz must be used.
	The 2022 Pavlov paper measures patients during a digit span task. Patients listened to sequences of 5, 9, or 13 digits, each presented every two seconds, and were asked to recall them in order. The EEG data from that task represents the memory data, along with four minutes of rest as the control data.


<p align="center">
<img alt="image3" src="https://user-images.githubusercontent.com/52719688/217158704-431326b1-1b60-4c37-8a2c-2f154237acf7.png">
</p>

<p align="center"><i>
The Pavlov 2022 paper experimental design and results.
</p></i>

The 2020 Pavlov paper distinguishes between retention and manipulation. The retention task only tested participants’ ability to recall a string of 5, 6, or 7 letters shown for 3000 ms, followed by a delay of 6700 ms. The manipulation task asked participants to reorganize the letters into alphabetical order. They also found a positive correlation between theta executive index and performance in working memory tasks, but not in simple retention tasks, although other authors have found a correlation between theta power and retention. The 2022 paper seems to demonstrate such a correlation. The researchers also found a negative correlation between beta index and performance.

<p align="center">
<img width="271" alt="image3" src="https://user-images.githubusercontent.com/52719688/217158694-8e7ce022-85bf-43a6-a1ca-75801291a133.png">
</p>

<p align="center"><i>
The Pavlov 2022 data showing a spike in theta wave power in the memory task, but not in the eyes-closed rest task from the Fz electrode.
</p></i>

<p align="center">
<img width="271" alt="image3" src="https://user-images.githubusercontent.com/52719688/217446326-daacb6e9-34c2-4f39-9c4e-9fc9f31d932c.png">
</p>

<p align="center"><i>
Recreation of Pavlov 2022 paper results (Patient 43, Channel Fz).
</p></i>

The Wang paper reports partially different results. The team conducts tests of memory, memory (recalling day’s events), music (singing songs in head), and subtraction (counting backwards from 5000 by increments of 7), as well as open- and closed-eyed resting periods. The team measured log-transformed spectral power of theta and alpha waves, similarly to Pavlov’s team, and also only found theta wave spikes from the Fz electrode. Wang’s team only records a spike in theta waves in the subtraction task, not in memory. However, Wang’s team also records spikes in alpha waves from the Fz electrode, which were absent from Pavlov’s data. The spikes persisted for every task except for the eyes-opened rest period. It may be worth taking inspiration from Wang’s methods, since users will be using devices with their eyes open, and the alpha waves seem to capture more types of cognitive load. The spikes appear to be of similar magnitude with respect to task, which does not support the idea of ranking tasks by difficulty based on alpha or theta wave powers.

<p align="center">
<img alt="image3" src="https://user-images.githubusercontent.com/52719688/217158713-51b7b89d-a3ce-45f4-8d38-241279094c0e.png">
</p>

<p align="center"><i>
The Wang 2022 data showing, from the Fz electrode, a spike in theta power for only the math task, and a spike in alpha power for all tasks except for eyes-open rest.
</p></i>

<p align="center">
<img alt="image3" src="https://user-images.githubusercontent.com/52719688/217446328-051302d8-708f-4693-b44a-2b5c8a6bf6ba.png">
</p>

<p align="center"><i>
Recreation of the Wang 2022 paper results (Patient 1, Session 1, Channel Fz).
</p></i>


To at least replicate the results of the studies, we plan to conduct similar tests with a few key dimensions: task (retention vs. manipulation), load (number of digits or letters), the time the digits are shown, and the delay between the time they are shown and the time the participants are asked to recall or manipulate the letters or digits. We will measure the EEG data. To correlate the EEG data with the cognitive burden on the participants, we will measure both the accuracy of the participants’ memory or manipulation, as well as self-reported difficulty levels. A patient who achieves higher accuracy scores may have taken on more cognitive load to solve the problem, resulting in higher theta power and higher self-reported difficulty. Such a patient also may have a more efficient thought process that utilizes less cognitive load, resulting in lower theta power and lower self-reported difficulty. The self-reported component aims to distinguish between the situations where the same accuracy in solving the same task may result in differing theta powers. It may also be useful to compare the data with other biometric markers, such as pupillometry and ECG data, which the Pavlov team does.
If our product can quantify cognitive load in experiments similar to the papers, we will attempt to quantify cognitive load in more realistic tasks. We will create tests of common design flaws — long loading times, visual clutter, hidden information, etc. — that will incite cognitive load and see if the cognitive load can be detected. These tests will represent real-world issues rather than tests with the purpose of inciting cognitive load, and will be more relevant for product design.
Live classification and quantification of cognitive load is a goal. However, post-experimental data would still be useful in aiding product design.

### Signal Processing
	
Our signal processing will begin with removing artifacts such as eye blinks and facial movements. This can be partially achieved by automatically removing chunks of data with large spikes that cannot be caused purely by EEG. However, the papers referenced manually remove artifacts, which is not realistic for practical use. The literature also uses independent component analysis to reject artifacts. We also may simply rely on our narrow frequency range to remove noise and artifacts.
Since we are specifically looking for theta waves, we will apply bandpass filters from 4 Hz to 7 Hz. This will remove much of the noise as well and is consistent with the literature. 
To measure theta wave strength, we will use Welch’s method for computing the power spectral density. We will measure the relative power of theta waves compared to other frequencies to gauge cognitive load. We will also measure absolute spectral power as done in the cited papers. If this method fails, we will try a simpler Fourier analysis or neural networks.

### Technologies of Choice
	
We will build our signal processing and data analysis program in Python to take advantage of the variety of packages. We also plan on building our task program in Python to take advantage of the knowledge base of the team.
The data from the 2022 Pavlov paper uses .mat format, which requires modules h5py and pandas to load. From there, numpy is used for basic matrix operations. We will use the scipy.signal package to perform Butterworth filters on data. We will also use scipy.signal to use Welch’s method for computing power spectral density. Finally, we will use the numpy fast Fourier transform package. If we choose to use neural networks to classify data, we will use either scikit-learn or keras packages.


<p align="center">
<img width="552" alt="image2" src="https://user-images.githubusercontent.com/52719688/217158679-7d45f624-3c79-4bfb-aa32-b4b6bdfc4c62.png">
</p>

<p align="center"><i>
Our Project Data Flow.
</p></i>

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










