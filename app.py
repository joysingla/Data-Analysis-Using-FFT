# Author: [Karanveer Singh]
# LinkedIn : https://www.linkedin.com/in/karanveer-singh-98b381339/
# Date: [31st March 2025]
# Description: This Streamlit web app allows users to upload one or two CSV files, visualize them interactively, 
# detect peaks (maxima and minima) in the main file, and download the peak data as CSV files.

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy.signal import find_peaks

st.title("Graph Visualization & Peak Detection")

uploaded_file1 = st.file_uploader("Upload Main CSV file (*Compulsory)", type=["csv"])
uploaded_file2 = st.file_uploader("Upload Another CSV File (Optional, Add only if you want to compare these 2 files)", type=["csv"])

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

    fig.update_layout(title="Interactive Graph",
                      xaxis_title="Timestamp",
                      yaxis_title="Selected Data Column",
                      hovermode="x",
                      template="plotly_dark")

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Peak Detection & CSV Export (*For Main File Only)")

    maxima, _ = find_peaks(y1)
    minima, _ = find_peaks(-y1)

    maxima_values = y1.iloc[maxima].values
    minima_values = y1.iloc[minima].values

    maxima_timestamps = x1.iloc[maxima].values.astype(float)
    minima_timestamps = x1.iloc[minima].values.astype(float)

    maxima_slopes = np.diff(maxima_values) / np.diff(maxima_timestamps) if len(maxima_values) > 1 else []
    minima_slopes = np.diff(minima_values) / np.diff(minima_timestamps) if len(minima_values) > 1 else []

    maxima_table = pd.DataFrame({
        'Timestamp': maxima_timestamps[:-1] if len(maxima_values) > 1 else maxima_timestamps,
        'Maxima Value': maxima_values[:-1] if len(maxima_values) > 1 else maxima_values,
        'Slope': maxima_slopes if len(maxima_values) > 1 else [None]
    })

    minima_table = pd.DataFrame({
        'Timestamp': minima_timestamps[:-1] if len(minima_values) > 1 else minima_timestamps,
        'Minima Value': minima_values[:-1] if len(minima_values) > 1 else minima_values,
        'Slope': minima_slopes if len(minima_values) > 1 else [None]
    })

    st.download_button("Download Maxima CSV", maxima_table.to_csv(index=False), "maxima_table.csv", "text/csv")
    st.download_button("Download Minima CSV", minima_table.to_csv(index=False), "minima_table.csv", "text/csv")

    fig_peaks = go.Figure()
    fig_peaks.add_trace(go.Scatter(x=x1, y=y1, mode='lines', name="Original Data", line=dict(color="black")))
    fig_peaks.add_trace(go.Scatter(x=maxima_timestamps, y=maxima_values, mode='markers', name="Maxima", marker=dict(color='red', size=8)))
    fig_peaks.add_trace(go.Scatter(x=minima_timestamps, y=minima_values, mode='markers', name="Minima", marker=dict(color='blue', size=8)))

    fig_peaks.update_layout(title="Interactive Peak Detection (*For Main File Only)",
                            xaxis_title="Timestamp",
                            yaxis_title="Value",
                            hovermode="x",
                            template="plotly_dark")

    st.plotly_chart(fig_peaks, use_container_width=True)



