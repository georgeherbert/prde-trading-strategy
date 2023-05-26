import subprocess
from multiprocessing import Pool

def run_experiment(params):
    k, f = params
    command = ["python3", "_prde_zip_experiment.py", str(k), str(f)]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f"Error running command {' '.join(command)}: {stderr.decode()}")

    print(f"Output for command {' '.join(command)}: {stdout.decode()}")

if __name__ == "__main__":
    k_values = range(4, 21, 2)
    f_values = [0.0, 0.4, 0.8, 1.2, 1.6, 2.0]

    # Create a list of all combinations of k_values and f_values
    experiments = [(k, f) for k in k_values for f in f_values]

    # Create a multiprocessing Pool
    with Pool() as p:
        p.map(run_experiment, experiments)
