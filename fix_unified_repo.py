#!/usr/bin/env python3
import os
import shutil
import subprocess
from pathlib import Path

def run(cmd, cwd=None):
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    return result.returncode == 0, result.stdout, result.stderr

def main():
    print("=" * 50)
    print("Fixing Unified Repository")
    print("=" * 50)
    print()
    
    repos = [
        ("extreme-goal-achievement", "https://github.com/wanglin1111111/extreme-goal-achievement.git"),
        ("supply-chain-negotiation-mastery", "https://github.com/wanglin1111111/supply-chain-negotiation-mastery.git"),
        ("workplace-evaluation-art", "https://github.com/wanglin1111111/workplace-evaluation-art.git"),
        ("interview-me", "https://github.com/wanglin1111111/interview-me.git"),
        ("cross-border-listing-ma-finance-practice", "https://github.com/wanglin1111111/cross-border-listing-ma-finance-practice.git"),
        ("cross-border-investment-financing-risk-control", "https://github.com/wanglin1111111/cross-border-investment-financing-risk-control.git")
    ]
    
    # Step 1: Clone repos
    print("[1/5] Cloning external repositories...")
    Path("temp_repos").mkdir(exist_ok=True)
    cloned = 0
    for name, url in repos:
        print(f"  Cloning: {name}")
        target = f"temp_repos/{name}"
        if Path(target).exists():
            shutil.rmtree(target)
        success, _, _ = run(f"git clone --depth 1 {url} {target}")
        if success and Path(target).exists():
            print(f"    OK")
            cloned += 1
        else:
            print(f"    FAILED")
    print(f"  Cloned: {cloned}/{len(repos)}")
    print()
    
    # Step 2: Copy to skills
    print("[2/5] Copying skills to local directory...")
    Path("skills").mkdir(exist_ok=True)
    copied = 0
    for name, _ in repos:
        source = f"temp_repos/{name}"
        target = f"skills/{name}"
        if Path(source).exists():
            if Path(target).exists():
                shutil.rmtree(target)
            shutil.copytree(source, target, ignore=shutil.ignore_patterns('.git'))
            print(f"  OK: {name}")
            copied += 1
    print(f"  Copied: {copied}/{len(repos)}")
    print()
    
    # Step 3: Create metadata.json
    print("[3/5] Creating metadata.json...")
    metadata = """{
  "name": "personal-development-skills-collection",
  "version": "1.0.0",
  "description": "Personal development and business skills - Unified Repository",
  "author": "wanglin1111111",
  "license": "MIT",
  "skills_count": 6,
  "skills": [
    { "name": "extreme-goal-achievement", "category": "personal-development", "path": "skills/extreme-goal-achievement/" },
    { "name": "supply-chain-negotiation-mastery", "category": "business", "path": "skills/supply-chain-negotiation-mastery/" },
    { "name": "workplace-evaluation-art", "category": "personal-development", "path": "skills/workplace-evaluation-art/" },
    { "name": "interview-me", "category": "business", "path": "skills/interview-me/" },
    { "name": "cross-border-listing-ma-finance-practice", "category": "finance", "path": "skills/cross-border-listing-ma-finance-practice/" },
    { "name": "cross-border-investment-financing-risk-control", "category": "finance", "path": "skills/cross-border-investment-financing-risk-control/" }
  ],
  "updated_at": "2026-05-29"
}"""
    with open("metadata.json", "w", encoding="utf-8") as f:
        f.write(metadata)
    print("  OK: metadata.json created")
    print()
    
    # Step 4: Create INDEX.md
    print("[4/5] Creating INDEX.md...")
    index = """# Personal Development Skills Collection

> True Unified Repository - All skills included locally

## Skills List

| # | Skill Name | Local Path |
|---|------------|------------|
| 1 | [Extreme Goal Achievement](skills/extreme-goal-achievement/) | skills/extreme-goal-achievement/ |
| 2 | [Supply Chain Negotiation](skills/supply-chain-negotiation-mastery/) | skills/supply-chain-negotiation-mastery/ |
| 3 | [Workplace Evaluation Art](skills/workplace-evaluation-art/) | skills/workplace-evaluation-art/ |
| 4 | [Interview Me](skills/interview-me/) | skills/interview-me/ |
| 5 | [Cross-border Listing](skills/cross-border-listing-ma-finance-practice/) | skills/cross-border-listing-ma-finance-practice/ |
| 6 | [Cross-border Investment](skills/cross-border-investment-financing-risk-control/) | skills/cross-border-investment-financing-risk-control/ |

## Quick Start

```bash
git clone https://github.com/wanglin1111111/personal-development-skills-collection.git
cd skills/extreme-goal-achievement/
```

---
**Updated**: 2026-05-29
**Total Skills**: 6
"""
    with open("INDEX.md", "w", encoding="utf-8") as f:
        f.write(index)
    print("  OK: INDEX.md created")
    print()
    
    # Step 5: Cleanup
    print("[5/5] Cleaning up...")
    if Path("temp_repos").exists():
        shutil.rmtree("temp_repos")
    print("  OK: temp directory removed")
    print()
    
    # Summary
    print("=" * 50)
    print("Fix Complete!")
    print("=" * 50)
    print()
    print("Fixed:")
    print(f"  - Cloned {cloned} external repos")
    print(f"  - Copied {copied} skills locally")
    print("  - Created metadata.json")
    print("  - Created INDEX.md")
    print("  - Updated directory structure")
    print()
    print("Next steps:")
    print("  git add -A")
    print("  git commit -m 'fix: convert to true unified repository'")
    print("  git push origin main")

if __name__ == "__main__":
    main()
