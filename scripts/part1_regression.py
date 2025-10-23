import os
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Load summary constants (use Median row for omega_d, zeta)
summary_df = pd.read_csv('../part2_results/ultimate_summary.csv')
# If your median row has index 'Median', use .loc['Median'], else change as required
if "Median" in summary_df['Trial'].astype(str).values:
    zeta = float(summary_df.set_index('Trial').loc['Median', 'zeta'])
    omega_d = float(summary_df.set_index('Trial').loc['Median', 'omega_d (rad/s)'])
else:
    zeta = summary_df['zeta'].median()
    omega_d = summary_df['omega_d (rad/s)'].median()

in_dir = '../part1_positions/'
out_dir = '../part1_results/'
os.makedirs(out_dir, exist_ok=True)
files = [f for f in os.listdir(in_dir) if f.endswith('_position.csv')]

results = []
for fname in files:
    df = pd.read_csv(os.path.join(in_dir, fname))
    t = df['time'].values
    x = df['position'].values
    def model_func(t, A, B):
        return np.exp(-zeta * omega_d * t) * (A * np.cos(omega_d * t) + B * np.sin(omega_d * t))
    popt, _ = curve_fit(model_func, t, x)
    A_fit, B_fit = popt
    results.append({'trial': fname, 'A': A_fit, 'B': B_fit})
    # Plot
    plt.plot(t, x, label='Exp')
    plt.plot(t, model_func(t, *popt), '--', label='Fit')
    plt.legend(); plt.title(fname)
    plt.xlabel('Time (s)'); plt.ylabel('Position (m)')
    plt.savefig(os.path.join(out_dir, f"{fname}_fit.png"))
    plt.clf()

pd.DataFrame(results).to_csv(os.path.join(out_dir, 'fitted_AB.csv'), index=False)
