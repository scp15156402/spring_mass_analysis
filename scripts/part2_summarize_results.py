import os
import pandas as pd
import numpy as np

out_dir = '../part2_results/'
m = 0.200

k_df     = pd.read_csv(os.path.join(out_dir, 'k_results.csv'))
damp_df  = pd.read_csv(os.path.join(out_dir, 'damping_results.csv'))
omega_df = pd.read_csv(os.path.join(out_dir, 'omega_d_results.csv'))

median_k      = np.median(k_df['k'])
median_omega  = np.median(omega_df['omega_d'])
median_zeta   = np.nanmedian(damp_df['zeta'])

summary_df = pd.DataFrame({
    'Trial': np.arange(1, 6),
    'm (kg)': [m]*5,
    'k (N/m)': k_df['k'],
    'omega_d (rad/s)': omega_df['omega_d'],
    'zeta': damp_df['zeta']
})

summary_df.loc['Median'] = ['', m, median_k, median_omega, median_zeta]
summary_df.to_csv(os.path.join(out_dir, 'ultimate_summary.csv'), index=False)

print("Ultimate Experimental Results:")
print(f"Mass (m): {m:.3f} kg")
print(f"Median Spring Constant (k): {median_k:.4f} N/m")
print(f"Median Damping Ratio (zeta): {median_zeta:.4f}")
print(f"Median Damped Angular Frequency (omega_d): {median_omega:.4f} rad/s")
