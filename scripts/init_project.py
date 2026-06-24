#!/usr/bin/env python3
"""
项目初始化脚本
"""

import os
import subprocess
import sys


def create_directories():
    """创建项目目录结构"""
    directories = [
        # 项目管理
        "00_ProjectManagement/00_需求导入_QFD",
        "00_ProjectManagement/01_需求约束_Push",
        "00_ProjectManagement/02_需求转化_BasicStatics",
        "00_ProjectManagement/03_功能图谱_FunctionMap",
        "00_ProjectManagement/04_法规认证",
        "00_ProjectManagement/05_功能风险管控_DFMEA",
        "00_ProjectManagement/06_知识产权",
        "00_ProjectManagement/07_敏捷开发_Scrum",
        "00_ProjectManagement/08_持续集成与测试_DevOps",
        "00_ProjectManagement/09_产品生产管理_SixSigma",
        "00_ProjectManagement/10_缺陷管理追踪_Jira",

        # 参考文档
        "00_Reference/documentation/system/architecture",
        "00_Reference/documentation/system/decisions",
        "00_Reference/documentation/user-manual",
        "00_Reference/documentation/installation",
        "00_Reference/documentation/operation",
        "00_Reference/documentation/maintenance",
        "00_Reference/documentation/troubleshooting",
        "00_Reference/documentation/api-reference",
        "00_Reference/resources/datasheets",
        "00_Reference/resources/reference-manuals",
        "00_Reference/resources/tools",
        "00_Reference/resources/libraries",
        "00_Reference/standards/coding-standards",
        "00_Reference/standards/design-standards",
        "00_Reference/standards/testing-standards",

        # 硬件设计
        "02_Hardware/architecture",
        "02_Hardware/schematic",
        "02_Hardware/pcb",
        "02_Hardware/bom",
        "02_Hardware/interface",
        "02_Hardware/review",

        # 机械设计
        "03_Mechanical/architecture",
        "03_Mechanical/3d-model",
        "03_Mechanical/shell-design",
        "03_Mechanical/assembly",
        "03_Mechanical/interface",
        "03_Mechanical/review",

        # 固件开发
        "04_Firmware/architecture",
        "04_Firmware/bsp",
        "04_Firmware/drivers",
        "04_Firmware/middleware",
        "04_Firmware/rtos",
        "04_Firmware/interface",
        "04_Firmware/tests",
        "04_Firmware/docs",

        # 应用软件
        "05_Software/architecture",
        "05_Software/core",
        "05_Software/algorithms",
        "05_Software/protocols",
        "05_Software/services",
        "05_Software/interface",
        "05_Software/tests",
        "05_Software/docs",

        # 上位机工具
        "06_Tools/architecture",
        "06_Tools/web-control/src",
        "06_Tools/web-control/docs",
        "06_Tools/web-control/build",
        "06_Tools/app-control/src",
        "06_Tools/app-control/docs",
        "06_Tools/app-control/build",
        "06_Tools/desktop-tools/serial-monitor",
        "06_Tools/desktop-tools/data-analyzer",
        "06_Tools/desktop-tools/configuration",
        "06_Tools/scripts/build",
        "06_Tools/scripts/deploy",
        "06_Tools/scripts/test",

        # 工厂生产
        "06_Factory/production-plan",
        "06_Factory/quality",
        "06_Factory/factory-test",
        "06_Factory/deployment",
        "06_Factory/process",

        # 测试
        "07_Tests/unit",
        "07_Tests/integration",
        "07_Tests/system",
        "07_Tests/performance",
        "07_Tests/reports",
    ]

    print("Creating project directories...")
    for dir_path in directories:
        os.makedirs(dir_path, exist_ok=True)
        print(f"  Created: {dir_path}")

    print(f"\nTotal directories created: {len(directories)}")


def init_git():
    """初始化 Git 仓库"""
    print("\nInitializing Git repository...")

    try:
        # 初始化 Git
        subprocess.run(["git", "init"], check=True)
        print("  Git repository initialized")

        # 添加所有文件
        subprocess.run(["git", "add", "."], check=True)
        print("  Files added to Git")

        # 初始提交
        subprocess.run(["git", "commit", "-m", "feat: 初始化项目结构"], check=True)
        print("  Initial commit created")

        return True
    except subprocess.CalledProcessError as e:
        print(f"  Error initializing Git: {e}")
        return False
    except FileNotFoundError:
        print("  Git not found. Please install Git first.")
        return False


def create_gitignore():
    """创建 .gitignore 文件"""
    gitignore_content = """# 临时文件
*.tmp
*.temp
*.swp
*.swo
*~
.DS_Store
Thumbs.db

# 编译产物
*.o
*.obj
*.elf
*.bin
*.hex
*.map
*.axf
*.out
*.d

# IDE 配置
.vscode/
.idea/
*.swp
*.swo
*~

# 操作系统文件
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# 固件编译产物
04_Firmware/build/
04_Firmware/output/
04_Firmware/bin/
04_Firmware/obj/

# 软件编译产物
05_Software/build/
05_Software/output/
05_Software/bin/
05_Software/obj/
05_Software/__pycache__/
05_Software/**/*.pyc

# 上位机工具
06_Tools/web-control/node_modules/
06_Tools/web-control/dist/
06_Tools/web-control/build/
06_Tools/app-control/build/
06_Tools/app-control/.dart_tool/

# 测试报告
07_Tests/reports/*.html
07_Tests/reports/*.xml

# 环境变量
.env
.env.local
.env.*.local

# 日志文件
*.log
logs/
"""

    print("\nCreating .gitignore file...")
    with open(".gitignore", "w", encoding="utf-8") as f:
        f.write(gitignore_content)
    print("  .gitignore created")


def main():
    """主函数"""
    print("=" * 50)
    print("嵌入式产品项目初始化脚本")
    print("=" * 50)

    # 创建目录结构
    create_directories()

    # 创建 .gitignore
    create_gitignore()

    # 初始化 Git
    init_git()

    print("\n" + "=" * 50)
    print("项目初始化完成！")
    print("=" * 50)

    print("\n下一步操作:")
    print("1. 在 GitHub 上创建一个新的仓库")
    print("2. 运行以下命令推送到 GitHub:")
    print("   git remote add origin https://github.com/your-username/your-repo.git")
    print("   git push -u origin master")
    print("\n3. 开始使用 Claude Code 进行开发:")
    print("   在 Claude Code 中输入: '帮我分析这个智能温控器项目的需求'")


if __name__ == "__main__":
    main()
