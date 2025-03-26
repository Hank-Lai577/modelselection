# modelselection
## FFT method 
### Overview
This method applies the Fast Fourier Transform (FFT) to convert the rPPG signal from the time domain to the frequency domain. By identifying the peak frequency corresponding to the heart rate and multiplying it by 60, we can determine the tester's heart rate.

### Requirements
- Python 3.x
- matplotlib
- numpy

### Usage
1. git clone https://github.com/Hank-Lai577/modelselection.git
2. Open FFT_code.py in the modelselection directory.
3. Run the script to process the rPPG signal.

### Features
- Reads rPPG signal data from rPPG.txt files.
- Plots the rPPG signal in both the time and frequency domains for comparison.
- Extracts the heart rate frequency to calculate the heart rate.

### Enhancements
- Directly output the calculated heart rate.