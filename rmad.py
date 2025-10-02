# 去除文本中的广告 多余字符

import re


def clean_text(text):
    # 示例：去除特定广告语
    patterns = [
        r"本小说由.*?首发于.*?，请勿转载！",  # 示例广告语
        r"点击进入.*?阅读更多精彩内容！",  # 示例广告语
        r"（.*?）",  # 去除括号及其内容
        r"【.*?】",  # 去除方括号及其内容
        r"\s+"  # 多余空白字符,
        r'loadAdv\(\d, \d\)'
    ]
    
    for pattern in patterns:
        text = re.sub(pattern, "", text)
    # 去除多余空行
    text = re.sub(r"[\n\s]{2,}", "\n\n", text)
    return text.strip()

def test():
    sample_text = """
    loadAdv(2, 0)
    第1章 开始
    这是小说的正文内容。本小说由某某首发于某某网站，请勿转载！
    
    点击进入某某网站阅读更多精彩内容！
    
    （注：此处有注释）
    
    【广告：购买正版支持作者】
    
    第二段内容。
    """
    
    cleaned = clean_text(sample_text)
    # print("清理前：", sample_text)
    print("清理后：", cleaned)

if __name__ == "__main__":
    test()