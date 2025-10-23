import os
import pandas as pd
import numpy as np

in_dir = '../part2_trimmed/'
out_dir = '../part2_position/'
os.makedirs(out_dir, exist_ok=True)

files = [f for f in os.listdir(in_dir) if f.startswith('trimmed_smooth_')]
for fname in files:
    df = pd.read_csv(os.path.join(in_dir, fname))
    t = df['time'].values
    az = df['az_smooth'].values

    v = np.cumtrapz(az, t, initial=0)
    x = np.cumtrapz(v, t, initial=0)
    x = x - x[0]

    out_df = pd.DataFrame({'time': t, 'position': x})
    new_name = fname.replace('trimmed_smooth_', 'position_')
    out_df.to_csv(os.path.join(out_dir, new_name), index=False)
