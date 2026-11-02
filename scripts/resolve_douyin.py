#!/usr/bin/env python3
"""把抖音分享短链解析成博主主页地址与 sec_uid。

用法:
    python resolve_douyin.py "https://v.douyin.com/xxxx/"
输出 (JSON):
    {"final_url": "...", "sec_uid": "MS4wLjAB...", "author_url": "https://www.douyin.com/user/<sec_uid>"}

兼容两种输入:
  1. 短链  https://v.douyin.com/xxxx/
  2. 已解析的用户页 https://www.iesdouyin.com/share/user/<sec_uid>?...
  (也接受 https://www.douyin.com/user/<sec_uid> 直接返回)

仅做 HTTP 重定向解析, 不进入浏览器。若脚本失败(网络/反爬), 交给浏览器直接打开短链再读取最终 URL。
"""

import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

UA = (
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
)

# 常见短链/分享域名, 命中即需跟随重定向
_SHORT_HOSTS = (
    "v.douyin.com",
    "www.iesdouyin.com",
    "iesdouyin.com",
    "www.douyin.com",
)


def _request(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return req


def resolve(url):
    url = url.strip()
    if url.startswith("https://www.douyin.com/user/"):
        return url, _sec_uid_from_url(url)

    current = url
    for _ in range(12):
        req = _request(current)
        try:
            resp = urllib.request.urlopen(req, timeout=25)
        except urllib.error.HTTPError as e:
            if e.code in (301, 302, 303, 307, 308):
                loc = e.headers.get("Location")
                if not loc:
                    raise
                current = urllib.parse.urljoin(current, loc)
                continue
            raise
        current = resp.geturl()
        break
    return current, _sec_uid_from_url(current)


def _sec_uid_from_url(u):
    m = re.search(r"(?:sec_uid=|/user/)(MS4wLjAB[0-9A-Za-z_-]+)", u)
    return m.group(1) if m else None


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "usage: python resolve_douyin.py <douyin-share-url>"}))
        sys.exit(2)
    url = sys.argv[1]
    try:
        final_url, sec_uid = resolve(url)
    except Exception as e:  # noqa: BLE001
        print(json.dumps({"error": str(e), "input": url}))
        sys.exit(1)

    result = {
        "input": url,
        "final_url": final_url,
        "sec_uid": sec_uid,
        "author_url": f"https://www.douyin.com/user/{sec_uid}" if sec_uid else None,
    }
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
