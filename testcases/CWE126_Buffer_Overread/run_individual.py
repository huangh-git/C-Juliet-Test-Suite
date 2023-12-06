import os
import subprocess
import sys
from datetime import datetime
import concurrent.futures
import multiprocessing

ignore_list = [
    "./s01/CWE126_Buffer_Overread__CWE170_char_strncpy_03.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_loop_04.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_memcpy_05.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_memcpy_16.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_strncpy_17.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_strncpy_16.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_loop_07.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_memcpy_02.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_strncpy_02.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_loop_14.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_strncpy_01.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_loop_03.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_loop_15.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_memcpy_08.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_strncpy_15.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_loop_05.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_memcpy_11.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_strncpy_09.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_strncpy_06.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_memcpy_12.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_strncpy_08.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_strncpy_11.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_loop_10.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_strncpy_13.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_strncpy_14.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_loop_08.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_strncpy_12.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_loop_13.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_memcpy_06.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_loop_17.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_strncpy_18.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_memcpy_07.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_loop_11.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_memcpy_13.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_loop_18.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_memcpy_04.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_strncpy_05.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_memcpy_01.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_strncpy_10.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_loop_02.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_strncpy_04.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_memcpy_03.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_memcpy_10.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_memcpy_09.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_loop_01.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_loop_09.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_memcpy_14.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_loop_12.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_strncpy_07.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_memcpy_18.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_loop_06.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_loop_16.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_memcpy_17.wasm",
    "./s01/CWE126_Buffer_Overread__CWE170_char_memcpy_15.wasm"
]

# Initialize arrays to store the results
successful_runs = []
timeout_runs = []
failed_runs = []
undetected = []
dataCnt = {
    'cnt_successful': 0,
    'cnt_timeout': 0,
    'cnt_failed_abnormal': 0,
    'cnt_total': 0
}

wasmtime_path = '/Users/hh/git/wasmtime/target/debug/wasmtime'
runOption = ""
maxWorkNum = multiprocessing.cpu_count()*1/4
if len(sys.argv) - 1 > 0:
    wasmtime_path = sys.argv[1]
if len(sys.argv) - 2 > 0:
    suffix = sys.argv[2]
if len(sys.argv) - 3 > 0:
    runOption = sys.argv[3]
if len(sys.argv) - 4 > 0:
    maxWorkNum = int(sys.argv[4])

def run_executable(filename):
    try:
        result = subprocess.run([wasmtime_path, filename, '--allow-unknown-exports', runOption], check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=20)
        print(f"++++Successfully ran: {filename}")
        # if os.path.join(subdir, filename) in ignore_list:
        #     print("ignore this file, because in wasm, the initial value in memory is 0")
        return 'success', filename
    except subprocess.TimeoutExpired:
        print(f"====Timeout while running: {filename}")
        return 'timeout', filename
    except subprocess.CalledProcessError as e:
        if 'out of bounds' not in str(e.stderr):
            print("without 'out of bounds'")
            return 'fail', filename
        print(f"----The out-of-bounds access was successfully detected: {filename}")
    return '', ''


# Loop through each subdirectory in the current directory
for subdir, _, _ in os.walk('.'):
    if subdir == '.':
        continue  # Skip the current directory

    # Change to the subdirectory
    os.chdir(subdir)

    executable_files = [f for f in os.listdir('.') if f.endswith(suffix) and "_good" not in f]
    dataCnt['cnt_total'] += len(executable_files)
    # 使用线程池执行
    with concurrent.futures.ThreadPoolExecutor(max_workers=maxWorkNum) as executor:
        results = executor.map(run_executable, executable_files)
        for status, filename in results:
            if status == 'success':
                successful_runs.append(filename)
            elif status == 'timeout':
                timeout_runs.append(filename)
            elif status == 'fail':
                failed_runs.append(filename)
    # Run each .wasm file in the subdirectory
    # for filename in os.listdir('.'):
    #     if filename.endswith(suffix) and "_good" not in filename:
    #         dataCnt['cnt_total'] += 1
            
    #         try:
    #             result = subprocess.run([wasmtime_path, filename, '--allow-unknown-exports', runOption], check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10)
    #             print(f"++++Successfully ran: {os.path.join(subdir, filename)}")
    #             print(result.stdout)
    #             # if os.path.join(subdir, filename) in ignore_list:
    #             #     print("ignore this file, because in wasm, the initial value in memory is 0")
    #             successful_runs.append(os.path.join(subdir, filename))
    #         except subprocess.TimeoutExpired:
    #             print(f"====Timeout while running: {os.path.join(subdir, filename)}")
    #             timeout_runs.append(os.path.join(subdir, filename))
    #             # break
    #         except subprocess.CalledProcessError as e:
    #             print(f"----Failed to run: {os.path.join(subdir, filename)}")
    #             if 'out of bounds' not in str(e.stderr):
    #                 print("without 'out of bounds'")
    #                 failed_runs.append(os.path.join(subdir, filename))

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
    undetected = undetected + failed_runs + timeout_runs + successful_runs
    successful_runs=[]
    timeout_runs=[]
    failed_runs=[]

current_dir = os.path.dirname(os.path.abspath(__file__))
with open('../../total_bad.txt', 'a') as file:
    file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") +  "\n")
    file.write("current dir:" + current_dir +  ".\nsuffix: " + suffix +"\n")
    noPassCnt = 0
    for key, value in dataCnt.items():
        file.write(f"{key}\t{value}\n")
        if key != "cnt_total":
            noPassCnt += value
    file.write("can not detection:\t" + str(noPassCnt*1.0/dataCnt["cnt_total"]) + "\n")
    file.write("can detection:\t" + str(1-noPassCnt*1.0/dataCnt["cnt_total"]) + "\n")
    file.write("undetected files:\n" + undetected.__str__() + "\n")
    file.write("\n")
# Print the results
# print("Successful runs:", successful_runs)
# print("Timeout runs:", timeout_runs)
# print("Failed runs:", failed_runs)

