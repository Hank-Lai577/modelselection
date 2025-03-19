import numpy as np
import matplotlib.pyplot as plt

# 讀取 rPPG 訊號
rPPG_data = np.loadtxt("rPPG.txt")  # 假設 TXT 只有 rPPG 數值
sampling_rate = 30  # 輸入影片的頻率
N = len(rPPG_data)  # 訊號長度

# 產生時間軸
t = np.linspace(0, (N-1) / sampling_rate, N) # np.linspace(start, stop, num)

# 計算 FFT
fft_result = np.fft.fft(rPPG_data)  # 用於計算傅立葉轉換的公式，主要是將時域信號轉換為頻域信號
freqs = np.fft.fftfreq(N, d=1 / sampling_rate)  # 計算頻率對應關係，np.fft.fftfreq 是 NumPy 中用來生成傅立葉轉換後對應的頻率軸的函數。

# 只取正頻率部分
half_N = N // 2
 

# 畫圖
plt.figure(figsize=(12, 5))

# 繪製時域訊號
plt.subplot(1, 2, 1)
plt.plot(t, rPPG_data, label="rPPG Signal", color="b")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Time-Domain Signal")
plt.legend()
plt.grid()

# 畫出頻譜圖
plt.subplot(1, 2, 2)
plt.plot(freqs, fft_magnitude, color="r")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("rPPG Frequency Spectrum")
plt.grid()

plt.tight_layout()  # 自動調整間距
plt.show()
