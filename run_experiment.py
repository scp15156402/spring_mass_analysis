import subprocess
import os

scripts_folder = os.path.join(os.getcwd(), "scripts")

os.chdir(scripts_folder)
print("Entered scripts folder")

# Run Part 2 pipeline
print("\n========== Running: run_all_part2.py ==========")
result = subprocess.run(["python", "run_all_part2.py"], capture_output=True, text=True)
print(result.stdout)
if result.returncode != 0:
    print(f"Error in run_all_part2.py:\n{result.stderr}")
    exit(1)  # Stop if any error

# Run Part 1 pipeline
print("\n========== Running: run_all_part1.py ==========")
result = subprocess.run(["python", "run_all_part1.py"], capture_output=True, text=True)
print(result.stdout)
if result.returncode != 0:
    print(f"Error in run_all_part1.py:\n{result.stderr}")
    exit(1)

print("\nAll scripts completed successfully.")
