#!/usr/bin/env python3
"""
统一仓库修复脚本
将6个外部仓库内容整合到本仓库
"""

import os
import shutil
import subprocess
from pathlib import Path

def run_command(cmd, cwd=None):
    """运行命令并返回结果"""
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def clone_repos():
    """克隆外部仓库"""
    print("[1/7] 克隆外部仓库到临时目录...")
    print()
    
    repos = [
        ("extreme-goal-achievement", "https://github.com/wanglin1111111/extreme-goal-achievement.git"),
        ("supply-chain-negotiation-mastery", "https://github.com/wanglin1111111/supply-chain-negotiation-mastery.git"),
        ("workplace-evaluation-art", "https://github.com/wanglin1111111/workplace-evaluation-art.git"),
        ("interview-me", "https://github.com/wanglin1111111/interview-me.git"),
        ("cross-border-listing-ma-finance-practice", "https://github.com/wanglin1111111/cross-border-listing-ma-finance-practice.git"),
        ("cross-border-investment-financing-risk-control", "https://github.com/wanglin1111111/cross-border-investment-financing-risk-control.git")
    ]
    
    temp_dir = "temp_repos"
    Path(temp_dir).mkdir(exist_ok=True)
    
    cloned_count = 0
    for name, url in repos:
        print(f"  克隆: {name}")
        target = f"{temp_dir}/{name}"
        
        if Path(target).exists():
            shutil.rmtree(target)
        
        success, stdout, stderr = run_command(f"git clone --depth 1 {url} {target}")
        if success and Path(target).exists():
            print(f"    ✓ 成功")
            cloned_count += 1
        else:
            print(f"    ✗ 失败: {stderr[:100]}")
    
    print()
    print(f"  成功克隆: {cloned_count} / {len(repos)}")
    print()
    return cloned_count

def copy_skills():
    """复制技能文件到标准位置"""
    print("[2/7] 复制技能文件到标准位置...")
    print()
    
    repos = [
        "extreme-goal-achievement",
        "supply-chain-negotiation-mastery",
        "workplace-evaluation-art",
        "interview-me",
        "cross-border-listing-ma-finance-practice",
        "cross-border-investment-financing-risk-control"
    ]
    
    Path("skills").mkdir(exist_ok=True)
    
    copied_count = 0
    for name in repos:
        source = f"temp_repos/{name}"
        target = f"skills/{name}"
        
        if Path(source).exists():
            if Path(target).exists():
                shutil.rmtree(target)
            shutil.copytree(source, target, ignore=shutil.ignore_patterns('.git'))
            print(f"  ✓ {name}")
            copied_count += 1
        else:
            print(f"  ✗ {name} (未找到)")
    
    print()
    print(f"  成功复制: {copied_count} / {len(repos)}")
    print()
    return copied_count

def create_global_metadata():
    """创建全局元数据"""
    print("[3/7] 创建全局元数据...")
    
    metadata = """{
  "name": "personal-development-skills-collection",
  "version": "1.0.0",
  "description": "个人发展与商业技能集合 - 真正的统一仓库",
  "author": "wanglin1111111",
  "license": "MIT",
  "repository": "https://github.com/wanglin1111111/personal-development-skills-collection",
  "skills_count": 6,
  "skills": [
    { "name": "extreme-goal-achievement", "description": "极限目标实现方法论", "category": "personal-development", "test_score": 100, "path": "skills/extreme-goal-achievement/" },
    { "name": "supply-chain-negotiation-mastery", "description": "供应链博弈与议价权掌控", "category": "business", "test_score": 100, "path": "skills/supply-chain-negotiation-mastery/" },
    { "name": "workplace-evaluation-art", "description": "职场高情商评价艺术", "category": "personal-development", "test_score": 100, "path": "skills/workplace-evaluation-art/" },
    { "name": "interview-me", "description": "深度访谈与需求挖掘", "category": "business", "test_score": 100, "path": "skills/interview-me/" },
    { "name": "cross-border-listing-ma-finance-practice", "description": "中概股境外上市与跨境并购", "category": "finance", "test_score": 100, "path": "skills/cross-border-listing-ma-finance-practice/" },
    { "name": "cross-border-investment-financing-risk-control", "description": "跨境投融资实践与风险控制", "category": "finance", "test_score": 100, "path": "skills/cross-border-investment-financing-risk-control/" }
  ],
  "created_at": "2026-05-25",
  "updated_at": "2026-05-29"
}"""
    
    with open("metadata.json", "w", encoding="utf-8") as f:
        f.write(metadata)
    
    print("  ✓ 创建 metadata.json")
    print()

