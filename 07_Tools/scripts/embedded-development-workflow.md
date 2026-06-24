# 嵌入式开发工作流

## 工作流概述

本工作流整合了嵌入式产品开发的全流程，从需求分析到生产部署，支持硬件设计、固件开发、应用软件开发、上位机工具开发、机械设计等多个维度。

## 工作流阶段

### 阶段 1: 需求分析 (Sprint 0)

**目标**: 明确项目需求，制定项目计划

**执行步骤**:
1. 调用 `需求工程工作流` 进行需求分析
2. 调用 `embedded-architect` skill 进行架构可行性分析
3. 调用 `DFMEA 工作流` 进行风险评估
4. 调用 `Scrum 工作流` 制定项目计划

**输出物**:
- 00_ProjectManagement/00_需求导入_QFD/
- 00_ProjectManagement/01_需求约束_Push/
- 00_ProjectManagement/03_功能图谱_FunctionMap/
- 00_ProjectManagement/05_功能风险管控_DFMEA/

**技能调用**:
```markdown
# 需求分析
用户: "帮我分析这个智能温控器项目的需求"

# Claude 自动执行
1. 调用需求工程工作流
2. 调用 embedded-architect skill
3. 调用 DFMEA 工作流
4. 调用 Scrum 工作流
```

### 阶段 2: 系统设计 (Sprint 0)

**目标**: 完成系统架构设计和技术选型

**执行步骤**:
1. 调用 `embedded-architect` skill 进行系统架构设计
2. 调用 `chip-architecture` skill 进行 MCU 选型
3. 调用 `api-design` skill 进行接口设计
4. 调用 `architecture-decision-records` skill 记录架构决策

**输出物**:
- 00_Reference/documentation/system/architecture/01_系统架构设计.md
- 00_Reference/documentation/system/decisions/ADR-001-MCU选型.md
- 02_Hardware/architecture/01_硬件架构设计.md
- 04_Firmware/architecture/01_固件架构设计.md

**技能调用**:
```markdown
# 系统架构设计
用户: "帮我设计这个系统的架构"

# Claude 自动执行
1. 调用 embedded-architect skill
2. 调用 chip-architecture skill
3. 调用 api-design skill
4. 调用 architecture-decision-records skill
```

### 阶段 3: 硬件设计 (Sprint 1)

**目标**: 完成硬件设计和评审

**执行步骤**:
1. 调用 `hardware-design` 工作流进行硬件设计
2. 调用 `embedded-architect` skill 进行引脚分配
3. 调用 `i2c-bus`, `spi-bus`, `uart-module` skills 进行总线设计
4. 调用 `embedded-reviewer` skill 进行设计评审

**输出物**:
- 02_Hardware/schematic/ - 原理图
- 02_Hardware/pcb/ - PCB 设计
- 02_Hardware/bom/ - BOM 清单
- 02_Hardware/interface/ - 硬件接口定义

**技能调用**:
```markdown
# 硬件设计
用户: "帮我设计这个产品的硬件"

# Claude 自动执行
1. 调用 hardware-design 工作流
2. 调用 embedded-architect skill
3. 调用 i2c-bus, spi-bus, uart-module skills
4. 调用 embedded-reviewer skill
```

### 阶段 4: 机械设计 (Sprint 1)

**目标**: 完成 3D 外壳设计和装配设计

**执行步骤**:
1. 调用 `mechanical-design` 工作流进行机械设计
2. 调用 `embedded-architect` skill 确认接口位置
3. 进行 3D 建模和外壳设计
4. 进行装配设计和评审

**输出物**:
- 03_Mechanical/3d-model/ - 3D 模型
- 03_Mechanical/shell-design/ - 外壳设计
- 03_Mechanical/assembly/ - 装配设计
- 03_Mechanical/interface/ - 机械接口定义

**技能调用**:
```markdown
# 机械设计
用户: "帮我设计这个产品的3D外壳"

# Claude 自动执行
1. 调用 mechanical-design 工作流
2. 调用 embedded-architect skill
3. 生成 3D 模型和外壳设计
4. 生成装配图和评审报告
```

