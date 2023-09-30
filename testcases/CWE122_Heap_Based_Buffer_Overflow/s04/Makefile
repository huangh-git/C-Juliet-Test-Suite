CC_PATH?=/Users/hh/git/llvm-project-memswasm/build
WASI_LIBC_PATH?=/Users/hh/git/ms-wasi-libc/sysroot
WASI_SDK_PATH?=/Users/hh/git/ms-wasi-sdk/build
SUFFIX ?= .wasm
CC=$(CC_PATH)/bin/clang
LD=$(CC_PATH)/bin/wasm-ld#ld
# CPP=/usr/bin/g++
DEBUG=#-g
CFLAGS=-c -DOMITBAD --target=wasm32-unknown-wasi -ffreestanding --sysroot $(WASI_LIBC_PATH) -x c #-std=c89
LFLAGS=-m wasm32 -error-limit=0 --no-entry --export-all -L$(WASI_LIBC_PATH)/lib/wasm32-wasi -lc -lc $(WASI_SDK_PATH)/compiler-rt/lib/wasi/libclang_rt.builtins-wasm32.a#-lpthread -lm -Wl,--no-entry -Wl,--export-all  -flavor wasm -m wasm32 
INDIVIDUALS_FLAG=-DOMITGOOD --target=wasm32-unknown-wasi -ffreestanding --sysroot $(WASI_LIBC_PATH) -x c -L$(WASI_LIBC_PATH)/lib/wasm32-wasi -lc -Wl,--no-entry -Wl,--export-all
INCLUDE_MAIN=-DINCLUDEMAIN

INCLUDES=-I../../../testcasesupport -I$(WASI_LIBC_PATH)/include

MAIN=new_main_linux.cpp
MAIN_OBJECT=$(MAIN:.cpp=.o)

C_SUPPORT_PATH=../../../testcasesupport/
C_SUPPORT_FILES=$(C_SUPPORT_PATH)io.c #$(C_SUPPORT_PATH)std_thread.c
C_SUPPORT_OBJECTS=io.o #std_thread.o
FILTER_OUT=$(wildcard CWE*w32*.c*) $(wildcard CWE*wchar_t*.c*) $(wildcard CWE*socket*.c*) $(wildcard CWE*fscanf*.c*) $(wildcard CWE*fgets*.c*)

# only grab the .c files without "w32" or "wchar_t" in the name
C_SOURCES=$(filter-out $(FILTER_OUT),$(wildcard CWE*.c))
C_OBJECTS=$(C_SOURCES:.c=.o)

# only grab the .cpp files without "w32" or "wchar_t" in the name
CPP_SOURCES=$(filter-out $(FILTER_OUT),$(wildcard CWE*.cpp))

SIMPLES=$(filter-out $(FILTER_OUT), $(wildcard CWE*0.c*) $(wildcard CWE*1.c*) $(wildcard CWE*2.c*) $(wildcard CWE*3.c*) $(wildcard CWE*4.c*))         $(filter-out $(FILTER_OUT), $(wildcard CWE*5.c*) $(wildcard CWE*6.c*) $(wildcard CWE*7.c*) $(wildcard CWE*8.c*) $(wildcard CWE*9.c*))
SIMPLES_C=$(filter-out $(CPP_SOURCES), $(SIMPLES))

LETTEREDS=$(filter-out $(FILTER_OUT), $(wildcard CWE*a.c*))
LETTEREDS_C=$(subst a.,.,$(filter-out $(CPP_SOURCES), $(LETTEREDS)))

GOOD1S=$(filter-out $(FILTER_OUT), $(wildcard CWE*_good1.cpp))
BADS=$(subst _good1.,_bad.,$(GOOD1S))

INDIVIDUALS_C=$(addsuffix $(SUFFIX), $(sort $(subst .c,,$(SIMPLES_C) $(LETTEREDS_C))))

OBJECTS=$(MAIN_OBJECT) $(C_OBJECTS) $(C_SUPPORT_OBJECTS)

# TARGET is the only line in this file specific to the CWE
TARGET=CWE122_s04_good$(SUFFIX)
all: $(TARGET)

individuals: $(INDIVIDUALS_C)

$(INDIVIDUALS_C): $(C_SUPPORT_FILES)
	$(CC) $(INCLUDES) $(INCLUDE_MAIN) -o $@ $(wildcard $(subst $(SUFFIX),,$@)*.c) $(C_SUPPORT_FILES) $(INDIVIDUALS_FLAG)

$(TARGET) : $(OBJECTS)
	$(LD) $(LFLAGS) $(OBJECTS) -o $(TARGET)

$(C_OBJECTS) : %.o:%.c 
	$(CC) $(CFLAGS) $(INCLUDES) $^ -o $@

$(C_SUPPORT_OBJECTS) : $(C_SUPPORT_FILES)
	$(CC) $(CFLAGS) $(INCLUDES) $(C_SUPPORT_PATH)$(@:.o=.c) -o $@

$(MAIN_OBJECT) : $(MAIN)
	$(CC) $(CFLAGS) $(INCLUDES) $(MAIN) -o $@

clean:
	rm -rf *.o *.out *$(SUFFIX) $(TARGET)