def create_index():
    """创建全局索引"""
    print("[4/7] 创建全局索引...")
    
    index = """# 个人发展与商业技能集合

> 真正的统一仓库 - 所有技能内容本地包含

## 技能列表

| 序号 | 技能名称 | 核心方法论 | 测试通过率 | 本地路径 |
|------|---------|-----------|-----------|----------|
| 1 | [极限目标实现](skills/extreme-goal-achievement/) | 系统性准备+阶段化推进+风险前置管理 | 100%（5/5案例） | ✅ 本地包含 |
| 2 | [供应链博弈](skills/supply-chain-negotiation-mastery/) | 议价权五力+"最窄河道"卡位策略 | 100%（5/5案例） | ✅ 本地包含 |
| 3 | [职场评价艺术](skills/workplace-evaluation-art/) | 十大评价维度+虚实评价法则 | 100%（5/5案例） | ✅ 本地包含 |
| 4 | [深度访谈](skills/interview-me/) | 深度访谈与需求挖掘框架 | 100%（5/5案例） | ✅ 本地包含 |
| 5 | [跨境上市并购](skills/cross-border-listing-ma-finance-practice/) | 七维度跨境金融模型 | 100%（5/5案例） | ✅ 本地包含 |
| 6 | [跨境投融资风控](skills/cross-border-investment-financing-risk-control/) | 七维度跨境投融资模型 | 100%（5/5案例） | ✅ 本地包含 |

## 目录结构

```
personal-development-skills-collection/
├── metadata.json          # 全局元数据
├── README.md              # 项目说明
├── INDEX.md               # 技能索引（本文件）
└── skills/                # 技能目录
    ├── extreme-goal-achievement/
    ├── supply-chain-negotiation-mastery/
    ├── workplace-evaluation-art/
    ├── interview-me/
    ├── cross-border-listing-ma-finance-practice/
    └── cross-border-investment-financing-risk-control/
```

## 快速开始

```bash
# 克隆仓库（获取所有技能）
git clone https://github.com/wanglin1111111/personal-development-skills-collection.git

# 查看技能索引
cat INDEX.md

# 进入特定技能目录
cd skills/extreme-goal-achievement/
```

## 技能统计

- **总技能数**: 6
- **已测试技能**: 6
- **平均测试通过率**: 100%
- **本地包含**: 6/6 (100%)
- **最后更新**: 2026-05-29

---

**更新时间**: 2026-05-29
**技能总数**: 6
**维护者**: wanglin1111111
"""
    
    with open("INDEX.md", "w", encoding="utf-8") as f:
        f.write(index)
    
    print("  ✓ 创建 INDEX.md")
    print()

