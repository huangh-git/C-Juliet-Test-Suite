CC_PATH?=/Users/hh/git/llvm-project-memswasm/build
WASI_LIBC_PATH?=/Users/hh/git/ms-wasi-libc/sysroot
WASI_SDK_PATH?=/Users/hh/git/ms-wasi-sdk/
SUFFIX?=.wasm

# 子目录列表
ALL_SUBDIRS := $(wildcard */.)
EXCLUDE = s03/. 
SUBDIRS = $(filter-out $(EXCLUDE), $(ALL_SUBDIRS))


# 默认目标
all:
	for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir all CC_PATH=$(CC_PATH) WASI_LIBC_PATH=$(WASI_LIBC_PATH) WASI_SDK_PATH=$(WASI_SDK_PATH) SUFFIX=$(SUFFIX); \
	done

individuals: 
	for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir individuals CC_PATH=$(CC_PATH) WASI_LIBC_PATH=$(WASI_LIBC_PATH) WASI_SDK_PATH=$(WASI_SDK_PATH) SUFFIX=$(SUFFIX); \
	done

# 清理目标
clean:
	for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir clean SUFFIX=$(SUFFIX); \
	done
