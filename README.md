# C-Juliet-Test-Suite
C Juliet Test Suite for WebAssembly test.
We use CWE121, CWE122, CWE124, CWE126, CWE127 and CWE476 to test MemS-Wasm spatial safety.
## Folder Location
All the projects that were cloned from Git are located in the same folder. Like the following.
```
.
├── C-Juliet-Test-Suite
├── llvm-project-memswasm
├── ms-wasi-libc
├── ms-wasi-sdk
├── wasi-sdk
└── wasmtime
```
## Prepare compilers
1. Build compile [MemS-Wasm compiler](https://github.com/huangh-git/llvm-project-memswasm) 
2. Build Standard WebAssembly compiler from [wasi-sdk](https://github.com/WebAssembly/wasi-sdk). And we use wasi-sdk-16 because it corresponds to llvm version 14.
```
git clone https://github.com/WebAssembly/wasi-sdk.git
git checkout tags/wasi-sdk-16     
git submodule update --init
NINJA_FLAGS=-v make package
```


## Prepare wasmtime
You need to prepare [wasmtime](https://github.com/huangh-git/wasmtime) virtual machine for MemS-Wasm.
## How to Use
Just `./run.sh`
For test cases without memory vulnerabilities, their results are in `total_good.txt`. For test cases with memory vulnerabilities, their results are in `total_bad.txt`.
