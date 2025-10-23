import os
import pandas as pd

out_dir = '../part2_results/'
m = 0.200  # kg

omega_df = pd.read_csv(os.path.join(out_dir, 'omega_d_results.csv'))
omega_df['k'] = m * omega_df['omega_d']**2
omega_df.to_csv(os.path.join(out_dir, 'k_results.csv'), index=False)
