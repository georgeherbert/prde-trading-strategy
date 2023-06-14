import subprocess
from multiprocessing import Pool

def run_experiment(params):
    f, val = params
    command = ["python3", "_prjade_prde_experiment.py", str(f), str(val)]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f"Error running command {' '.join(command)}: {stderr.decode()}")

    print(f"Output for command {' '.join(command)}: {stdout.decode()}")

if __name__ == "__main__":
    # f_values = range(1, 2)  # 0, 1, 2
    f_values = [2]
    val_values = range(0, 20)  # 0 to 19 (inclusive)

    # Create a list of all combinations of f_values and val_values
    experiments = [(f, val) for f in f_values for val in val_values]

    # Create a multiprocessing Pool
    with Pool() as p:
        p.map(run_experiment, experiments)
