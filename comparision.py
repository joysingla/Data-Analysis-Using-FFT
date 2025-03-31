# Author: [Karanveer Singh]
# LinkedIn : https://www.linkedin.com/in/karanveer-singh-98b381339/
# Date: [31st March 2025]
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data1 = pd.read_csv('ReferenceData.csv')
data2 = pd.read_csv('SampleData.csv')

signal1 = data1['IMU[0].AccX']
signal2 = data2['IMU[0].AccX']

sampling_frequency = 2000
N1 = len(signal1)
N2 = len(signal2)

fft_result1 = np.fft.fft(signal1)
fft_result2 = np.fft.fft(signal2)

freqs1 = np.fft.fftfreq(N1, 1/sampling_frequency)
freqs2 = np.fft.fftfreq(N2, 1/sampling_frequency)

magnitude1 = np.abs(fft_result1)
scaled_magnitude1 = 10 * np.log10(magnitude1)

magnitude2 = np.abs(fft_result2)
scaled_magnitude2 = 10 * np.log10(magnitude2)

plt.figure(figsize=(20, 10))
plt.plot(freqs1[:N1//2], scaled_magnitude1[:N1//2],'r-')
plt.plot(freqs2[:N2//2], scaled_magnitude2[:N2//2],'b-')
plt.title('FFT Analysis of IMU Data')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (dB)')
plt.grid(True)
plt.show()
