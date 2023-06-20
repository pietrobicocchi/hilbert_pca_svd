from scipy.signal import hilbert
import numpy as np

def analytic_signal(data):
    # Perform Hilbert transform on the data
    analytic_signal = np.matrix(hilbert(data, axis=0))

    # Calculate the mean and standard deviation of each column
    mean = np.mean(analytic_signal, axis=0)
    std_dev = np.std(analytic_signal, axis=0)

    # Normalize each column
    analytic_signal = (analytic_signal - mean) / std_dev  # now it's normalized!

    return analytic_signal