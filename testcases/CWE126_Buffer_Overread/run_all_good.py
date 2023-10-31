import os
import subprocess
import sys

wasmtime_path = '/Users/hh/git/wasmtime/target/debug/wasmtime'
suffix = '.wasm'
if len(sys.argv) - 1 > 0:
    wasmtime_path = sys.argv[1]

if len(sys.argv) - 2 > 0:
    suffix = sys.argv[2]

failed_runs = []

# 遍历当前目录下的所有子目录
for subdir, _, _ in os.walk('.'):
    if subdir == '.':  # 跳过当前目录
        continue
    
    # 改变当前工作目录到子目录
    os.chdir(subdir)
    
    # 执行 'wasmtime dirname.wasm' 命令
    wasm_file = f"CWE126_{os.path.basename(subdir)}_good{suffix}"
    if not os.path.exists(wasm_file):
        os.chdir('..')
        continue
    try:
        subprocess.run([wasmtime_path, wasm_file, '--allow-unknown-exports'], check=True)
    except subprocess.CalledProcessError:
        print(f"Wasmtime failed for wasm file: {wasm_file}\n")
        failed_runs.append(wasm_file)
        sys.exit()
    
    # 改回到原始目录
    os.chdir('..')

print("failed runs:\n", failed_runs)