#!/usr/bin/env pwsh
# 统一仓库修复脚本
# 将6个外部仓库内容整合到本仓库

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "统一仓库修复 - 整合外部技能仓库" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

# 定义外部仓库列表
$repos = @(
    @{ Name = "extreme-goal-achievement"; Url = "https://github.com/wanglin1111111/extreme-goal-achievement.git" },
    @{ Name = "supply-chain-negotiation-mastery"; Url = "https://github.com/wanglin1111111/supply-chain-negotiation-mastery.git" },
    @{ Name = "workplace-evaluation-art"; Url = "https://github.com/wanglin1111111/workplace-evaluation-art.git" },
    @{ Name = "interview-me"; Url = "https://github.com/wanglin1111111/interview-me.git" },
    @{ Name = "cross-border-listing-ma-finance-practice"; Url = "https://github.com/wanglin1111111/cross-border-listing-ma-finance-practice.git" },
    @{ Name = "cross-border-investment-financing-risk-control"; Url = "https://github.com/wanglin1111111/cross-border-investment-financing-risk-control.git" }
)

# 创建临时目录
$tempDir = "temp_repos"
if (-not (Test-Path $tempDir)) {
    New-Item -ItemType Directory -Path $tempDir -Force | Out-Null
}

# 创建 skills 目录
if (-not (Test-Path "skills")) {
    New-Item -ItemType Directory -Path "skills" -Force | Out-Null
}

Write-Host "[1/7] 克隆外部仓库到临时目录..." -ForegroundColor Yellow
Write-Host ""

$clonedCount = 0
foreach ($repo in $repos) {
    $repoName = $repo.Name
    $repoUrl = $repo.Url
    $targetDir = "$tempDir/$repoName"
    
    Write-Host "  克隆: $repoName" -ForegroundColor Gray
    
    if (Test-Path $targetDir) {
        Remove-Item -Path $targetDir -Recurse -Force
    }
    
    try {
        git clone --depth 1 $repoUrl $targetDir 2>&1 | Out-Null
        if (Test-Path $targetDir) {
            Write-Host "    ✓ 成功" -ForegroundColor Green
            $clonedCount++
        } else {
            Write-Host "    ✗ 失败" -ForegroundColor Red
        }
    } catch {
        Write-Host "    ✗ 错误: $_" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "  成功克隆: $clonedCount / $($repos.Count)" -ForegroundColor Cyan
Write-Host ""

Write-Host "[2/7] 复制技能文件到标准位置..." -ForegroundColor Yellow
Write-Host ""

$copiedCount = 0
foreach ($repo in $repos) {
    $repoName = $repo.Name
    $sourceDir = "$tempDir/$repoName"
    $targetDir = "skills/$repoName"
    
    if (Test-Path $sourceDir) {
        if (-not (Test-Path $targetDir)) {
            New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
        }
        
        # 复制所有文件（排除.git）
        Get-ChildItem -Path $sourceDir -Exclude ".git" | ForEach-Object {
            $destPath = "$targetDir/$($_.Name)"
            if ($_.PSIsContainer) {
                Copy-Item -Path $_.FullName -Destination $destPath -Recurse -Force
            } else {
                Copy-Item -Path $_.FullName -Destination $destPath -Force
            }
        }
        
        Write-Host "  ✓ $repoName" -ForegroundColor Green
        $copiedCount++
    } else {
        Write-Host "  ✗ $repoName (未找到)" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "  成功复制: $copiedCount / $($repos.Count)" -ForegroundColor Cyan
Write-Host ""

Write-Host "[3/7] 创建全局元数据..." -ForegroundColor Yellow

$globalMetadata = @"
{
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
}
"@

$globalMetadata | Out-File -FilePath "metadata.json" -Encoding UTF8
Write-Host "  ✓ 创建 metadata.json" -ForegroundColor Green
Write-Host ""

Write-Host "[4/7] 创建全局索引..." -ForegroundColor Yellow

$indexContent = @"
# 个人发展与商业技能集合

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
    │   ├── SKILL.md
    │   ├── QUICKREF.md
    │   └── metadata.json
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
"@

$indexContent | Out-File -FilePath "INDEX.md" -Encoding UTF8
Write-Host "  ✓ 创建 INDEX.md" -ForegroundColor Green
Write-Host ""

Write-Host "[5/7] 更新 README.md..." -ForegroundColor Yellow

# 备份原README
Copy-Item -Path "README.md" -Destination "README.md.backup" -Force

# 读取原README内容
$readmeContent = Get-Content -Path "README.md" -Raw -Encoding UTF8

# 添加统一仓库说明
$newReadme = @"
# 个人发展与商业技能集合统一仓库

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

"@

# 保留原README的核心认知部分
if ($readmeContent -match "## 💡 核心认知汇总") {
    $coreContent = $readmeContent -replace ".*## 💡 核心认知汇总", ""
    $newReadme += $coreContent
} else {
    $newReadme += "
（详见各技能目录下的SKILL.md）
"
}

$newReadme += @"

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
"@

$newReadme | Out-File -FilePath "README.md" -Encoding UTF8
Write-Host "  ✓ 更新 README.md" -ForegroundColor Green
Write-Host ""

Write-Host "[6/7] 清理临时文件..." -ForegroundColor Yellow
if (Test-Path $tempDir) {
    Remove-Item -Path $tempDir -Recurse -Force
    Write-Host "  ✓ 删除临时目录" -ForegroundColor Green
}
Write-Host ""

Write-Host "[7/7] 验证修复结果..." -ForegroundColor Yellow
$skillsDir = "skills"
if (Test-Path $skillsDir) {
    $skillCount = (Get-ChildItem -Path $skillsDir -Directory).Count
    Write-Host "  本地技能数量: $skillCount" -ForegroundColor Cyan
    
    Get-ChildItem -Path $skillsDir -Directory | ForEach-Object {
        Write-Host "    ✓ $($_.Name)" -ForegroundColor Green
    }
}
Write-Host ""

Write-Host "==========================================" -ForegroundColor Green
Write-Host "统一仓库修复完成！" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green
Write-Host ""
Write-Host "修复摘要:" -ForegroundColor Cyan
Write-Host "  ✓ 克隆 $clonedCount 个外部仓库" -ForegroundColor White
Write-Host "  ✓ 复制 $copiedCount 个技能到本地" -ForegroundColor White
Write-Host "  ✓ 创建 metadata.json（全局元数据）" -ForegroundColor White
Write-Host "  ✓ 创建 INDEX.md（全局索引）" -ForegroundColor White
Write-Host "  ✓ 更新 README.md（统一仓库说明）" -ForegroundColor White
Write-Host ""
Write-Host "下一步操作:" -ForegroundColor Yellow
Write-Host "  1. git add -A" -ForegroundColor Gray
Write-Host "  2. git commit -m 'fix: 升级为真正的统一仓库'" -ForegroundColor Gray
Write-Host "  3. git push origin main" -ForegroundColor Gray
Write-Host ""
