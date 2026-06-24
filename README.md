# 嵌入式产品开发项目

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/your-username/your-repo.svg?style=social)](https://github.com/your-username/your-repo/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/your-username/your-repo.svg?style=social)](https://github.com/your-username/your-repo/network/members)
[![GitHub issues](https://img.shields.io/github/issues/your-username/your-repo.svg)](https://github.com/your-username/your-repo/issues)

## 项目简介

这是一个完整的嵌入式产品开发项目模板，包含了从需求分析到生产部署的全流程管理。项目采用敏捷开发方法，支持硬件设计、固件开发、应用软件开发、上位机工具开发、机械设计等多个维度。

## 项目结构

```
嵌入式产品项目/
├── 00_ProjectManagement/          # 项目管理
│   ├── 00_需求导入_QFD/           # 客户需求分析
│   ├── 01_需求约束_Push/          # 需求约束分析
│   ├── 02_需求转化_BasicStatics/  # 需求转化分析
│   ├── 03_功能图谱_FunctionMap/   # 功能图谱
│   ├── 04_法规认证/               # 法规认证
│   ├── 05_功能风险管控_DFMEA/     # DFMEA分析
│   ├── 06_知识产权/               # 知识产权
│   ├── 07_敏捷开发_Scrum/         # 敏捷开发管理
│   ├── 08_持续集成与测试_DevOps/  # CI/CD管理
│   ├── 09_产品生产管理_SixSigma/  # 生产管理
│   └── 10_缺陷管理追踪_Jira/      # 缺陷管理
├── 00_Reference/                   # 参考文档
│   ├── documentation/              # 文档
│   ├── resources/                  # 资源
│   └── standards/                  # 标准规范
├── 02_Hardware/                    # 硬件设计
├── 03_Mechanical/                  # 机械设计
├── 04_Firmware/                    # 固件开发
├── 05_Software/                    # 应用软件
├── 06_Tools/                       # 上位机工具
├── 06_Factory/                     # 工厂生产
└── 07_Tests/                       # 测试
```

## 功能特性

### 1. 完整的项目管理体系
- 需求工程（QFD、Push矩阵、功能图谱）
- 敏捷开发管理（Scrum）
- 风险管控（DFMEA）
- 缺陷管理（Jira）

### 2. 硬件设计支持
- 原理图设计
- PCB布局
- BOM管理
- 硬件评审

### 3. 固件开发支持
- 分层架构设计
- HAL层抽象
- 驱动程序开发
- RTOS集成

### 4. 应用软件开发
- 业务逻辑实现
- 算法开发
- 通信协议
- 服务层设计

### 5. 上位机工具开发
- Web控制端（React/Vue）
- APP控制端（Flutter/React Native）
- 桌面工具（Python/C#）

### 6. 机械设计支持
- 3D建模
- 外壳设计
- 装配设计

### 7. 测试与质量保证
- 单元测试
- 集成测试
- 系统测试
- 性能测试

### 8. 生产管理
- 生产计划
- 质量控制
- 工厂测试
- 部署管理

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. 初始化项目结构

```bash
# 创建目录结构
mkdir -p 00_ProjectManagement/{00_需求导入_QFD,01_需求约束_Push,02_需求转化_BasicStatics,03_功能图谱_FunctionMap,04_法规认证,05_功能风险管控_DFMEA,06_知识产权,07_敏捷开发_Scrum,08_持续集成与测试_DevOps,09_产品生产管理_SixSigma,10_缺陷管理追踪_Jira}
mkdir -p 00_Reference/{documentation/{system/{architecture,decisions},user-manual,installation,operation,maintenance,troubleshooting,api-reference},resources/{datasheets,reference-manuals,tools,libraries},standards/{coding-standards,design-standards,testing-standards}}
mkdir -p 02_Hardware/{architecture,schematic,pcb,bom,interface,review}
mkdir -p 03_Mechanical/{architecture,3d-model,shell-design,assembly,interface,review}
mkdir -p 04_Firmware/{architecture,bsp,drivers,middleware,rtos,interface,tests,docs}
mkdir -p 05_Software/{architecture,core,algorithms,protocols,services,interface,tests,docs}
mkdir -p 06_Tools/{architecture,web-control/src,app-control/src,desktop-tools/{serial-monitor,data-analyzer,configuration},scripts/{build,deploy,test}}
mkdir -p 06_Factory/{production-plan,quality,factory-test,deployment,process}
mkdir -p 07_Tests/{unit,integration,system,performance,reports}
```

### 3. 配置 Claude Code

在项目根目录创建 `.claude/settings.json`：

```json
{
  "skills": {
    "directories": [
      "C:/Users/zhang/.claude/skills",
      "C:/Users/zhang/.claude/plugins/cache/ecc/ecc/2.0.0/skills",
      "C:/Users/zhang/.claude/plugins/cache/superpowers-marketplace/superpowers/6.0.2/skills"
    ]
  }
}
```

### 4. 开始开发

```bash
# 需求分析
# 在 Claude Code 中输入: "帮我分析这个智能温控器项目的需求"

# 架构设计
# 在 Claude Code 中输入: "帮我设计这个系统的架构"

# 硬件设计
# 在 Claude Code 中输入: "帮我设计这个产品的硬件"

# 固件开发
# 在 Claude Code 中输入: "帮我实现这个产品的固件"
```

## 开发流程

### 阶段 1: 项目启动 (Sprint 0)
1. 需求分析
2. 架构设计
3. 技术选型
4. 项目计划

### 阶段 2: 硬件设计 (Sprint 1)
1. 硬件架构设计
2. 原理图设计
3. PCB布局
4. BOM管理

### 阶段 3: 固件开发 (Sprint 2-N)
1. 固件架构设计
2. HAL层开发
3. 驱动程序开发
4. 中间件开发
5. 应用层开发

### 阶段 4: 软件开发 (Sprint 2-N)
1. 软件架构设计
2. 核心业务逻辑开发
3. 算法实现
4. 通信协议开发

### 阶段 5: 上位机开发 (Sprint 3-N)
1. Web控制端开发
2. APP控制端开发
3. 桌面工具开发

### 阶段 6: 测试验证 (Sprint N)
1. 单元测试
2. 集成测试
3. 系统测试
4. 性能测试

### 阶段 7: 生产准备 (发布前)
1. 生产计划
2. 质量控制
3. 工厂测试
4. 部署管理

## 技术栈

### 硬件设计
- 原理图设计: Altium Designer / Cadence
- PCB设计: Altium Designer / KiCad
- 3D建模: SolidWorks / Fusion 360

### 固件开发
- MCU: STM32 / ESP32 / nRF52
- 开发环境: Keil MDK / IAR / STM32CubeIDE
- RTOS: FreeRTOS / RT-Thread
- 驱动框架: HAL / LL / SPL

### 应用软件
- 编程语言: C / C++ / Python
- 通信协议: MQTT / HTTP / WebSocket
- 数据库: SQLite / MySQL

### 上位机工具
- Web控制端: React / Vue / Angular
- APP控制端: Flutter / React Native
- 桌面工具: Python / C# / Electron

### 测试工具
- 单元测试: Unity / Google Test
- 集成测试: Robot Framework
- 性能测试: JMeter / Locust

## 文档

### 项目文档
- [需求文档](00_ProjectManagement/requirements/)
- [架构设计](00_Reference/documentation/system/architecture/)
- [接口定义](02_Hardware/interface/)
- [API文档](00_Reference/documentation/api-reference/)

### 用户文档
- [用户手册](00_Reference/documentation/user-manual/)
- [安装指南](00_Reference/documentation/installation/)
- [操作手册](00_Reference/documentation/operation/)
- [维护手册](00_Reference/documentation/maintenance/)
- [故障排除](00_Reference/documentation/troubleshooting/)

### 开发文档
- [编码标准](00_Reference/standards/coding-standards/)
- [设计标准](00_Reference/standards/design-standards/)
- [测试标准](00_Reference/standards/testing-standards/)

## 贡献指南

我们欢迎所有形式的贡献！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何参与项目开发。

### 贡献方式

1. **报告问题**: 在 [GitHub Issues](https://github.com/your-username/your-repo/issues) 中报告bug或提出建议
2. **提交代码**: Fork项目，创建特性分支，提交Pull Request
3. **改进文档**: 帮助改进项目文档
4. **分享经验**: 分享你的使用经验和最佳实践

### 开发规范

1. 遵循项目的编码标准
2. 提交代码前进行代码审查
3. 编写清晰的提交信息
4. 添加必要的测试用例
5. 更新相关文档

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 联系方式

- 项目主页: https://github.com/your-username/your-repo
- 问题反馈: https://github.com/your-username/your-repo/issues
- 邮箱: your-email@example.com

## 致谢

感谢所有为这个项目做出贡献的人！

特别感谢：
- Claude Code - 提供AI辅助开发
- ECC插件 - 提供开发工具和最佳实践
- Superpowers插件 - 提供工作流支持

---

**注意**: 这是一个模板项目，你可以根据自己的需求进行修改和扩展。
