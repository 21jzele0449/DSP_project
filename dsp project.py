import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, find_peaks
import neurokit2 as nk
import streamlit as st

st.title("ECG Signal Analysis")
st.sidebar.header("Settings")

fs = st.sidebar.slider("Sampling Frequency (Hz)", min_value=100, max_value=500, value=360, step=10)
duration = st.sidebar.slider("Signal Duration (seconds)", min_value=5, max_value=30, value=20, step=1)
st.sidebar.subheader("Signal Generation")

ecg_signal = nk.ecg_simulate(duration=duration, sampling_rate=fs)
st.sidebar.write(f"Generated synthetic ECG signal with {len(ecg_signal)} samples.")
def high_pass_filter(signal, cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return filtfilt(b, a, signal)

def notch_filter(signal, notch_freq, fs, quality_factor=30):
    nyquist = 0.5 * fs
    w0 = notch_freq / nyquist
    b, a = butter(2, [w0 - w0 / quality_factor, w0 + w0 / quality_factor], btype='bandstop')
    return filtfilt(b, a, signal)

def low_pass_filter(signal, cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return filtfilt(b, a, signal)

filtered_signal = high_pass_filter(ecg_signal, cutoff=0.5, fs=fs)
filtered_signal = notch_filter(filtered_signal, notch_freq=50, fs=fs)
filtered_signal = low_pass_filter(filtered_signal, cutoff=100, fs=fs)
squared_signal = np.square(np.gradient(filtered_signal))
window_size = int(0.150 * fs) 
 
moving_avg = np.convolve(squared_signal, np.ones(window_size) / window_size, mode='same')
peaks, _ = find_peaks(moving_avg, height=np.mean(moving_avg) * 1.2, distance=fs * 0.6)  
if len(peaks) > 1:
    rr_intervals = np.diff(peaks) / fs  
    heart_rate = 60 / np.mean(rr_intervals)
else:
    heart_rate = 0
st.subheader("Original ECG Signal")
st.line_chart(ecg_signal)
st.subheader("Filtered ECG Signal")
st.line_chart(filtered_signal)
st.subheader("QRS Detection and Results")
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(ecg_signal, label='Original ECG Signal', alpha=0.5)
ax.plot(filtered_signal, label='Filtered ECG Signal')
ax.plot(peaks, filtered_signal[peaks], 'ro', label='QRS Peaks')
ax.set_title(f"Heart Rate: {heart_rate:.2f} BPM")
ax.set_xlabel('Samples')
ax.set_ylabel('Amplitude')
ax.legend()
st.pyplot(fig)
st.sidebar.subheader("Results")
st.sidebar.write(f"Heart Rate: {heart_rate:.2f} BPM")

