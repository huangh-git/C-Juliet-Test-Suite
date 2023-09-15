import os
import subprocess
import sys
from datetime import datetime

# Initialize arrays to store the results
successful_runs = []
timeout_runs = []
failed_runs = []
wasmtime_path = '/Users/hh/git/wasmtime/target/debug/wasmtime'
if len(sys.argv) - 1 > 0:
    wasmtime_path = sys.argv[1]

# Loop through each subdirectory in the current directory
for subdir, _, _ in os.walk('.'):
    if subdir == '.':
        continue  # Skip the current directory

    # Change to the subdirectory
    os.chdir(subdir)

    # Run 'make individual' command
    try:
        subprocess.run(['make', 'individuals'], check=True)
    except subprocess.CalledProcessError:
        print(f"Compilation failed in directory: {subdir}")
        os.chdir('..')  # Change back to the parent directory
        sys.exit()

    # Run each .wasm file in the subdirectory
    for filename in os.listdir('.'):
        if "_good" in filename:
            continue
        if filename.endswith('.wasm'):
            count = 0
            max_runs = 5
            while count < max_runs:
                try:
                    result = subprocess.run([wasmtime_path, filename, '--allow-unknown-exports'], check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10)
                    print(f"++++Successfully ran: {os.path.join(subdir, filename)}")
                    count += 1
                except subprocess.TimeoutExpired:
                    print(f"====Timeout while running: {os.path.join(subdir, filename)}")
                    timeout_runs.append(os.path.join(subdir, filename))
                    break
                except subprocess.CalledProcessError as e:
                    print(f"----Failed to run: {os.path.join(subdir, filename)}")
                    if 'out of bounds' not in str(e.stderr):
                        failed_runs.append(os.path.join(subdir, filename))
                    break

    # Change back to the parent directory
    os.chdir('..')
    with open("output.log", "a") as f:
        f.write(subdir + " " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") +  "\n")
        f.write("Successful runs more than five times:" + "\n\t".join(successful_runs)+"\n\n")
        f.write("Timeout runs:" + "\n\t".join(timeout_runs)+"\n\n")
        f.write("Failed runs without out of bounds trap:" + "\n\t".join(failed_runs)+"\n\n")
    successful_runs=[]
    timeout_runs=[]
    failed_runs=[]


# Print the results
# print("Successful runs:", successful_runs)
# print("Timeout runs:", timeout_runs)
# print("Failed runs:", failed_runs)

