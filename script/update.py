from github import Github
import requests
import random
import time

# 名人名言 API 接口
api_url = "https://v1.hitokoto.cn/"
params = {
    "c": "i",
    "encode": "text"
}

# 创建 GitHub 对象
g = Github("your_access_token")

# 获取仓库和文件信息
repo = g.get_repo("vagmr/Guestbook")
file_path = "Guestbook/README2.md" 
file = repo.get_contents(file_path)

# 随机获取一条名言
response = requests.get(api_url, params=params)
quote = response.text.strip()

# 图片链接
image_url = "https://source.unsplash.com/960x640/?perseverance&victory"

# 创建 md 文件内容
new_content = f"## {time.strftime('%B %dth | %m月%d号')}\n\n### {quote}\n\n`{quote}`\n\n---\n<div style=\"background-color:#90ccd9;border-radius:5px;padding:10px;color:black;\">\n无论遇到多大困难和挫折，都要坚持下去，因为成功的胜利就在不远处等待着你的到来。\n</div>\n\n---\n\n![dream image]({image_url})"

# 更新 md 文件
repo.update_file(file.path, "commit message", new_content, file.sha)
