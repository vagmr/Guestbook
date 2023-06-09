from github import Github
import requests

# 创建GitHub对象
g = Github("access_token")

# 获取仓库和文件信息
repo = g.get_repo("your_username/your_repository")
file_path = "Guestbook/script/your_file_name.py" # 实际的脚本路径
file = repo.get_contents(file_path)

# 运行脚本
exec(file.decoded_content.decode('utf-8'))

# 图片链接
image_url = "https://source.unsplash.com/960x640/?perseverance&victory"

# 下载图片并上传到GitHub
response = requests.get(image_url)
repo.create_file("dream.jpg", "commit message", response.content)

# 更新md文件
new_content = f"{quote}\n\n![perseverance and victory]({image_url})"
repo.update_file(file.path, "commit message", new_content, file.sha)
