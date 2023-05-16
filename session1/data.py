

import pandas as pd
import matplotlib.pyplot as plt

f = 'amanda/OpenBCI-RAW-2023-05-10_16-29-04_eyesclosed_1.txt'
f2 = 'amanda/OpenBCI-RAW-2023-05-10_16-29-01.txt'
text = pd.read_csv(f, skiprows=4)

print(text.columns)
print(text.iloc[0])
print(text[' Timestamp'])

ch1 = text[' EXG Channel 1']

plt.plot(ch1[1000:1200])
plt.savefig('ch1.png')
print(ch1)