# douyin-Michael-DaMaiGe-skill

抖音博主视频知识库 Skill，**开箱即用**。随包内置博主「Michael大麦哥」的知识库，你直接问该博主视频里的内容就能得到基于原文的回答，无需提供抖音链接。也支持输入任意抖音博主分享链接（`v.douyin.com/xxx`）或主页地址，自动解析 → 浏览主页 → 抓取前 N 个视频文字 → 建立新的本地知识库。

## 安装

任选一种方式：

**方式一：下载压缩包（推荐，点开即下载）**

1. 打开 Release 发布页：`https://github.com/qwer3021/douyin-Michael-DaMaiGe-skill/releases/tag/v1.0.0`
   或直接点开下载直链：`https://github.com/qwer3021/douyin-Michael-DaMaiGe-skill/releases/download/v1.0.0/douyin-Michael-DaMaiGe-skill-v1.0.0.zip`
2. 解压 zip，得到文件夹 `douyin-Michael-DaMaiGe-skill`；
3. 把该文件夹放到 agent 的 `.user_skills/` 目录下（例如 `<workspace>/.user_skills/douyin-Michael-DaMaiGe-skill/`）；
4. 重启会话即可被识别，开箱即用。

**方式二：Git 克隆**

```bash
cd <你的workspace>/.user_skills
git clone https://github.com/qwer3021/douyin-Michael-DaMaiGe-skill.git
```

重启会话即可被识别。

## 使用

- **开箱即用（问答）**：直接问「Michael大麦哥视频里讲过什么」（例如"他怎么看待管理自己"），技能从内置知识库 `kb/抖音爆火的Michael大麦哥skill.md` 回答，标注出自哪个视频。也可指定其它已建立知识库的博主。
- **建立新知识库**：提供任意抖音博主分享短链或主页地址，技能会自动解析链接、进入博主主页、抓取前 N 个视频的标题与完整文案，写入 `kb/<昵称>_<抖音号>.md`，之后同样可问答。

## 目录结构

```
douyin-Michael-DaMaiGe-skill/
├── SKILL.md                    # 技能主流程（建立 / 问答）
├── scripts/
│   └── resolve_douyin.py       # 分享短链 → sec_uid 解析（纯 HTTP）
├── references/
│   └── douyin-tips.md          # 抖音主页/视频页浏览器抓取细节
└── kb/
    ├── .gitkeep                       # 目录占位
    └── 抖音爆火的Michael大麦哥skill.md  # 内置默认知识库（开箱即用）
```

## 依赖

- 抓取抖音需要带浏览器（`aha_browser_use` / `browser-use-automation`）的执行环境；当前环境无浏览器时切换到可用环境。
- 短链解析脚本为纯 HTTP，无第三方依赖（Python 3 标准库）。

## 说明

- 文案以页面实际读到的原文为准，不做改写；话题标签（#...）保留。
- `kb/` 内置了 Michael大麦哥 的默认知识库（开箱即用）；你新建的其它博主知识库默认不入库（在 `.gitignore` 排除），如需一并发布可自行放开。
