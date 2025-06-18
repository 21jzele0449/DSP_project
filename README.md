# DSP_project
# ECG Signal Processing using DSP Techniques :
This project focuses on filtering noise from real-world ECG signals and extracting key cardiac parameters using digital signal processing (DSP) methods to enhance accuracy in clinical diagnosis.

## ECG Signal Processing with Python

This project applies **Digital Signal Processing (DSP)** techniques to denoise ECG signals and extract key cardiac features such as the **QRS complex** and **heart rate**. It provides an interactive interface using **Streamlit**, making it suitable for educational and clinical analysis.


## Abstract

Electrocardiogram (ECG) signals are essential for diagnosing cardiovascular diseases. However, raw ECG data often contains noise from various sources such as power line interference, muscle artifacts, and baseline drift. This project implements effective filtering techniques and feature extraction methods using Python libraries like `SciPy`, `NeuroKit2`, and `Streamlit` to analyze and visualize ECG signals.


## Project Objectives

1. Apply noise filtering techniques to ECG signals.
2. Detect and extract key ECG features: **QRS complex** and **heart rate**.
3. Visualize and interactively analyze ECG signals via a Streamlit dashboard.


## 🧪 Methodology:

# Signal Acquisition
- A **synthetic ECG signal** is generated using `NeuroKit2` to simulate real-world cardiac activity.

# Noise Filtering
- **High-Pass Filter (0.5 Hz)**: Removes baseline drift.
- **Notch Filter (50 Hz)**: Eliminates power line interference.
- **Low-Pass Filter (100 Hz)**: Removes high-frequency noise.
- Filters implemented using the **Butterworth** design via `scipy.signal`.

# Feature Extraction
- **QRS Complex Detection**: Performed using the squared derivative of the filtered signal.
- **Peak Detection**: Implemented using `find_peaks()` from `SciPy`.
- **Heart Rate**: Calculated using RR intervals.

# Visualization
- Real-time plots using **Streamlit**:
  - Raw ECG Signal
  - Filtered Signal
  - QRS Peaks & Heart Rate

---

## Tech Stack & Libraries

| Library       | Purpose                            |
|---------------|------------------------------------|
| `numpy`       | Numerical computations             |
| `matplotlib`  | Plotting ECG signals               |
| `scipy.signal`| Signal filtering & peak detection  |
| `neurokit2`   | ECG signal simulation              |
| `streamlit`   | Interactive web-based UI           |


## Results:

- Filters effectively **clean ECG signals**.
- QRS detection accurately **identifies R-peaks**.
- **Heart rate** calculated aligns with expected values.
- Interactive interface allows users to **adjust parameters in real-time**.


## Conclusion:

This project successfully demonstrates:
- ECG signal **denoising**
- Accurate **QRS complex detection**
- Real-time **visualization** and **heart rate computation**


## Future Work:

- Integrate real-time ECG monitoring via wearable sensors.
- Implement machine learning for arrhythmia detection.
- Improve GUI for mobile and clinical usability.
- Support real ECG datasets (e.g., MIT-BIH).


