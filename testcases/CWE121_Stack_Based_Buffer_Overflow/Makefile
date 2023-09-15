# 子目录列表
SUBDIRS := $(wildcard */.)

# 默认目标
all:
	for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir all; \
	done

individuals: 
	for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir individuals; \
	done

# 清理目标
clean:
	for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir clean; \
	done
