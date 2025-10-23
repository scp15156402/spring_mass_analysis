import subprocess

scripts = [
    "part1_trim_smooth.py",
    "part1_regression.py",
    "part1_ode_simulation.py"
]

for script in scripts:
    print(f"\nRunning: {script}")
    result = subprocess.run(['python', script], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error running {script}:\n{result.stderr}")
        break  # Stop if any script fails
    print(f"Completed: {script}\n{'-'*40}")
