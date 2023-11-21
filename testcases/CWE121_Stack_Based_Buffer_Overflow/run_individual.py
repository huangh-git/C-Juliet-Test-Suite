import os
import subprocess
import sys
from datetime import datetime

# Initialize arrays to store the results
successful_runs = []
timeout_runs = []
failed_runs = []
dataCnt = {
    'cnt_successful': 0,
    'cnt_timeout': 0,
    'cnt_failed_abnormal': 0,
    'cnt_total': 0
}

wasmtime_path = '/Users/hh/git/wasmtime/target/debug/wasmtime'
suffix = '.wasm'
runOption = ""
if len(sys.argv) - 1 > 0:
    wasmtime_path = sys.argv[1]
if len(sys.argv) - 2 > 0:
    suffix = sys.argv[2]
if len(sys.argv) - 3 > 0:
    runOption = sys.argv[3]

# Loop through each subdirectory in the current directory
for subdir, _, _ in os.walk('.'):
    if subdir == '.':
        continue  # Skip the current directory

    # Change to the subdirectory
    os.chdir(subdir)

    # Run each .wasm file in the subdirectory
    for filename in os.listdir('.'):
        if filename.endswith(suffix) and "_good" not in filename:
            dataCnt['cnt_total'] += 1 # tatal cnt in this cwe
            # max_runs = 5
            # count = max_runs
            # if "rand" in filename:
            #     count += max_runs
                
            # while count > 0:
            try:
                result = subprocess.run([wasmtime_path, filename, '--allow-unknown-exports', runOption], check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10)
                print(f"++++Successfully ran: {os.path.join(subdir, filename)}")
                # count -= 1
                # if count == 0:
                successful_runs.append(os.path.join(subdir, filename))
            except subprocess.TimeoutExpired:
                print(f"====Timeout while running: {os.path.join(subdir, filename)}")
                timeout_runs.append(os.path.join(subdir, filename))
                # break
            except subprocess.CalledProcessError as e:
                print(f"----Failed to run: {os.path.join(subdir, filename)}")
                if 'out of bounds' not in str(e.stderr):
                    print("without 'out of bounds'")
                    failed_runs.append(os.path.join(subdir, filename))
                # break

    # Change back to the parent directory
    os.chdir('..')
    with open("output.log", "a") as f:
        f.write(subdir + " " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") +  "\n")
        f.write("Successful runs more than five times:" + "\n\t".join(successful_runs)+"\n\n")
        f.write("Timeout runs:" + "\n\t".join(timeout_runs)+"\n\n")
        f.write("Failed runs without out of bounds trap:" + "\n\t".join(failed_runs)+"\n\n")
    dataCnt["cnt_failed_abnormal"] += len(failed_runs)
    dataCnt["cnt_successful"] += len(successful_runs)
    dataCnt["cnt_timeout"] += len(timeout_runs)
    successful_runs=[]
    timeout_runs=[]
    failed_runs=[]

current_dir = os.path.dirname(os.path.abspath(__file__))
with open('../../total_output.txt', 'a') as file:
    file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") +  "\n")
    file.write(current_dir +  ". run " + suffix +"\n")
    noPassCnt = 0
    for key, value in dataCnt.items():
        file.write(f"{key}\t{value}\n")
        if key != "cnt_total":
            noPassCnt += value
    file.write("can not detection:\t" + str(noPassCnt*1.0/dataCnt["cnt_total"]) + "\n")
    file.write("can detection:\t" + str(1-noPassCnt*1.0/dataCnt["cnt_total"]) + "\n")
# Print the results
# print("Successful runs:", successful_runs)
# print("Timeout runs:", timeout_runs)
# print("Failed runs:", failed_runs)

