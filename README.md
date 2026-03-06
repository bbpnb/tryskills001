# tryskills001

> 🧪 OpenClaw Skills 测试项目

## 项目说明

这是一个测试仓库，用于开发和测试自定义的 **OpenClaw Skills**。

## 目标

- ✅ 开发个人常用的 Skill 模板
- ✅ 测试 Skill 功能和集成
- 实验 OpenClaw 的能力边界

## 可用 Skills

### 1. News Collector (新闻抓取)

📰 自动抓取新闻并整理成 JSON 格式

**安装依赖：**
```bash
pip install -r requirements.txt
```

**使用方法：**
```bash
# 抓取新闻并输出到控制台
python news_collector.py --query "Iran war"

# 保存到文件
python news_collector.py -q "Trump" -o news/trump-news.json

# 指定数量
python news_collector.py -q "AI technology" -l 10
```

**在 OpenClaw 中：**
直接说 "抓取伊朗战争的新闻" 或 "帮我查 Trump 的新闻，保存到 news 目录"

**详细文档：** 见 [SKILL.md](SKILL.md)

---

### 2. 计划添加的 Skills

- [ ] 天气查询增强版
- [ ] GitHub 自动化工具
- [ ] 文件整理助手
- [ ] 代码审查助手

## 项目结构

```
tryskills001/
├── README.md              # 项目说明
├── SKILL.md               # Skill 使用文档
├── news_collector.py      # 新闻抓取脚本
├── requirements.txt       # Python 依赖
└── news/                  # 新闻数据目录
    ├── iran-news-2026-03-07.json
    └── ai-news-test.json
```

## 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/bbpnb/tryskills001.git
cd tryskills001
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 运行 Skill

```bash
python news_collector.py -q "你的关键词" -o news/output.json
```

### 4. 在 OpenClaw 中使用

将 `news_collector.py` 复制到 OpenClaw workspace，然后在聊天中直接说：
- "用 news_collector 抓取 AI 新闻"
- "帮我查今天的科技新闻"

## 配置新闻 API (可选)

要获取真实新闻，需要配置新闻 API：

### NewsAPI
1. 注册：https://newsapi.org/
2. 获取 API key
3. 在 `news_collector.py` 中取消注释 NewsAPI 相关代码
4. 填入你的 API key

### GNews API
1. 注册：https://gnews.io/
2. 免费层：100 次/天
3. 在代码中配置 API key

## 技术栈

- **Python 3.8+** - 脚本语言
- **OpenClaw** - AI 代理框架
- **requests** - HTTP 请求
- **beautifulsoup4** - HTML 解析 (可选)

## 贡献

欢迎提交 Issue 和 PR！

## 许可证

MIT License

---

_由 ccc (Qwen3.5-Plus) 协助创建和维护_
