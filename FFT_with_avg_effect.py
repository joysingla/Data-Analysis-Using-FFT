import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your data
data = pd.read_csv('Final_17-12-2024_Test1.IMU1.xlsx2.csv')  # Replace with your actual file path
signal = data['IMU[1].AccX2']  # Replace with your IMU acceleration data column name
sampling_frequency = 2000  # Set your sampling frequency
N = len(signal)

# Apply Hanning window
window = np.hanning(N)
windowed_signal = signal * window

# Compute the FFT
fft_result = np.fft.fft(windowed_signal)
# Compute the frequencies
freqs = np.fft.fftfreq(N, 1/sampling_frequency)

# Logarithmic scaling
magnitude = np.abs(fft_result)
scaled_magnitude = 10 * np.log10(magnitude)

# Define frequency bins with 2 Hz width
bin_width = 2
nyquist_freq = sampling_frequency / 2
bins = np.arange(0, nyquist_freq + bin_width, bin_width)

# Initialize an array to hold the averaged magnitudes
averaged_magnitudes = []

# Average magnitudes within each bin
for i in range(len(bins) - 1):
    bin_start = bins[i]
    bin_end = bins[i + 1]
    # Find indices corresponding to the current bin
    bin_indices = np.where((freqs >= bin_start) & (freqs < bin_end))[0]
    if bin_indices.size > 0:
        # Compute the average magnitude for this bin
        avg_magnitude = np.mean(scaled_magnitude[bin_indices])
        averaged_magnitudes.append(avg_magnitude)
    else:
        averaged_magnitudes.append(0)

# Convert to numpy array for easier slicing
averaged_magnitudes = np.array(averaged_magnitudes)

# Apply a moving average to smooth the data
window_size = 5  # Adjust as needed
smoothed_magnitudes = np.convolve(averaged_magnitudes, np.ones(window_size)/window_size, mode='same')

# Adjust bins to align with the smoothed data
trim_size = (window_size - 1) // 2
smoothed_bins = bins[trim_size: -trim_size] if trim_size > 0 else bins

# Ensure both arrays have the same length
min_length = min(len(smoothed_bins), len(smoothed_magnitudes))
smoothed_bins = smoothed_bins[:min_length]
smoothed_magnitudes = smoothed_magnitudes[:min_length]

# Plotting the smoothed magnitudes
plt.figure(figsize=(10, 8))
plt.plot(smoothed_bins, smoothed_magnitudes, color='b', linewidth=2)
plt.title('Smoothed Magnitudes by FFT Analysis with 2 Hz Binning and Hanning Window')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Average Amplitude (dB)')
plt.grid(True)
plt.show()
