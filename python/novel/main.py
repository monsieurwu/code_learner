import requests
from bs4 import BeautifulSoup

def get_novel_chapters():
    root_url ="http://www.89wxw.cn/0_9/"
    r = requests.get(root_url)
    print(r.status_code)
    r.encoding="gbk"
    soup = BeautifulSoup(r.text,"html.parser")

    data = []
    for dd in soup.find_all("dd"):
        link = dd.find("a")
        if not link:
            continue
        # 加个元组
        data.append(("http://www.89wxw.cn%s"%link["href"], link.get_text()))
    return data
    # print(link)

# get_novel_chapters()
# 挨个打印每个章节的内容
for chapter in get_novel_chapters():
    print(chapter)
# 这样就返回一个列表 这个列表每个元素都是两个子元素 第一个是每个正文的链接 第二个是每个正文的标题
# 然后就可以去实现 每个标题对应的正文
    