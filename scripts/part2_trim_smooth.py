import os
import pandas as pd
import numpy as np
from scipy.signal import savgol_filter

in_dir = '../part2_raw/'
out_dir = '../part2_trimmed/'
os.makedirs(out_dir, exist_ok=True)

files = [f for f in os.listdir(in_dir) if f.endswith('.csv')]
for fname in files:
    df = pd.read_csv(os.path.join(in_dir, fname))
    t = df['time'].values
    az = df['az'].values
    # --- SET manually after looking at data! ---
    start, end = 100, 900
    t_trim = t[start:end]
    az_trim = az[start:end]
    az_smooth = savgol_filter(az_trim, 21, 2)

    trimmed = pd.DataFrame({'time': t_trim, 'az_smooth': az_smooth})
    trimmed.to_csv(os.path.join(out_dir, f'trimmed_smooth_{fname}'), index=False)
