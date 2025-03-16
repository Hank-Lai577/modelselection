import matplotlib.pyplot as plt
import numpy as np
import os

def plot(path_name:str, cilp_frame=3000):
    PPG_gt = np.loadtxt(path_name)
    num = int(len(PPG_gt) / cilp_frame)
    for i in range(num):
        PPG_gt_cilp = PPG_gt[cilp_frame * i:cilp_frame * (i + 1)]
        plt.figure(figsize=(17, 8))
        plt.plot(PPG_gt_cilp)
        plt.title(path_name.split('/')[-1])
        plt.show()


all_path = "./temp1"
all_file = os.listdir(all_path)
all_file = sorted(all_file)
for file in all_file:
    path = os.path.join(all_path, file)
    plot(path)
