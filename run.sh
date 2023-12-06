
echo "Running the all test cases without vulnerabilities for standard WebAssembly ..."
python3 test_all_good.py --wasmtime ../wasmtime/target/debug/wasmtime --suffix .good-raw-wasm --cc ../wasi-sdk/build/install/opt/wasi-sdk/ --wasi_libc ../wasi-sdk/build/install/opt/wasi-sdk/share/wasi-sysroot --wasi_sdk ../wasi-sdk/build/install/opt/wasi-sdk/lib/clang/14.0.4/lib/wasi/
echo "Finished, the result is in total_good.txt"

echo "Running the all test cases with vulnerabilities for standard WebAssembly ..."
python3 test_all_bad.py --wasmtime ../wasmtime/target/debug/wasmtime --suffix .bad-raw-wasm --cc ../wasi-sdk/build/install/opt/wasi-sdk/ --wasi_libc ../wasi-sdk/build/install/opt/wasi-sdk/share/wasi-sysroot/
echo "Finished, the result is in total_bad.txt"

echo "Running the all test cases without vulnerabilities for MemS-Wasm ..."
python3 test_all_good.py --wasmtime ../wasmtime/target/debug/wasmtime --suffix .good-mems-wasm --cc ../llvm-project-memswasm/build --wasi_libc ../ms-wasi-libc/sysroot --wasi_sdk ../ms-wasi-sdk/ 
echo "Finished, the result is in total_good.txt"

echo "Running the all test cases with vulnerabilities for MemS-Wasm full check ..."
python3 test_all_bad.py  --suffix .bad-mems-wasm --cc ../llvm-project-memswasm/build --wasi_libc ../ms-wasi-libc/sysroot --wasi_sdk ../ms-wasi-sdk/
echo "Finished, the result is in total_bad.txt"

echo "Running the all test cases with vulnerabilities for MemS-Wasm upper check only ..."
python3 test_all_bad.py  --suffix .bad-mems-wasm --cc ../llvm-project-memswasm/build --wasi_libc ../ms-wasi-libc/sysroot --wasi_sdk ../ms-wasi-sdk/ --run_option="--upper-check-only" --no_remake=True
echo "Finished, the result is in total_bad.txt"


echo "Running the all test cases with vulnerabilities for MemS-Wasm store check only ..."
python3 test_all_bad.py  --suffix .bad-mems-wasm --cc ../llvm-project-memswasm/build --wasi_libc ../ms-wasi-libc/sysroot --wasi_sdk ../ms-wasi-sdk/ --run_option="--store-check-only" --no_remake=True
echo "Finished, the result is in total_bad.txt"
