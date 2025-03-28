import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('Pixhawk IMU0 ACC X Y Z(1).csv')  
signal = data['IMU[0].AccX']  
sampling_frequency = 2000
N = len(signal)


fft_result = np.fft.fft(signal)
freqs = np.fft.fftfreq(len(signal), 1/sampling_frequency)

magnitude = abs(np.real(fft_result))
scaled_magnitude = 10 * np.log10(magnitude)

table = pd.DataFrame({
    'Frequency': freqs[:-1],
    'Amplitude':scaled_magnitude[:-1]
})
table.to_csv('table.csv',index=False)

plt.figure(figsize=(20,10)) 
plt.plot(freqs[0:len(freqs)//2], scaled_magnitude[0:len(freqs)//2])  
plt.title('Real Part by FFT Analysis Using Logarithmic Scaling (Shifted)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (dB)')
plt.grid(True)  
plt.show()