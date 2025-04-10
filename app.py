# # Author: [Karanveer Singh]
# # LinkedIn : https://www.linkedin.com/in/karanveer-singh-98b381339/
# # Date: [31st March 2025]
# # Description: This Streamlit web app allows users to upload one or two CSV files, visualize them interactively, 
# # Detect peaks (maxima and minima) in the main file, and download the peak data as CSV files.

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy.signal import find_peaks

st.title("Graph Visualization, Peak Detection & FFT Analysis")

uploaded_file1 = st.file_uploader("Upload Main CSV file (*Compulsory)", type=["csv"])
uploaded_file2 = st.file_uploader("Upload Another CSV File (Optional)", type=["csv"])

if uploaded_file1:
    data1 = pd.read_csv(uploaded_file1)
    st.subheader("Select Columns for Main File")
    time_col1 = st.selectbox("Select Timestamp Column", data1.columns)
    value_col1 = st.selectbox("Select Data Column", data1.columns)

    x1 = data1[time_col1]
    y1 = data1[value_col1]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x1, y=y1, mode='lines', name='1st Graph', line=dict(color='red')))

    if uploaded_file2:
        data2 = pd.read_csv(uploaded_file2)
        st.subheader("Select Columns for Second File")
        time_col2 = st.selectbox("Select Timestamp Column (File 2)", data2.columns)
        value_col2 = st.selectbox("Select Data Column (File 2)", data2.columns)

        x2 = data2[time_col2]
        y2 = data2[value_col2]
        fig.add_trace(go.Scatter(x=x2, y=y2, mode='lines', name='2nd Graph', line=dict(color='blue')))

    fig.update_layout(title="Interactive Graph: Main and Optional File", xaxis_title="Timestamp", yaxis_title="Selected Data Column", hovermode="x", template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("FFT Analysis of IMU Data")
    sampling_frequency = st.number_input("Enter Sampling Frequency (Hz)", min_value=1, max_value=10000, value=2000, step=1)

    N = len(y1)
    fft_result1 = np.fft.fft(y1)
    freqs1 = np.fft.fftfreq(N, 1/sampling_frequency)
    magnitude1 = np.abs(fft_result1)
    scaled_magnitude1 = 10 * np.log10(magnitude1)

    fft_table1 = pd.DataFrame({'Frequency (Hz)': freqs1[:N//2], 'Amplitude (dB)': scaled_magnitude1[:N//2]})
    st.download_button("Download FFT CSV (Main File)", fft_table1.to_csv(index=False), "fft_analysis_results_main.csv", "text/csv")

    fig_fft1 = go.Figure()
    fig_fft1.add_trace(go.Scatter(x=freqs1[:N//2], y=scaled_magnitude1[:N//2], mode='lines', name='FFT Magnitude Spectrum (Main File)'))
    fig_fft1.update_layout(title="FFT Analysis (Main File)", xaxis_title="Frequency (Hz)", yaxis_title="Amplitude (dB)", hovermode="x", template="plotly_dark")
    st.plotly_chart(fig_fft1, use_container_width=True)

    if uploaded_file2:
        N2 = len(y2)
        fft_result2 = np.fft.fft(y2)
        freqs2 = np.fft.fftfreq(N2, 1/sampling_frequency)
        magnitude2 = np.abs(fft_result2)
        scaled_magnitude2 = 10 * np.log10(magnitude2)

        fft_table2 = pd.DataFrame({'Frequency (Hz)': freqs2[:N2//2], 'Amplitude (dB)': scaled_magnitude2[:N2//2]})
        st.download_button("Download FFT CSV (Second File)", fft_table2.to_csv(index=False), "fft_analysis_results_second.csv", "text/csv")

        fig_fft2 = go.Figure()
        fig_fft2.add_trace(go.Scatter(x=freqs2[:N2//2], y=scaled_magnitude2[:N2//2], mode='lines', name='FFT Magnitude Spectrum (Second File)'))
        fig_fft2.update_layout(title="FFT Analysis (Second File)", xaxis_title="Frequency (Hz)", yaxis_title="Amplitude (dB)", hovermode="x", template="plotly_dark")
        st.plotly_chart(fig_fft2, use_container_width=True)

        fig_fft_combined = go.Figure()
        fig_fft_combined.add_trace(go.Scatter(x=freqs1[:N//2], y=scaled_magnitude1[:N//2], mode='lines', name='Main File', line=dict(color='red')))
        fig_fft_combined.add_trace(go.Scatter(x=freqs2[:N2//2], y=scaled_magnitude2[:N2//2], mode='lines', name='Second File', line=dict(color='blue')))
        fig_fft_combined.update_layout(title="Combined FFT Analysis (Main & Second File)", xaxis_title="Frequency (Hz)", yaxis_title="Amplitude (dB)", hovermode="x", template="plotly_dark")
        st.plotly_chart(fig_fft_combined, use_container_width=True)

    st.subheader("Peak Detection & CSV Export (*For Main File Only)")

    maxima, _ = find_peaks(y1)
    minima, _ = find_peaks(-y1)

    maxima_values = y1.iloc[maxima].values
    minima_values = y1.iloc[minima].values
    maxima_timestamps = x1.iloc[maxima].values.astype(float)
    minima_timestamps = x1.iloc(minima).values.astype(float)

    maxima_slopes = np.diff(maxima_values) / np.diff(maxima_timestamps) if len(maxima_values) > 1 else []
    minima_slopes = np.diff(minima_values) / np.diff(minima_timestamps) if len(minima_values) > 1 else []

    maxima_table = pd.DataFrame({'Timestamp': maxima_timestamps[:-1] if len(maxima_values) > 1 else maxima_timestamps,
                                 'Maxima Value': maxima_values[:-1] if len(maxima_values) > 1 else maxima_values,
                                 'Slope': maxima_slopes if len(maxima_values) > 1 else [None]})

    minima_table = pd.DataFrame({'Timestamp': minima_timestamps[:-1] if len(minima_values) > 1 else minima_timestamps,
                                 'Minima Value': minima_values[:-1] if len(minima_values) > 1 else minima_values,
                                 'Slope': minima_slopes if len(minima_values) > 1 else [None]})

    st.download_button("Download Maxima CSV", maxima_table.to_csv(index=False), "maxima_table.csv", "text/csv")
    st.download_button("Download Minima CSV", minima_table.to_csv(index=False), "minima_table.csv", "text/csv")

    fig_peaks = go.Figure()
    fig_peaks.add_trace(go.Scatter(x=x1, y=y1, mode='lines', name="Original Data", line=dict(color="black")))
    fig_peaks.add_trace(go.Scatter(x=maxima_timestamps, y=maxima_values, mode='markers', name="Maxima (Main File)", marker=dict(color='red', size=8)))
    fig_peaks.add_trace(go.Scatter(x=minima_timestamps, y=minima_values, mode='markers', name="Minima (Main File)", marker=dict(color='blue', size=8)))

    fig_peaks.update_layout(title="Peak Detection Graph (Main File)", xaxis_title="Timestamp", yaxis_title="Value", hovermode="x", template="plotly_dark")
    st.plotly_chart(fig_peaks, use_container_width=True)

    if uploaded_file2:
        maxima2, _ = find_peaks(y2)
        minima2, _ = find_peaks(-y2)

        maxima_values2 = y2.iloc[maxima2].values
        minima_values2 = y2.iloc[minima2].values
        maxima_timestamps2 = x2.iloc[maxima2].values.astype(float)
        minima_timestamps2 = x2.iloc[minima2].values.astype(float)

        fig_peaks2 = go.Figure()
        fig_peaks2.add_trace(go.Scatter(x=x2, y=y2, mode='lines', name="Original Data", line=dict(color="black")))
        fig_peaks2.add_trace(go.Scatter(x=maxima_timestamps2, y=maxima_values2, mode='markers', name="Maxima (Second File)", marker=dict(color='red', size=8)))
        fig_peaks2.add_trace(go.Scatter(x=minima_timestamps2, y=minima_values2, mode='markers', name="Minima (Second File)", marker=dict(color='blue', size=8)))

        fig_peaks2.update_layout(title="Peak Detection Graph (Second File)", xaxis_title="Timestamp", yaxis_title="Value", hovermode="x", template="plotly_dark")
        st.plotly_chart(fig_peaks2, use_container_width=True)
