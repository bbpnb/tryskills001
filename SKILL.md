# News Collector Skill

📰 自动抓取新闻并整理成 JSON 格式的 OpenClaw Skill

## 功能

- 搜索指定关键词的实时新闻
- 自动整理成结构化 JSON 格式
- 支持多种新闻源 (Google News, BBC 等)
- 可配置输出路径和数量限制

## 依赖

```bash
pip install requests beautifulsoup4
```

## 使用方法

### 基础用法

```bash
# 抓取新闻并输出到控制台
python news_collector.py --query "Iran war"

# 保存到文件
python news_collector.py -q "Trump" -o news/trump-news.json

# 指定数量和抓取方法
python news_collector.py -q "AI technology" -l 10 -m requests
```

### 参数说明

| 参数 | 简写 | 说明 | 默认值 |
|------|------|------|--------|
| `--query` | `-q` | 搜索关键词 (必填) | - |
| `--output` | `-o` | 输出文件路径 | 控制台输出 |
| `--limit` | `-l` | 抓取新闻数量 | 5 |
| `--method` | `-m` | 抓取方法 (browser/requests) | requests |

### 在 OpenClaw 中使用

在 OpenClaw 聊天中直接说：
- "抓取伊朗战争的新闻"
- "帮我查 Trump 的新闻，保存到 news 目录"
- "用 news_collector 抓取 10 条 AI 相关新闻"

OpenClaw 会自动调用这个脚本并处理结果。

## 输出格式

```json
{
  "title": "Iran war 相关新闻",
  "date": "2026-03-07",
  "query": "Iran war",
  "source": "Google News / BBC News / Al Jazeera",
  "news": [
    {
      "headline": "新闻标题",
      "summary": "新闻摘要",
      "category": "类别",
      "source": "来源",
      "source_url": "https://www.bbc.com/news/...",
      "timestamp": "2026-03-07T00:00:00"
    }
  ],
  "count": 5,
  "collected_by": "ccc (OpenClaw News Collector Skill)",
  "note": "自动抓取的新闻数据 - 包含信息来源链接"
}
```

**新增字段:**
- `source_url`: 新闻原文链接，方便查看完整报道和验证信息来源

## 高级用法

### 定时抓取 (配合 OpenClaw Heartbeat)

在 `HEARTBEAT.md` 中添加：
```markdown
- 每天早上 9 点抓取 Iran 新闻 → `python news_collector.py -q "Iran" -o news/iran-daily.json`
```

### 批量抓取多个主题

```bash
for topic in "Iran war" "Trump" "AI"; do
    python news_collector.py -q "$topic" -o "news/${topic// /-}.json"
done
```

### 集成到 GitHub Actions

创建 `.github/workflows/news-collect.yml` 自动定时抓取新闻。

## 注意事项

1. **网络要求**: 需要能访问 Google News 或 BBC
2. **速率限制**: 避免频繁请求，建议设置间隔
3. **数据准确性**: 自动抓取的内容可能需要人工校验
4. **OpenClaw 浏览器**: 使用 `browser` 方法需要 OpenClaw 浏览器服务运行

## 故障排除

| 问题 | 解决方法 |
|------|---------|
| 无法连接 Google News | 检查网络/代理设置 |
| 解析失败 | 尝试 `--method browser` |
| 输出文件为空 | 检查关键词是否有结果 |
| OpenClaw 无响应 | 重启 Gateway 服务 |

## 版本

- **v0.2.0** - 添加 source_url 字段，记录新闻原文链接
- **v0.1.0** - 初始版本，基础新闻抓取功能

## 作者

由 ccc (Qwen3.5-Plus) 为 OpenClaw 创建

## 许可证

MIT License
