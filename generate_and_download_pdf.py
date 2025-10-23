import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

report_md = []
fig_count = 1

# --- 1. Raw Acceleration Data: X, Y, Z ---
try:
    df_raw = pd.read_csv("part2_raw/trial1.csv")
    plt.figure(figsize=(10,5))
    plt.plot(df_raw["time"], df_raw["ax"], label="Acceleration X")
    plt.plot(df_raw["time"], df_raw["ay"], label="Acceleration Y")
    plt.plot(df_raw["time"], df_raw["az"], label="Acceleration Z")
    plt.legend(); plt.xlabel("Time (s)"); plt.ylabel("Acceleration (m/s^2)")
    plt.title("Raw Acceleration Data")
    plt.tight_layout()
    raw_fig = f"raw_accel_xyz.png"
    plt.savefig(raw_fig); plt.close()
    report_md += ["## Raw Acceleration Data (X, Y, Z)", f"![]({raw_fig})\n"]
except Exception as e:
    report_md += ["## Raw Acceleration Data (Missing)\n"]

# --- 2. Filtered/Trimmed Data Example ---
try:
    df_filt = pd.read_csv("part2_trimmed/trimmed_smooth_trial1.csv")
    plt.figure(figsize=(8,4))
    plt.plot(df_filt["time"], df_filt["az_smooth"], label="Smoothed Accel Z")
    plt.xlabel("Time (s)"); plt.ylabel("Acceleration (m/s^2)")
    plt.title("Filtered Vertical Acceleration")
    plt.legend(); plt.tight_layout()
    filt_fig = "filtered_az.png"
    plt.savefig(filt_fig); plt.close()
    report_md += ["## Filtered/Trimmed Vertical Acceleration Data", f"![]({filt_fig})\n"]
except Exception as e:
    report_md += ["## Filtered/Trimmed Vertical Acceleration Data (Missing)\n"]

# --- 3. FFT Analysis with Labeled Peak ---
try:
    # Example trial, adjust for averaged data if desired
    df_fft = pd.read_csv("part2_trimmed/trimmed_smooth_trial1.csv")
    t = df_fft['time'].values
    az = df_fft['az_smooth'].values
    dt = t[1] - t[0]
    n = len(az)
    fft_vals = abs(np.fft.fft(az-np.mean(az)))
    fft_freqs = np.fft.fftfreq(n, d=dt)
    pos_mask = (fft_freqs > 0)
    fft_peak = fft_freqs[pos_mask][np.argmax(fft_vals[pos_mask])]

    plt.figure(figsize=(8,4))
    plt.plot(fft_freqs[pos_mask], fft_vals[pos_mask])
    plt.xlabel("Frequency (Hz)"); plt.ylabel("Amplitude")
    plt.title("FFT Spectrum (Acceleration)")
    plt.axvline(fft_peak, color='r', linestyle='--', label=f"Peak: {fft_peak:.3f} Hz")
    plt.legend(); plt.tight_layout()
    fft_fig = "fft_spectrum.png"
    plt.savefig(fft_fig); plt.close()
    report_md += ["## FFT Analysis of Acceleration Data", f"![]({fft_fig})\n"]
except Exception as e:
    report_md += ["## FFT Analysis (Missing)\n"]

# --- 4. Summary Table of ω_d, k, ζ (from ultimate_summary.csv) ---
try:
    summary = pd.read_csv("part2_results/ultimate_summary.csv")
    report_md += ["## Summary of Key Parameters"]
    report_md += [summary.to_markdown()]
except Exception as e:
    report_md += ["## Summary of Key Parameters (Missing)\n"]

# --- 5. Spring Extension Comparison Table ---
try:
    ext_manual = "[Measured value here]"  # Manually fill actual measured value in cm or m
    ext_num = "[Calculated from part1_positions/position_trial1.csv or summary]"
    ext_reg = "[Calculated from regression, use fitted_AB.csv or summary]"
    report_md += ["## Spring Extension at Equilibrium (Comparison)",
                  "| Method | Extension |",
                  "|--------|-----------|",
                  f"| Manual (Ruler) | {ext_manual} |",
                  f"| Numerical Integration | {ext_num} |",
                  f"| Regression | {ext_reg} |"]
except Exception as e:
    report_md += ["## Spring Extension Comparison (Missing)\n"]

# --- 6. Regression Results for A, B, Initial Position/Velocity ---
try:
    ab_df = pd.read_csv("part1_results/fitted_AB.csv")
    report_md += ["## Regression Results (A, B, Init Pos/Vel)",
                  ab_df.to_markdown()]
except Exception as e:
    report_md += ["## Regression Results (Missing)\n"]

# --- 7. Experimental Position vs Fitted Model (Overlay Plot) ---
try:
    overlay_fig = "part2_results/exp_fit_overlay.png"
    if os.path.exists(overlay_fig):
        report_md += ["## Overlay: Experimental Data and Analytical Model", f"![]({overlay_fig})\n"]
except Exception as e:
    report_md += ["## Overlay Plot (Missing)\n"]

# --- 8. ODE Simulated vs Experimental/Analytical ---
try:
    ode_fig = "part1_results/position_trial1_ODEcomp.png"
    if os.path.exists(ode_fig):
        report_md += ["## ODE Simulation vs Experiment vs Analytical Model", f"![]({ode_fig})\n"]
except Exception as e:
    report_md += ["## ODE Comparison Plot (Missing)\n"]

# --- Final markdown write ---
with open("submission_report.md", "w") as f:
    f.write("\n\n".join(report_md))

# --- Generate PDF with Pandoc ---
os.system("pandoc submission_report.md -o submission_report.pdf")

print("\nPDF report generated: submission_report.pdf")
