import os
import subprocess
import argparse

test_cases = [
    "CWE121_Stack_Based_Buffer_Overflow",
    "CWE122_Heap_Based_Buffer_Overflow",
    "CWE124_Buffer_Underwrite",
    "CWE126_Buffer_Overread",
    "CWE127_Buffer_Underread",
]

def run_make_clean(args):
    try:
        subprocess.run(['make', 'clean', f'SUFFIX={args.suffix}'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running 'make clean': {e}")

def run_make_all_good(args):
    try:
        subprocess.run(['make', 'all', f'CC_PATH={args.cc}', f'WASI_LIBC_PATH={args.wasi_libc}',
                        f'WASI_SDK_PATH={args.wasi_sdk}', f'SUFFIX={args.suffix}', '-j8'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running 'make all': {e}")
        # sys.exit(1)

def run_all_good_script(args):
    try:
        subprocess.run(['python3', 'run_all_good.py', f'{args.wasmtime}', f'{args.suffix}'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running 'run_all_good.py': {e}")

def main():
    parser = argparse.ArgumentParser(description='Script description')
    # parser.add_argument('--log', default='output.log', help='Path to the log file.')
    parser.add_argument('--wasmtime', default='/home/hh/wasmtime/target/debug/wasmtime', help='Path to the wasmtime')
    parser.add_argument('--suffix', default='.wasm', help='Path to the target directory.')
    parser.add_argument('--cc', default='/home/hh/llvm-project-memswasm/build', help='Path to clang build')
    parser.add_argument('--wasi_libc', default='/home/hh/ms-wasi-libc/sysroot', help='Path to wasi libc.')
    parser.add_argument('--wasi_sdk', default='/home/hh/ms-wasi-sdk', help='Path to wasi sdk.')
    parser.add_argument('--no_remake', default=False, help='do make clean and make again')

    args = parser.parse_args()

    for case in test_cases:
        os.chdir(os.path.join("testcases", case))
        #make clean
        if not args.no_remake:
            print("make clean")
            run_make_clean(args)
            print("make all")
            run_make_all_good(args)
        print("run all good")
        run_all_good_script(args)

        os.chdir("../..")

if __name__ == "__main__":
    main()
