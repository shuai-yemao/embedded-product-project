"""
单元测试示例
"""

import pytest


def test_addition():
    """测试加法运算"""
    # Arrange
    a = 2
    b = 3

    # Act
    result = a + b

    # Assert
    assert result == 5


def test_subtraction():
    """测试减法运算"""
    # Arrange
    a = 10
    b = 4

    # Act
    result = a - b

    # Assert
    assert result == 6


def test_multiplication():
    """测试乘法运算"""
    # Arrange
    a = 3
    b = 4

    # Act
    result = a * b

    # Assert
    assert result == 12


def test_division():
    """测试除法运算"""
    # Arrange
    a = 10
    b = 2

    # Act
    result = a / b

    # Assert
    assert result == 5.0


def test_division_by_zero():
    """测试除以零"""
    # Arrange
    a = 10
    b = 0

    # Act & Assert
    with pytest.raises(ZeroDivisionError):
        a / b


class TestStringOperations:
    """字符串操作测试类"""

    def test_string_concatenation(self):
        """测试字符串连接"""
        # Arrange
        str1 = "Hello"
        str2 = "World"

        # Act
        result = f"{str1} {str2}"

        # Assert
        assert result == "Hello World"

    def test_string_uppercase(self):
        """测试字符串大写"""
        # Arrange
        text = "hello"

        # Act
        result = text.upper()

        # Assert
        assert result == "HELLO"

    def test_string_lowercase(self):
        """测试字符串小写"""
        # Arrange
        text = "HELLO"

        # Act
        result = text.lower()

        # Assert
        assert result == "hello"


class TestListOperations:
    """列表操作测试类"""

    def test_list_append(self):
        """测试列表追加"""
        # Arrange
        lst = [1, 2, 3]

        # Act
        lst.append(4)

        # Assert
        assert lst == [1, 2, 3, 4]

    def test_list_remove(self):
        """测试列表删除"""
        # Arrange
        lst = [1, 2, 3, 4]

        # Act
        lst.remove(3)

        # Assert
        assert lst == [1, 2, 4]

    def test_list_length(self):
        """测试列表长度"""
        # Arrange
        lst = [1, 2, 3, 4, 5]

        # Act
        length = len(lst)

        # Assert
        assert length == 5


class TestDictionaryOperations:
    """字典操作测试类"""

    def test_dict_creation(self):
        """测试字典创建"""
        # Arrange & Act
        d = {"name": "Alice", "age": 30}

        # Assert
        assert d["name"] == "Alice"
        assert d["age"] == 30

    def test_dict_update(self):
        """测试字典更新"""
        # Arrange
        d = {"name": "Alice", "age": 30}

        # Act
        d["age"] = 31

        # Assert
        assert d["age"] == 31

    def test_dict_get(self):
        """测试字典获取"""
        # Arrange
        d = {"name": "Alice", "age": 30}

        # Act
        name = d.get("name")
        phone = d.get("phone", "N/A")

        # Assert
        assert name == "Alice"
        assert phone == "N/A"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
