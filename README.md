# ME225 - Numerical Analysis (Autumn 2025-26)
### Professor Abhishek Gupta
Department of Mechanical Engineering, IIT Bombay

## Project: Spring-Mass System Data Analysis

This repository contains the codebase and workflow for the spring-mass experimental data analysis project conducted as part of ME225 - Numerical Analysis. The project was done in Autumn Semester 2025-26 under the guidance of Prof. Abhishek Gupta, Department of Mechanical Engineering.

---

### **Project Overview**

This project automates the analysis of spring-mass oscillation experiments using Python. It processes raw acceleration data, applies filters and FFTs, estimates system parameters (mass, spring constant, damping ratio, natural frequency), performs regression fits, and generates a complete, publication-ready PDF report from results. The pipeline handles both experimental trials and validation with analytical and numerical (ODE) models.

#### **Major Components:**
- Data cleaning (trimming, smoothing)
- Double integration for displacement calculation
- Frequency analysis (FFT) for natural frequency estimation
- Parameter regression (A, B, initial position/velocity estimation)
- Numerical ODE simulation for system response
- Automated submission report generation (Markdown/PDF) with plots and analysis

---

### **Directory Structure**

```
spring_mass_analysis/
│
├── part1_raw/           # Raw datasets for part 1
├── part1_positions/     # Trimmed/double integrated position data from part 1
├── part1_results/       # Regression, ODE, fit plots/results from part 1
│
├── part2_raw/           # Raw datasets for part 2
├── part2_trimmed/       # Filtered/trimmed acceleration data (part 2)
├── part2_position/      # Position data after integration (part 2)
├── part2_results/       # FFT, summary, fit results, overlays for part 2
│
├── scripts/             # All Python scripts for each processing stage
│
├── run_all.py           # Master script: runs all data analysis end-to-end
├── generate_and_download_pdf.py # Auto-generates ready-to-submit report
├── README.md            # Project documentation (this file)
```

---

### **Key Code Files**

- `run_all.py`  
  *Runs all numbered scripts in sequence for a full project workflow (data processing, analysis, regression, report generation).*

- `scripts/part2_*`  
  *Scripts for Part 2: trimming, smoothing, integration, FFT, parameter extraction, ODE simulation.*

- `scripts/part1_trim_smooth.py`  
  *Processes raw Part 1 files and computes position.*

- `scripts/part1_regression.py`  
  *Fits the analytical model to experimental position data, extracts A/B/initial conditions.*

- `scripts/part1_ode_simulation.py`  
  *Runs a numerical simulation of the spring-mass system and overlays results.*

- `generate_and_download_pdf.py`  
  *Automatically generates a Markdown submission report and converts it to PDF, embedding all key results, tables, and plots.*

---

### **How to Use**

1. **Place raw CSV files in their respective `part1_raw` and `part2_raw` folders.**
2. **Run the project end-to-end:**
   ```
   python run_all.py
   ```
3. **Generate the submission PDF:**
   ```
   python generate_and_download_pdf.py
   ```
   > This creates `submission_report.pdf` with all required analysis/results for direct submission.

---

