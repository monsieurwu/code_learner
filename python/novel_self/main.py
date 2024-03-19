import requests
from bs4 import BeautifulSoup

def get_novel_chapters():
    root_url = "https://www.readnovel.com/book/12110374803718803"
    r = requests.get(root_url)
    print(r.status_code)
    soup = BeautifulSoup(r.text,"html.parser")
    # print(soup)
    
    
    links = soup.find_all("div", class_ = "volume")
    fout = open("craw_all_chapter.txt", "w")
    fout.write("%s\n"%(links))
    fout.flush()

    # for div in soup.find_all("div", class_ = "volume"):
    #     link = div.find("a")
    #     if not link:
    #         continue
    #     print(link)


    print(links)
    fout.close()


get_novel_chapters()