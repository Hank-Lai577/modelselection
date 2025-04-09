import numpy as np
import matplotlib.pyplot as plt

# read rPPG signal
rPPG_data = np.loadtxt("rPPG.txt") # np.loadtxt() is used to read .txt or .csv file
sampling_rate = 30  # sampling_rate is the frequency of input video
N = len(rPPG_data)  # len() is the length of signal

# generate time axis
t = np.linspace(0, (N-1) / sampling_rate, N) # np.linspace(start, stop, num) is a function to generate time x-axis

# calculate FFT
fft_result = np.fft.fft(rPPG_data)  # np.fft.fft() is a function to translate signal from  time domain into frequency domain
freqs = np.fft.fftfreq(N, d=1 / sampling_rate)  # np.fft.fftfreq(N, d=1 / sampling_rate) is a function to generate frequency domain x-axis

# only pick positive side
half_N = N // 2
freqs = freqs[:half_N]
fft_magnitude = np.abs(fft_result[:half_N])

positive_freqs = freqs > 0  # 過濾出 freq > 0 的索引
peak_index = np.argmax(fft_magnitude[positive_freqs])  # 找到最大值的索引
peak_freq = freqs[positive_freqs][peak_index]  # 最大值對應的頻率
peak_value = fft_magnitude[positive_freqs][peak_index]  # 最大值的振幅


# set figure size
plt.figure(figsize=(12, 5))

# time domain diagram
plt.subplot(1, 2, 1)
plt.plot(t, rPPG_data, label="rPPG Signal", color="b")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Time-Domain Signal")
plt.legend()
plt.grid()

# frequency domain diagram
plt.subplot(1, 2, 2)
plt.plot(freqs, fft_magnitude, color="r")
plt.scatter(peak_freq, peak_value, color="black", marker="o", label="Peak")
plt.annotate(f"{peak_freq:.2f} Hz", xy=(peak_freq, peak_value), xytext=(peak_freq + 0.5, peak_value),arrowprops=dict(facecolor='black', arrowstyle="->"), fontsize=10)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("rPPG Frequency Spectrum")
plt.grid()

plt.tight_layout()  # adjust spacing Automatically
plt.show()
