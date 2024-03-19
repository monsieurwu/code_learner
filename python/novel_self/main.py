import requests
from bs4 import BeautifulSoup

def get_novel_chapters():
    root_url = "https://www.readnovel.com/book/12110374803718803"
    r = requests.get(root_url)
    print(r.status_code)
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
            print(f"链接：{href}, 标题：{text}")
            data.append(("http://www.89wxw.cn%s"%href, text))
    return data
        

    #     if not link:
    #         continue
    #     data.append((link["href"], link.get_text))
    # print(data)
    # return data
    # print(link)


    # print(links)
    # fout.close()


get_novel_chapters()