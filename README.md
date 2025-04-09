# modelselection
## FFT method 
### Overview
This method applies the Fast Fourier Transform (FFT) to convert the rPPG signal from the time domain to the frequency domain. By identifying the peak frequency corresponding to the heart rate and multiplying it by 60, we can determine the tester's heart rate.

### Requirements
- Python 3.9
- matplotlib
- numpy

### Usage
1. git clone our repository
2. Open FFT_code.py in the main file.
3. Run the script to process the rPPG signal.

### Features
- input: rPPG signal data from facial video.
- output: rPPG signal of time and frequency domains
- goal: calculate the heart rate
- Reads rPPG signal data from rPPG.txt files.
- Plots the rPPG signal in both the time and frequency domains for comparison.
- Extracts the heart rate frequency to calculate the heart rate.

### Enhancements
- Directly output the calculated heart rate.