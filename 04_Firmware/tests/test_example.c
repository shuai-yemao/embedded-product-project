/**
 * @file test_example.c
 * @brief 单元测试示例
 */

#include <stdio.h>
#include <assert.h>

/**
 * @brief 测试加法运算
 */
void test_addition(void) {
    // Arrange
    int a = 2;
    int b = 3;

    // Act
    int result = a + b;

    // Assert
    assert(result == 5);
    printf("test_addition: PASSED\n");
}

/**
 * @brief 测试减法运算
 */
void test_subtraction(void) {
    // Arrange
    int a = 10;
    int b = 4;

    // Act
    int result = a - b;

    // Assert
    assert(result == 6);
    printf("test_subtraction: PASSED\n");
}

/**
 * @brief 测试乘法运算
 */
void test_multiplication(void) {
    // Arrange
    int a = 3;
    int b = 4;

    // Act
    int result = a * b;

    // Assert
    assert(result == 12);
    printf("test_multiplication: PASSED\n");
}

/**
 * @brief 测试除法运算
 */
void test_division(void) {
    // Arrange
    int a = 10;
    int b = 2;

    // Act
    int result = a / b;

    // Assert
    assert(result == 5);
    printf("test_division: PASSED\n");
}

/**
 * @brief 测试除以零（应触发错误处理）
 */
void test_division_by_zero(void) {
    // Arrange
    int a = 10;
    int b = 0;

    // Act & Assert
    // 在实际代码中，应检查除数是否为零
    // 这里只是示例，实际测试中应避免除以零
    printf("test_division_by_zero: SKIPPED (avoid division by zero)\n");
}

/**
 * @brief 主函数
 */
int main(void) {
    printf("Running unit tests...\n\n");

    // 运行所有测试
    test_addition();
    test_subtraction();
    test_multiplication();
    test_division();
    test_division_by_zero();

    printf("\nAll tests passed!\n");

    return 0;
}
