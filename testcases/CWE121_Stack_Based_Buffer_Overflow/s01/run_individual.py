import os
import subprocess

successful_runs = []
failed_runs = []

def run_wasm_file(file_path):
    wasmtime_path = "/Users/hh/git/wasmtime/target/debug/wasmtime"
    try:
        subprocess.run([wasmtime_path, file_path, "--allow-unknown-exports"], check=True, capture_output=True, text=True)
        print(f"Successfully ran {file_path}")
        if "rand" not in file_path:
            successful_runs.append(file_path)
    except subprocess.CalledProcessError as e:
        print(f"    Failed to run {file_path}")
        # print("Error Output:")
        # print(e.stderr)
        if "out of bounds" in e.stderr:
            print("        The error contains 'out of bounds'")
        else:
            failed_runs.append(file_path)

def main():
    for filename in os.listdir('.'):
        if filename.endswith('.wasm'):
            run_wasm_file(filename)
    print("Successfully ran the following files without 'rand' in their names:")
    for file in successful_runs:
        print(file)
    print("Failed to run the following files without 'out of bounds' :")
    for file in failed_runs:
        print(file)
        
if __name__ == '__main__':
    main()
