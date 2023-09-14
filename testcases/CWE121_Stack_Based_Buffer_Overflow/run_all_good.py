import os
import subprocess
import sys

wasmtime_path = '/Users/hh/git/wasmtime/target/debug/wasmtime'
if len(sys.argv) - 1 > 0:
    wasmtime_path = sys.argv[1]

# 遍历当前目录下的所有子目录
for subdir, _, _ in os.walk('.'):
    if subdir == '.':  # 跳过当前目录
        continue
    
    # 改变当前工作目录到子目录
    os.chdir(subdir)
    
    # 执行 'make all' 命令
    try:
        subprocess.run(['make', 'all'], check=True)
    except subprocess.CalledProcessError:
        print(f"Make all failed in directory: {subdir}")
        sys.exit()
    
    # 执行 'wasmtime dirname.wasm' 命令
    wasm_file = f"CWE121_{os.path.basename(subdir)}_good.wasm"
    try:
        subprocess.run([wasmtime_path, wasm_file, '--allow-unknown-exports'], check=True)
    except subprocess.CalledProcessError:
        print(f"Wasmtime failed for wasm file: {wasm_file}\n")
        sys.exit()
    
    # 改回到原始目录
    os.chdir('..')
