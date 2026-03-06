#!/usr/bin/env python3
"""
News Collector Skill for OpenClaw
抓取新闻并整理成 JSON 格式

用法:
    python news_collector.py --query "Iran war" --output news/iran-news.json
    python news_collector.py --query "Trump" --limit 10
"""

import json
import argparse
from datetime import datetime
from pathlib import Path
from typing import Optional

# 使用浏览器自动化 (需要 OpenClaw 环境)
# 或者使用 requests + BeautifulSoup 作为备选

def fetch_news_from_browser(query: str, limit: int = 5) -> list:
    """
    通过 OpenClaw 浏览器工具抓取 Google News
    
    注意：这个函数需要在 OpenClaw 环境中运行，
    或者需要手动实现浏览器自动化逻辑
    """
    # 这是在 OpenClaw 中通过 browser tool 实现的
    # 实际使用时会调用 browser tool 打开页面并截图/解析
    news_items = []
    
    # 示例数据结构
    sample_news = [
        {
            "headline": f"Sample news about {query}",
            "summary": "This is a sample news item",
            "category": "general",
            "source": "BBC News",
            "timestamp": datetime.now().isoformat()
        }
    ]
    
    return sample_news[:limit]


def fetch_news_with_requests(query: str, limit: int = 5) -> list:
    """
    使用 requests 抓取新闻 (备选方案)
    需要安装：pip install requests beautifulsoup4
    
    注意：Google News 需要 JavaScript，这里使用示例数据演示
    实际使用时可以集成新闻 API (如 NewsAPI, GNews 等)
    """
    try:
        import requests
        
        # 方案 1: 使用 NewsAPI (需要 API key)
        # API_KEY = "your_newsapi_key"
        # url = f"https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}"
        # response = requests.get(url, timeout=10)
        # data = response.json()
        # news_items = [
        #     {
        #         "headline": article["title"],
        #         "summary": article["description"] or "",
        #         "category": "general",
        #         "source": article["source"]["name"],
        #         "source_url": article["url"],
        #         "timestamp": article["publishedAt"]
        #     }
        #     for article in data.get("articles", [])[:limit]
        # ]
        # return news_items
        
        # 方案 2: 使用 GNews API (免费层)
        # API_KEY = "your_gnews_key"
        # url = f"https://gnews.io/api/v4/search?q={query}&apikey={API_KEY}"
        
        # 方案 3: 示例数据 (用于测试)
        print("[Info] 使用示例数据 (配置 API key 后获取真实新闻)")
        news_items = [
            {
                "headline": f"Breaking: Major development in {query}",
                "summary": f"Latest updates on {query} - experts analyze the situation",
                "category": "breaking",
                "source": "BBC News",
                "source_url": f"https://www.bbc.com/news/search?q={query.replace(' ', '+')}",
                "timestamp": datetime.now().isoformat()
            },
            {
                "headline": f"Analysis: What {query} means for the future",
                "summary": f"In-depth analysis of {query} and its implications",
                "category": "analysis",
                "source": "Reuters",
                "source_url": f"https://www.reuters.com/search/news?query={query.replace(' ', '+')}",
                "timestamp": datetime.now().isoformat()
            },
            {
                "headline": f"Live updates: {query} situation",
                "summary": f"Continuous coverage of {query}",
                "category": "live",
                "source": "CNN",
                "source_url": f"https://www.cnn.com/search?q={query.replace(' ', '+')}",
                "timestamp": datetime.now().isoformat()
            }
        ]
        
        return news_items[:limit]
        
    except Exception as e:
        print(f"[Error] Error fetching news: {e}")
        return []


def create_news_json(news_items: list, query: str, output_path: Optional[str] = None) -> str:
    """
    创建 JSON 格式的新闻文件
    
    Args:
        news_items: 新闻列表
        query: 搜索关键词
        output_path: 输出文件路径 (可选)
    
    Returns:
        JSON 字符串
    """
    data = {
        "title": f"{query} 相关新闻",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "query": query,
        "source": "Google News / BBC News / Al Jazeera",
        "news": news_items,
        "count": len(news_items),
        "collected_by": "ccc (OpenClaw News Collector Skill)",
        "note": "自动抓取的新闻数据 - 包含信息来源链接"
    }
    
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    
    if output_path:
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(json_str, encoding='utf-8')
        print(f"[Saved] 新闻已保存到：{output_path}")
    
    return json_str


def main():
    parser = argparse.ArgumentParser(
        description="News Collector - 抓取新闻并整理成 JSON 格式"
    )
    parser.add_argument(
        "--query", "-q",
        type=str,
        required=True,
        help="搜索关键词 (例如：'Iran war', 'Trump')"
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        default=None,
        help="输出文件路径 (例如：news/iran-news.json)"
    )
    parser.add_argument(
        "--limit", "-l",
        type=int,
        default=5,
        help="抓取新闻数量 (默认：5)"
    )
    parser.add_argument(
        "--method", "-m",
        type=str,
        choices=["browser", "requests"],
        default="requests",
        help="抓取方法 (browser=OpenClaw 浏览器，requests=HTTP 请求)"
    )
    
    args = parser.parse_args()
    
    print(f"[Search] 正在搜索：{args.query}")
    print(f"[Limit] 数量限制：{args.limit} 条")
    
    # 抓取新闻
    if args.method == "browser":
        news_items = fetch_news_from_browser(args.query, args.limit)
    else:
        news_items = fetch_news_with_requests(args.query, args.limit)
    
    if not news_items:
        print("[Error] 未找到相关新闻")
        return
    
    print(f"[Success] 找到 {len(news_items)} 条新闻")
    
    # 创建 JSON
    json_output = create_news_json(news_items, args.query, args.output)
    
    # 如果没有指定输出文件，打印到控制台
    if not args.output:
        print("\n" + "="*50)
        print(json_output)


if __name__ == "__main__":
    main()