### 阶段 5: 固件开发 (Sprint 2-N)

**目标**: 完成固件开发和测试

**执行步骤**:
1. 调用 `firmware-development` 工作流进行固件开发
2. 调用 `peripheral-driver` skill 开发驱动程序
3. 调用 `freertos-module` skill 配置 RTOS
4. 调用 `tdd-workflow` skill 进行测试驱动开发

**输出物**:
- 04_Firmware/drivers/ - 驱动程序
- 04_Firmware/middleware/ - 中间件
- 04_Firmware/rtos/ - RTOS 配置
- 04_Firmware/tests/ - 单元测试

**技能调用**:
```markdown
# 固件开发
用户: "帮我实现这个产品的固件"

# Claude 自动执行
1. 调用 firmware-development 工作流
2. 调用 peripheral-driver skill
3. 调用 freertos-module skill
4. 调用 tdd-workflow skill
```

### 阶段 6: 应用软件开发 (Sprint 2-N)

**目标**: 完成应用软件开发和测试

**执行步骤**:
1. 调用 `backend-patterns` skill 进行架构设计
2. 调用 `api-design` skill 进行接口设计
3. 调用 `coding-standards` skill 确保代码质量
4. 调用 `tdd-workflow` skill 进行测试驱动开发

**输出物**:
- 05_Software/core/ - 核心业务逻辑
- 05_Software/algorithms/ - 算法实现
- 05_Software/protocols/ - 通信协议
- 05_Software/tests/ - 单元测试

**技能调用**:
```markdown
# 应用软件开发
用户: "帮我实现这个产品的应用软件"

# Claude 自动执行
1. 调用 backend-patterns skill
2. 调用 api-design skill
3. 调用 coding-standards skill
4. 调用 tdd-workflow skill
```

### 阶段 7: 上位机开发 (Sprint 3-N)

**目标**: 完成 Web 控制端和 APP 控制端开发

**执行步骤**:
1. 调用 `frontend-patterns` skill 进行前端架构设计
2. 调用 `react-patterns` / `vue-patterns` skill 进行 Web 开发
3. 调用 `dart-flutter-patterns` skill 进行 APP 开发
4. 调用 `mqtt-module` skill 进行物联网协议集成

**输出物**:
- 07_Tools/web-control/ - Web 控制端
- 07_Tools/app-control/ - APP 控制端
- 07_Tools/desktop-tools/ - 桌面工具

**技能调用**:
```markdown
# 上位机开发
用户: "帮我实现这个产品的控制端"

# Claude 自动执行
1. 调用 frontend-patterns skill
2. 调用 react-patterns / vue-patterns skill
3. 调用 dart-flutter-patterns skill
4. 调用 mqtt-module skill
```

### 阶段 8: 集成测试 (Sprint N)

**目标**: 完成系统集成测试和验证

**执行步骤**:
1. 调用 `testing-cicd` 工作流进行测试规划
2. 调用 `embedded-debugger-framework` skill 进行故障诊断
3. 调用 `security-review` skill 进行安全审查
4. 调用 `static-analysis` skill 进行代码质量检查

**输出物**:
- 05_Software/tests/unit/ - 单元测试
- 05_Software/tests/integration/ - 集成测试
- 05_Software/tests/system/ - 系统测试
- 05_Software/tests/reports/ - 测试报告

**技能调用**:
```markdown
# 集成测试
用户: "帮我测试这个产品"

# Claude 自动执行
1. 调用 testing-cicd 工作流
2. 调用 embedded-debugger-framework skill
3. 调用 security-review skill
4. 调用 static-analysis skill
```

### 阶段 9: 生产准备 (发布前)

**目标**: 完成生产准备和部署

**执行步骤**:
1. 调用 `production-management` 工作流进行生产规划
2. 调用 `factory-test` 工作流进行工厂测试
3. 调用 `document-writing` 工作流生成用户文档
4. 调用 `deployment-patterns` skill 进行部署

**输出物**:
- 06_Factory/production-plan/ - 生产计划
- 06_Factory/quality/ - 质量控制
- 06_Factory/factory-test/ - 工厂测试
- 00_Reference/documentation/user-manual/ - 用户手册

