import requests
from bs4 import BeautifulSoup

def get_novel_chapters():
    root_url = "https://www.readnovel.com/book/12110374803718803"
    r = requests.get(root_url)
    # print(r.status_code)
    if r.status_code == 200:
            print("request success!!!")
    else:
        # 如果状态码不等于200，执行这里的代码
        print("request fail!!!")
        return

    soup = BeautifulSoup(r.text,"html.parser")
    # print(soup)
    
    
    links = soup.find_all("div", class_ = "volume")
    # fout = open("craw_all_chapter.txt", "w")
    # fout.write("%s\n"%(links))
    # fout.flush()
    data = []
    for li in soup.find_all('li'):
        link = li.find("a")
        if link:
            href = link["href"]
            text = link.text
            # print(f"链接：{href}, 标题：{text}")
            if href.startswith("/chapter/12110374803718803/"):
                data.append(("https://www.readnovel.com%s"%href, text))
    return data
        

    #     if not link:
    #         continue
    #     data.append((link["href"], link.get_text))
    # print(data)
    # return data
    # print(link)


    # print(links)
    # fout.close()


def get_chapter_content(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    # return soup.find("div", id='content').get_text()
    chapter_content = soup.find("div", id='j_chapterBox')
    if chapter_content is not None:
        # print chapter_content.get_text()
        return chapter_content.get_text()
    else:
        return "未找到章节内容"
    # return soup.find("div", id='j_chapterBox').get_text()
    # print(soup.find("div", id='j_chapterBox').get_text())

    


# novel_chapters = get_novel_chapters()
# total_cnt = len(novel_chapters)
# idx = 0
# for chapter in novel_chapters:
#     idx += 1
#     print(idx, total_cnt)

#     url, title = chapter
#     # print("%s\t%s"%(title,url))
#     # with open("/mnt/d/doc/工作笔记/2024/code_learner/python/novel_self/text/%s.txt"%title, "w")as fout:
#     #     fout.write(get_chapter_content(url))
#     # fout.close()
#     # print("%s"%get_chapter_content(url))
#     # print(get_chapter_content(url))
#     # get_chapter_content("https://www.readnovel.com/chapter/12110374803718803/33253089373681294")
# with open("/mnt/d/doc/工作笔记/2024/code_learner/python/novel_self/text/first_novel.txt", "w")as fout:
#     fout.write(get_chapter_content(url))


novel_chapters = get_novel_chapters()
total_cnt = len(novel_chapters)
idx = 0

# 打开一个文件用于写入所有章节
with open("all_chapters.txt", "w") as fout:
    for chapter in novel_chapters:
        # 打印一下进度
        idx += 1
        percentage = (idx / total_cnt) * 100
        print(f"{percentage:.2f}%")
        # print(idx, total_cnt)
        
        url, title = chapter
        # 向文件中写入章节标题和内容
        fout.write(f"章节 {idx}: {title}\n\n")  # 写入章节标题
        fout.write(get_chapter_content(url) + "\n\n")  # 写入章节内容和两个换行符以分隔章节
        fout.flush()
print("Downloading Finished!!!!!!!!!!!!!!!!!!!!!")

# 注意：这个例子假设`get_chapter_content(url)`函数会返回对应URL章节的内容。
# 现在所有章节将会依次写入`all_chapters.txt`文件中。
