import os
import subprocess
import sys

successful_runs = []
failed_runs = []
timeout_runs = []
wasmtime_path = "/Users/hh/git/wasmtime/target/debug/wasmtime"
if len(sys.argv) - 1 > 0:
    wasmtime_path = sys.argv[1]

def run_wasm_file(file_path):
    try:
        subprocess.run([wasmtime_path, file_path, "--allow-unknown-exports"], check=True, text=True, stderr=subprocess.PIPE, timeout=10)
        print(f"Successfully ran {file_path}")
        if "rand" not in file_path:
            successful_runs.append(file_path)
    except subprocess.TimeoutExpired:
        print("The subprocess timed out.")
        timeout_runs.append(file_path)
    except subprocess.CalledProcessError as e:
        print(f"----Failed to run {file_path}")
        # print("Error Output:")
        # print(e.stderr)
        if "out of bounds" in e.stderr:
            print("--------The error contains 'out of bounds'")
        else:
            failed_runs.append(file_path)

def main():
    for filename in os.listdir('.'):
        if filename.endswith('.wasm'):
            run_wasm_file(filename)
    print("\n\nSuccessfully ran the following files without 'rand' in their names:")
    for file in successful_runs:
        print(f"\t{file}")
    print("Failed to run the following files without 'out of bounds' :")
    for file in failed_runs:
        print(f"\t{file}")
    print("Timeout to run the following files without:")
    for file in timeout_runs:
        print(f"\t{file}")
        
if __name__ == '__main__':
    main()