**技能调用**:
```markdown
# 生产准备
用户: "帮我准备生产"

# Claude 自动执行
1. 调用 production-management 工作流
2. 调用 factory-test 工作流
3. 调用 document-writing 工作流
4. 调用 deployment-patterns skill
```

## 工作流集成

### 技能调用优先级

1. **架构决策**: embedded-architect + architecture-decision-records
2. **代码实现**: tdd-workflow + 对应的模块技能
3. **质量保证**: coding-standards + security-review + static-analysis
4. **版本控制**: git-workflow + firmware-sign

### Claude 与 Codex 协作模式

- **Claude 负责**: 架构设计、风险分析、代码审查
- **Codex 负责**: 代码实现、测试生成、构建配置

### 交接规范

```markdown
# Claude → Codex 交接
## 任务：实现 XX 驱动

### 硬件信息
- 芯片型号：STM32F407
- 外设：SPI, I2C, UART

### 功能需求
- 初始化 SPI 接口
- 发送/接收数据
- 中断处理

### 接口定义
```c
typedef struct {
    SPI_TypeDef *instance;
    uint32_t baudrate;
    uint8_t mode;
} SPI_Handle_t;
```

### 约束条件
- 遵循 MISRA C 规范
- 支持 DMA 传输

### 输出要求
- 驱动代码：spi_driver.c, spi_driver.h
- 单元测试：test_spi_driver.c
- 文档：README.md
```

## 文档生成

### 各阶段文档清单

| 阶段 | 文档 | 输出位置 |
|------|------|----------|
| 需求分析 | 需求文档 | 00_ProjectManagement/ |
| 系统设计 | 架构文档 | 00_Reference/documentation/system/ |
| 硬件设计 | 硬件文档 | 02_Hardware/ |
| 机械设计 | 机械文档 | 03_Mechanical/ |
| 固件开发 | 固件文档 | 04_Firmware/docs/ |
| 应用软件 | 软件文档 | 05_Software/docs/ |
| 上位机 | 工具文档 | 07_Tools/*/docs/ |
| 测试 | 测试报告 | 05_Software/tests/reports/ |
| 生产 | 生产文档 | 06_Factory/ |

### 文档生成技能

- `document-writing` 工作流: 生成各类文档
- `doc-automation` skill: 文档自动化
- `embedded-learning-notes` skill: 学习笔记
- `embedded-learning-path-framework` skill: 学习路径

## 最佳实践

### 1. 迭代策略

- **Sprint 0**: 完成架构设计和技术选型
- **Sprint 1**: 完成硬件设计和机械设计
- **Sprint 2-N**: 逐步实现固件、软件、上位机
- **发布前**: 集成测试和生产准备

### 2. 风险管理

- **技术风险**: 调用 embedded-architect skill 提前识别
- **进度风险**: 调用 Scrum 工作流进行 Sprint 规划
- **质量风险**: 调用 embedded-reviewer skill 进行代码审查

### 3. 知识沉淀

- **技术文档**: 调用 document-writing 工作流
- **学习笔记**: 调用 embedded-learning-notes skill
- **经验总结**: 调用 embedded-learning-path-framework skill

## 快速开始

### 步骤 1: 项目启动

```bash
# 在项目目录中
cd /c/Users/zhang/embedded-product-project

# 启动 Claude Code
# 输入: "帮我分析这个智能温控器项目的需求"
```

### 步骤 2: 按阶段执行

按照工作流的 9 个阶段逐步执行，每个阶段调用相应的技能和工作流。

### 步骤 3: 文档生成

在每个阶段结束时，自动生成相应的文档，确保项目的完整性和可追溯性。

## 参考资源

- [嵌入式系统架构师思维框架](~/.claude/skills/embedded-architect/SKILL.md)
- [嵌入式系统故障诊断框架](~/.claude/skills/embedded-debugger-framework/SKILL.md)
- [固件开发管理工作流](~/.claude/workflows/firmware-development/)
- [硬件设计管理工作流](~/.claude/workflows/hardware-design/)
- [测试 CI/CD 工作流](~/.claude/workflows/testing-cicd/)
