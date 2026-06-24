# 贡献指南

感谢你对本项目的关注！我们欢迎所有形式的贡献。

## 如何贡献

### 1. 报告问题

如果你发现了bug或有改进建议，请在 [GitHub Issues](https://github.com/your-username/your-repo/issues) 中创建一个新的issue。

请包含以下信息：
- 问题描述
- 复现步骤
- 期望行为
- 实际行为
- 环境信息（操作系统、开发工具版本等）

### 2. 提交代码

#### 步骤 1: Fork 项目

在GitHub上fork本项目到你的账户。

#### 步骤 2: 克隆项目

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

#### 步骤 3: 创建特性分支

```bash
git checkout -b feature/your-feature-name
```

分支命名规范：
- `feature/xxx`: 新功能
- `fix/xxx`: 修复bug
- `docs/xxx`: 文档更新
- `refactor/xxx`: 代码重构
- `test/xxx`: 测试相关
- `chore/xxx`: 其他修改

#### 步骤 4: 进行修改

进行你的代码修改，确保：
1. 遵循项目的编码标准
2. 添加必要的注释
3. 编写清晰的提交信息

#### 步骤 5: 提交代码

```bash
git add .
git commit -m "feat: 添加新功能描述"
```

提交信息规范：
- `feat`: 新功能
- `fix`: 修复bug
- `docs`: 文档更新
- `style`: 代码格式（不影响代码运行的变动）
- `refactor`: 重构（既不是新增功能，也不是修改bug的代码变动）
- `test`: 增加测试
- `chore`: 构建过程或辅助工具的变动

#### 步骤 6: 推送到远程

```bash
git push origin feature/your-feature-name
```

#### 步骤 7: 创建 Pull Request

在GitHub上创建一个Pull Request，包含以下信息：
- 标题：简要描述修改内容
- 描述：详细说明修改内容、原因和影响
- 关联的issue（如果有）

### 3. 改进文档

帮助改进项目文档也是很有价值的贡献。你可以：
- 修复文档中的错误
- 添加新的文档
- 改进现有文档的表述
- 添加示例代码

### 4. 分享经验

分享你的使用经验和最佳实践，可以帮助其他用户更好地使用本项目。

## 开发规范

### 代码风格

#### C/C++ 代码风格
```c
// 函数命名：驼峰命名法
void FunctionName(void);

// 变量命名：小写下划线
int variable_name;

// 常量命名：大写下划线
#define CONSTANT_NAME

// 结构体命名：大驼峰命名法
typedef struct {
    int member_name;
} StructName_t;
```

#### Python 代码风格
```python
# 函数命名：小写下划线
def function_name():
    pass

# 变量命名：小写下划线
variable_name = 0

# 类命名：大驼峰命名法
class ClassName:
    pass

# 常量命名：大写下划线
CONSTANT_NAME = 0
```

#### JavaScript/TypeScript 代码风格
```javascript
// 函数命名：小驼峰命名法
function functionName() {}

// 变量命名：小驼峰命名法
let variableName;

// 类命名：大驼峰命名法
class ClassName {}

// 常量命名：大写下划线
const CONSTANT_NAME = 0;
```

### 提交信息规范

提交信息应该清晰、简洁，并遵循以下格式：

```
<type>: <subject>

<body>

<footer>
```

#### 示例

```
feat: 添加SPI驱动支持

- 实现SPI初始化函数
- 实现SPI发送和接收函数
- 添加SPI单元测试

Closes #123
```

### 代码审查

所有提交的代码都需要经过代码审查。审查时会检查：

1. **代码质量**
   - 代码是否清晰易读
   - 是否遵循编码标准
   - 是否有潜在的bug

2. **功能完整性**
   - 是否实现了预期功能
   - 是否有遗漏的边界情况

3. **测试覆盖**
   - 是否有相应的测试用例
   - 测试覆盖率是否足够

4. **文档更新**
   - 是否需要更新文档
   - 文档是否准确

### 测试要求

所有新功能和bug修复都应该包含相应的测试用例。

#### 单元测试
```c
// 示例：单元测试
void test_function_name(void) {
    // Arrange
    int input = 10;
    int expected = 20;
    
    // Act
    int result = function_name(input);
    
    // Assert
    assert(result == expected);
}
```

#### 集成测试
```python
# 示例：集成测试
def test_integration():
    # 测试多个组件之间的交互
    pass
```

## 开发环境设置

### 必需工具

- Git
- 代码编辑器（VS Code、CLion等）
- 相关开发工具（Keil MDK、IAR等）

### 可选工具

- Docker（用于容器化开发）
- CI/CD工具（用于自动化测试和部署）

### 环境配置

1. 安装Git
2. 配置Git用户信息
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your-email@example.com"
   ```
3. 克隆项目
4. 安装依赖（如果需要）

## 行为准则

### 我们的承诺

为了营造一个开放、友好的环境，我们承诺：
- 使用友好和包容的语言
- 尊重不同的观点和经验
- 接受建设性的批评
- 关注对社区最有利的事情
- 对其他社区成员表示同理心

### 不可接受的行为

- 使用性暗示的语言或图像
- 恶意评论、人身攻击或政治攻击
- 公开或私下的骚扰
- 未经明确许可发布他人的私人信息
- 其他在专业环境中被合理认为不适当的行为

## 获取帮助

如果你在贡献过程中遇到任何问题，可以通过以下方式获取帮助：
- 在GitHub Issues中提问
- 联系项目维护者
- 查阅项目文档

## 致谢

感谢所有为这个项目做出贡献的人！你的贡献使这个项目变得更好。
