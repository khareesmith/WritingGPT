import subprocess
from tqdm import tqdm

inputs = "A review of Mcdonalds\nfast food, healthy vs unhealthy, cheap\nmusic\nsports"
num_runs = 25
script_name = "main.py"

# The tqdm function takes an iterable and returns an iterator that updates the progress bar each time a value is requested.
for _ in tqdm(range(num_runs), desc="Running script", unit="run"):
    process = subprocess.run(["python", script_name], input=inputs, text=True)
    if process.returncode != 0:
        print(f"Script {script_name} failed with return code: {process.returncode}")
        break