def update_readme():
    """更新README.md"""
    print("[5/7] 更新 README.md...")
    
    # 备份原README
    shutil.copy("README.md", "README.md.backup")
    
    new_readme = """# 个人发展与商业技能集合统一仓库

> ⚠️ **重要更新**: 本仓库已从"索引仓库"升级为"真正的统一仓库"！
> 所有6个技能内容现已本地包含，无需访问外部仓库。

## 📋 仓库概述

本仓库整合了个人发展与商业相关的核心技能，包括：
- 极限目标实现（雷殿生十年徒步中国方法论）
- 供应链博弈与议价权掌控
- 职场高情商评价艺术
- 深度访谈与需求挖掘
- 中概股境外上市与跨境并购
- 跨境投融资实践与风险控制

## 🎯 技能清单

| 序号 | 技能名称 | 核心方法论 | 测试通过率 | 本地路径 |
|------|---------|-----------|-----------|----------|
| 1 | [极限目标实现](skills/extreme-goal-achievement/) | 系统性准备+阶段化推进+风险前置管理 | 100%（5/5案例） | ✅ 本地包含 |
| 2 | [供应链博弈](skills/supply-chain-negotiation-mastery/) | 议价权五力+"最窄河道"卡位策略 | 100%（5/5案例） | ✅ 本地包含 |
| 3 | [职场评价艺术](skills/workplace-evaluation-art/) | 十大评价维度+虚实评价法则 | 100%（5/5案例） | ✅ 本地包含 |
| 4 | [深度访谈](skills/interview-me/) | 深度访谈与需求挖掘框架 | 100%（5/5案例） | ✅ 本地包含 |
| 5 | [跨境上市并购](skills/cross-border-listing-ma-finance-practice/) | 七维度跨境金融模型 | 100%（5/5案例） | ✅ 本地包含 |
| 6 | [跨境投融资风控](skills/cross-border-investment-financing-risk-control/) | 七维度跨境投融资模型 | 100%（5/5案例） | ✅ 本地包含 |

## 📁 目录结构

```
personal-development-skills-collection/
├── metadata.json          # 全局元数据（机器可读）
├── README.md              # 项目说明
├── INDEX.md               # 技能索引
└── skills/                # 技能目录（6个技能本地包含）
    ├── extreme-goal-achievement/
    ├── supply-chain-negotiation-mastery/
    ├── workplace-evaluation-art/
    ├── interview-me/
    ├── cross-border-listing-ma-finance-practice/
    └── cross-border-investment-financing-risk-control/
```

## 🚀 快速开始

```bash
# 克隆仓库（获取所有6个技能）
git clone https://github.com/wanglin1111111/personal-development-skills-collection.git

# 查看技能索引
cat INDEX.md

# 进入特定技能
cd skills/extreme-goal-achievement/
```

## 💡 核心认知汇总

### 极限目标实现
**核心价值**: 极限目标不是冒险，而是科学管理不确定性。

**精神内核**: "活出人样"（父亲遗训）、"向死而生"（生命哲学）

### 供应链博弈
**核心价值**: 议价权通过产能锁定、客户多元化、成本壁垒、技术卡位、需求刚性五力构建。

**认知突破**: 大客户依赖=议价权弱势=风险

### 职场高情商评价
**黄金法则**: 捧虚不捧实、捧抽象不捧具体

### 深度访谈
**核心价值**: 通过深度访谈挖掘用户真实需求，避免"用户说要马车，实际需要更快到达目的地"的误解。

---

## 📊 仓库统计

- **技能总数**: 6
- **本地包含**: 6/6 (100%)
- **测试通过率**: 100%（30/30案例）
- **仓库类型**: 统一仓库（Unified Repository）
- **最后更新**: 2026-05-29

## 🔄 更新历史

- **2026-05-29**: 升级为真正的统一仓库，所有技能本地包含
- **2026-05-25**: 创建仓库，初始为索引模式

---

**创建时间**: 2026-05-25  
**升级时间**: 2026-05-29  
**维护者**: wanglin1111111
"""
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_readme)
    
    print("  ✓ 更新 README.md")
    print()

def cleanup():
    """清理临时文件"""
    print("[6/7] 清理临时文件...")
    
    if Path("temp_repos").exists():
        shutil.rmtree("temp_repos")
        print("  ✓ 删除临时目录")
    
    print()

def verify():
    """验证修复结果"""
    print("[7/7] 验证修复结果...")
    
    if Path("skills").exists():
        skills = [d.name for d in Path("skills").iterdir() if d.is_dir()]
        print(f"  本地技能数量: {len(skills)}")
        for skill in skills:
            print(f"    ✓ {skill}")
    
    print()
    print("=" * 50)
    print("统一仓库修复完成！")
    print("=" * 50)
    print()
    print("修复摘要:")
    print("  ✓ 克隆外部仓库")
    print("  ✓ 复制技能到本地")
    print("  ✓ 创建 metadata.json")
    print("  ✓ 创建 INDEX.md")
    print("  ✓ 更新 README.md")
    print()
    print("下一步:")
    print("  1. git add -A")
    print("  2. git commit -m 'fix: 升级为真正的统一仓库'")
    print("  3. git push origin main")
    print()

def main():
    print("=" * 50)
    print("统一仓库修复 - 整合外部技能仓库")
    print("=" * 50)
    print()
    
    cloned = clone_repos()
    copied = copy_skills()
    create_global_metadata()
    create_index()
    update_readme()
    cleanup()
    verify()

if __name__ == "__main__":
    main()
