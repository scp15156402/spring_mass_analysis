import os
import pandas as pd
import numpy as np
from scipy.signal import find_peaks

in_dir = '../part2_position/'
out_dir = '../part2_results/'
os.makedirs(out_dir, exist_ok=True)

files = [f for f in os.listdir(in_dir) if f.startswith('position_')]
zeta_list = []
delta_list = []
x1_list = []
x2_list = []

for fname in files:
    df = pd.read_csv(os.path.join(in_dir, fname))
    x = df['position'].values

    peaks, _ = find_peaks(x, height=np.std(x))
    n = 3
    if len(peaks) > n:
        x1 = x[peaks[0]]
        x2 = x[peaks[n]]
        delta = (1/n) * np.log(x1 / x2)
        zeta = delta / (2 * np.pi)
    else:
        x1 = np.nan
        x2 = np.nan
        delta = np.nan
        zeta = np.nan

    zeta_list.append(zeta)
    delta_list.append(delta)
    x1_list.append(x1)
    x2_list.append(x2)

damp_df = pd.DataFrame({'delta': delta_list, 'zeta': zeta_list, 'x1': x1_list, 'x2': x2_list})
damp_df.to_csv(os.path.join(out_dir, 'damping_results.csv'), index=False)
