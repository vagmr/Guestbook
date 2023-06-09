from github import Github
import requests

# 创建GitHub对象
g = Github("your_access_token")

# 获取仓库和文件信息
repo = g.get_repo("your_repository")
file = repo.get_contents("your_file_path")

# 从文件中获取名言
quote = file.decoded_content.decode("utf-8").strip()

# 图片链接
image_url = "https://source.unsplash.com/960x640/?perseverance&victory"

# 下载图片并上传到GitHub
response = requests.get(image_url)
repo.create_file("dream.jpg", "commit message", response.content)

# 更新md文件
new_content = f"{quote}\n\n![perseverance and victory]({image_url})"
repo.update_file(file.path, "commit message", new_content, file.sha)
