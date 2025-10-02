from flask import Flask, request, jsonify
import re
import os

from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

OUTPUT_FILE = "story.txt"

def extract_chapter(text):
    """
    简单正则：匹配章节名和正文
    章节名示例： 第1章 xxx / 第一章 xxx
    """
    pattern = r"(第[一二三四五六七八九十百零\d]+[章回节].*?)(?:\n+)([\s\S]*?)(?=第[一二三四五六七八九十百零\d]+[章回节]|$)"
    matches = re.findall(pattern, text)

    chapters = []
    for title, content in matches:
        chapters.append({"title": title.strip(), "content": content.strip()})
    return chapters[0]['title']


@app.route("/upload", methods=["POST"])
def upload():
    data = request.json
    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data["text"]
    

    # 追加写入
    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        
        f.write(text)
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        full_text = f.read()
    return jsonify({"message": "ok", "count": len( full_text ),"chapters": extract_chapter(text)}), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
