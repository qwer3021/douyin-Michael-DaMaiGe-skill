# douyin-blogger-kb

抖音博主视频知识库 Skill。输入抖音博主分享链接（`v.douyin.com/xxx`）或主页地址，自动解析博主 → 用浏览器浏览主页 → 抓取前 N 个视频的文字/文案 → 建立本地 Markdown 知识库；之后可基于知识库回答关于该博主视频内容的问题。

## 安装

把本目录 `douyin-blogger-kb` 放到 agent 的 `.user_skills/` 目录下（例如 `<workspace>/.user_skills/douyin-blogger-kb/`），重启会话即可被识别。

## 使用

- **建立知识库**：提供抖音博主分享短链或主页地址，技能会自动解析链接、进入博主主页、抓取前 N 个视频的标题与完整文案，写入 `kb/<昵称>_<抖音号>.md`。
- **问答**：直接问“某博主视频里讲过什么”，技能从知识库检索并作答，标注信息出自哪个视频。

## 目录结构

```
douyin-blogger-kb/
├── SKILL.md                    # 技能主流程（建立 / 问答）
├── scripts/
│   └── resolve_douyin.py       # 分享短链 → sec_uid 解析（纯 HTTP）
├── references/
│   └── douyin-tips.md          # 抖音主页/视频页浏览器抓取细节
└── kb/                         # 已建立的知识库（个人数据，默认不入库）
```

## 依赖

- 抓取抖音需要带浏览器（`aha_browser_use` / `browser-use-automation`）的执行环境；当前环境无浏览器时切换到可用环境。
- 短链解析脚本为纯 HTTP，无第三方依赖（Python 3 标准库）。

## 说明

- 文案以页面实际读到的原文为准，不做改写；话题标签（#...）保留。
- `kb/` 为运行时生成的知识库数据，已在 `.gitignore` 中排除，不入库。
