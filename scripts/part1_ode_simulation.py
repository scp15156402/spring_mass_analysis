import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

summary_df = pd.read_csv('../part2_results/ultimate_summary.csv')
if "Median" in summary_df['Trial'].astype(str).values:
    m = float(summary_df.set_index('Trial').loc['Median', 'm (kg)'])
    k = float(summary_df.set_index('Trial').loc['Median', 'k (N/m)'])
    zeta = float(summary_df.set_index('Trial').loc['Median', 'zeta'])
    omega_d = float(summary_df.set_index('Trial').loc['Median', 'omega_d (rad/s)'])
else:
    m = summary_df['m (kg)'].median()
    k = summary_df['k (N/m)'].median()
    zeta = summary_df['zeta'].median()
    omega_d = summary_df['omega_d (rad/s)'].median()
c = 2 * m * zeta * omega_d

ab_df = pd.read_csv('../part1_results/fitted_AB.csv')
in_dir = '../part1_positions/'
out_dir = '../part1_results/'

for idx, row in ab_df.iterrows():
    fname = row['trial']
    A, B = row['A'], row['B']
    pos_df = pd.read_csv(os.path.join(in_dir, fname))
    t = pos_df['time'].values

    # Derive initial conditions from A, B
    x0 = A
    v0 = B * omega_d - zeta * omega_d * A

    # ODE System
    def fun(t, y):
        x, v = y
        return [v, -(c / m) * v - (k / m) * x]

    y0 = [x0, v0]
    sol = solve_ivp(fun, [t[0], t[-1]], y0, t_eval=t)

    # Plot data vs simulation
    plt.plot(t, pos_df['position'], label='Exp')
    plt.plot(t, sol.y[0], '--', label='ODE Sim')
    plt.xlabel('Time (s)'); plt.ylabel('Position (m)')
    plt.title(fname)
    plt.legend()
    plt.savefig(os.path.join(out_dir, fname.replace('.csv', '_ODEcomp.png')))
    plt.clf()

    # Save simulated position as CSV
    pd.DataFrame({'time': t, 'ode_sim_position': sol.y[0]}).to_csv(
        os.path.join(out_dir, fname.replace('.csv', '_ODEsim.csv')), index=False)
