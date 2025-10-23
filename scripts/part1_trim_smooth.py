import os
import pandas as pd
from scipy.signal import savgol_filter

in_dir = '../part1_raw/'
out_dir = '../part1_positions/'
os.makedirs(out_dir, exist_ok=True)

files = [f for f in os.listdir(in_dir) if f.endswith('.csv')]
for fname in files:
    df = pd.read_csv(os.path.join(in_dir, fname))
    t = df['time'].values
    az = df['az'].values
    # --- SET these indices after inspection for each file ---
    start, end = 100, 900
    t_trim = t[start:end]
    az_trim = az[start:end]
    az_smooth = savgol_filter(az_trim, 21, 2)

    # Double integration
    import numpy as np
    v = np.cumtrapz(az_smooth, t_trim, initial=0)
    x = np.cumtrapz(v, t_trim, initial=0)
    x = x - x[0]

    out_df = pd.DataFrame({'time': t_trim, 'position': x})
    new_name = fname.replace('.csv', '_position.csv')
    out_df.to_csv(os.path.join(out_dir, new_name), index=False)
