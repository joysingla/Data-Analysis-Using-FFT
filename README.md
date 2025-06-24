# Time Series Data Analysis using FFT, DFT, and DTW

## Author: [joy singla]
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Karanveer%20Singh-blue)](https://www.linkedin.com/in/joy-singla-923005357/)

📅 **Date:** 31st March 2025  
🌐 **Live Streamlit App:** [Click here to try the app](https://data-analysis-comparision-and-peaks.streamlit.app/)  
📂 **GitHub Repo:** [Data-Analysis-Using-FFT-DFT-and-DTW](https://github.com/joysingla/Data-Analysis-Using-FFT)

---

## Overview
This repository provides a generalized framework for analyzing time series data using various techniques, including **Fast Fourier Transform (FFT), Discrete Fourier Transform (DFT), and Dynamic Time Warping (DTW)**. The dataset primarily consists of **time series data from an Inertial Measurement Unit (IMU)**, and the analysis methods are tailored to process and extract meaningful insights from the sensor data.

This project is designed for applications such as **sensor data analysis, motion tracking, and anomaly detection**, and can be extended for other time series datasets.

---

## 🎯 Features

- ✅ **Interactive Streamlit App** for seamless user experience — no coding required!
- 📈 **Simple Time Series Plot** of acceleration vs timestamp.
- ⚡ **FFT Plot** to analyze frequency components.
- 🔄 **Compare Two Files** — visualize and compare time series and FFTs side-by-side.
- 🌊 **DTW Comparison** to assess similarity between two signals.
- 🚩 **Automatic Peak Detection** in the data.
- 📥 **Downloadable Output** — graphs, FFT results, and peak info can all be downloaded as CSV.
- 🧩 **Modular Python Scripts** — for users who prefer using the code directly.

---

## Installation Guide

Follow these steps to set up your environment and install the required dependencies:

### 1. Clone the Repository
```sh
git clone https://github.com/Karanveer69/Data-Analysis-Using-FFT-DFT-and-DTW.git
```

### 2. Navigate to the Project Directory
```sh
cd Data-Analysis-Using-FFT-DFT-and-DTW
```

### 3. Set Up a Virtual Environment
It's recommended to use a virtual environment to avoid dependency conflicts.

#### Using `venv` (Standard Library):
```sh
python3 -m venv venv
```
This will create a folder named `venv` that contains the isolated environment.

#### Activate the Virtual Environment:
- **On Windows:**
  ```sh
  .\venv\Scripts\activate
  ```
- **On macOS/Linux:**
  ```sh
  source venv/bin/activate
  ```
After activation, your terminal prompt should change to indicate you're working inside the virtual environment.

### 4. Install Required Dependencies
```sh
pip install requirements.txt
```

### 5. Verify Installation (Optional)
Run the following Python commands to ensure all dependencies are installed correctly:
```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from dtaidistance import dtw
```
If no errors appear, the installation was successful.

---

## Usage

Once everything is set up, you can run the analysis scripts provided in the repository to process and analyze your time series data.

```sh
python analysis_script.py  # Replace with actual script name
```

---

## License
This project is licensed under the **MIT License**.

---

## Contact
For any queries, feel free to reach out via [LinkedIn](https://www.linkedin.com/in/karanveer-singh-98b381339/).

---

Enjoy analyzing time series data! 🚀

