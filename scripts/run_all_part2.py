import subprocess

# List your scripts in the order you want to run them
scripts = [
    "part2_trim_smooth.py",
    "part2_double_integration.py",
    "part2_fft_omega.py",
    "part2_k_from_omega.py",
    "part2_dampingratio.py",
    "part2_summarize_results.py"
]

for script in scripts:
    print(f"Running: {script}")
    result = subprocess.run(['python', script], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error running {script}:\n{result.stderr}")
        break  # Stop on error
    print(f"Completed: {script}\n{'-'*40}")
