import os
import pandas as pd
import numpy as np

in_dir = '../part2_trimmed/'
out_dir = '../part2_results/'
os.makedirs(out_dir, exist_ok=True)

files = [f for f in os.listdir(in_dir) if f.startswith('trimmed_smooth_')]
omega_d_list = []

for fname in files:
    df = pd.read_csv(os.path.join(in_dir, fname))
    t = df['time'].values
    az = df['az_smooth'].values
    dt = np.mean(np.diff(t))
    n = len(az)

    fft_vals = np.fft.fft(az - np.mean(az))
    fft_freqs = np.fft.fftfreq(n, d=dt)
    pos_mask = (fft_freqs > 0)
    main_freq = fft_freqs[pos_mask][np.argmax(np.abs(fft_vals[pos_mask]))]
    omega_d = 2 * np.pi * main_freq
    omega_d_list.append(omega_d)

omega_df = pd.DataFrame({'omega_d': omega_d_list})
omega_df.to_csv(os.path.join(out_dir, 'omega_d_results.csv'), index=False)
