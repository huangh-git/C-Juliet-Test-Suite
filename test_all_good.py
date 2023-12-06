import os
import subprocess
import argparse
from datetime import datetime
import sys

test_cases = [
    "CWE121_Stack_Based_Buffer_Overflow",
    "CWE122_Heap_Based_Buffer_Overflow",
    "CWE124_Buffer_Underwrite",
    "CWE126_Buffer_Overread",
    "CWE127_Buffer_Underread",
    "CWE476_NULL_Pointer_Dereference",
]

def run_make_clean(args):
    try:
        subprocess.run(['make', 'clean', '-s', f'SUFFIX={args.suffix}'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running 'make clean': {e}")

def run_make_all_good(args):
    try:
        subprocess.run(['make', 'all', '-s', f'CC_PATH={args.cc}', f'WASI_LIBC_PATH={args.wasi_libc}',
                        f'WASI_SDK_PATH={args.wasi_sdk}', f'SUFFIX={args.suffix}', '-j8'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running 'make all': {e}")
        # sys.exit(1)

def run_all_good_script(args):
    try:
        subprocess.run(['python3', 'run_all_good.py', f'{args.wasmtime}', f'{args.suffix}'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running 'run_all_good.py': {e}")
        sys.exit()

def deal_path(path):
    if not os.path.exists(path):
        print(f"{path} does not exist")
        sys.exit()
    if not os.path.isabs(path):
        return os.path.join(os.getcwd(), path)
    return path

def main():
    parser = argparse.ArgumentParser(description='Script description')
    current_path = os.getcwd()
    # parser.add_argument('--log', default='output.log', help='Path to the log file.')
    parser.add_argument('--wasmtime', default="../wasmtime/target/debug/wasmtime", help='Path to the wasmtime')
    parser.add_argument('--suffix', default='.wasm', help='Path to the target directory.')
    parser.add_argument('--cc', default='../llvm-project-memswasm/build', help='Path to clang build')
    parser.add_argument('--wasi_libc', default='../ms-wasi-libc/sysroot', help='Path to wasi libc.')
    parser.add_argument('--wasi_sdk', default='../ms-wasi-sdk', help='Path to wasi sdk.')
    parser.add_argument('--run_option', default="", help='wasmtime run option, like --store-check-only')
    parser.add_argument('--no_remake', default=False, help='do make clean and make again')

    args = parser.parse_args()
    args.wasmtime = deal_path(args.wasmtime)
    args.cc = deal_path(args.cc)
    args.wasi_libc = deal_path(args.wasi_libc)
    args.wasi_sdk = deal_path(args.wasi_sdk)

    with open('./total_good.txt', 'a') as file:
        file.write("\n" + "\n" + "//////////////////////////////"+ datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "//////////////////////////////" + "\n")
        file.write(f"Test cases with violation.\n")
        file.write(f"Run option: {args.run_option}\n")
        file.write(f"suffix: {args.suffix}\n")
        file.write("\n")

    for case in test_cases:
        os.chdir(os.path.join("testcases", case))
        print("////////////////////////////////////////////////////////////////////////////" + case + "////////////////////////////////////////////////////////////////////////////")
        
        #make clean
        if not args.no_remake:
            print("==================================making clean=================================")
            run_make_clean(args)
            print("====================================building====================================")
            run_make_all_good(args)
        print("==================================running tests==================================")
        run_all_good_script(args)

        os.chdir("../..")

if __name__ == "__main__":
    main()
