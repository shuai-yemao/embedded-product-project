# ============================================
# 嵌入式固件单元测试 Makefile
# ============================================

# 编译器
CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -I../include

# 测试文件
TEST_SRC = test_example.c
TEST_OBJ = $(TEST_SRC:.c=.o)
TEST_BIN = test_example

# 源文件目录
SRC_DIR = ../src
INCLUDE_DIR = ../include

# 测试目录
TEST_DIR = .
BUILD_DIR = build

# 默认目标
all: $(BUILD_DIR)/$(TEST_BIN)

# 创建构建目录
$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

# 编译测试文件
$(BUILD_DIR)/$(TEST_OBJ): $(TEST_SRC) | $(BUILD_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

# 链接测试文件
$(BUILD_DIR)/$(TEST_BIN): $(BUILD_DIR)/$(TEST_OBJ)
	$(CC) $^ -o $@

# 运行测试
test: $(BUILD_DIR)/$(TEST_BIN)
	./$(BUILD_DIR)/$(TEST_BIN)

# 清理
clean:
	rm -rf $(BUILD_DIR)

# 代码覆盖率（需要 gcov）
coverage: CFLAGS += --coverage
coverage: clean test
	gcov $(BUILD_DIR)/$(TEST_OBJ)

# 静态分析（需要 cppcheck）
static-analysis:
	cppcheck --enable=all --std=c99 $(SRC_DIR) $(TEST_DIR)

# 帮助
help:
	@echo "可用目标:"
	@echo "  all          - 编译测试"
	@echo "  test         - 运行测试"
	@echo "  clean        - 清理构建文件"
	@echo "  coverage     - 生成代码覆盖率报告"
	@echo "  static-analysis - 运行静态分析"
	@echo "  help         - 显示此帮助信息"

.PHONY: all test clean coverage static-analysis help
