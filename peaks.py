import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

data = pd.read_csv('SampleData.csv')
values = data['IMU[0].AccX']
sampling_frequency = 2000  

maxima, _ = find_peaks(values)
minima, _ = find_peaks(-values)

maxima_values = values[maxima]
minima_values = values[minima]

maxima_timestamps = data.index[maxima]
minima_timestamps = data.index[minima]

maxima_slopes = np.diff(maxima_values) / np.diff(maxima_timestamps)
minima_slopes = np.diff(minima_values) / np.diff(minima_timestamps)

maxima_table = pd.DataFrame({
    'Timestamp': maxima_timestamps[:-1],
    'Maxima Value': maxima_values[:-1],
    'Slope': maxima_slopes
})

minima_table = pd.DataFrame({
    'Timestamp': minima_timestamps[:-1],
    'Minima Value': minima_values[:-1],
    'Slope': minima_slopes
})

maxima_table.to_csv('maxima_table.csv', index=False)
minima_table.to_csv('minima_table.csv', index=False)

plt.figure(figsize=(20, 10))
plt.plot(values, label='Original Data', color='black')  
plt.plot(maxima, maxima_values, 'ro', label='Maxima', markersize=2)  
plt.plot(minima, minima_values, 'bo', label='Minima', markersize=2)  
plt.legend()
plt.title('Peak Detection with Maxima and Minima Highlighted as Dots')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)
plt.show()
