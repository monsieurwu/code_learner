"""
定义入口url
"""

from bs4 import BeautifulSoup
import requests
import url_manager
import re
# 首先定义入口url

root_url = "https://dict.eudic.net/"
"""
定义一个urlManager
快捷键可以引入这个模块
"""
urls = url_manager.UrlManager()
# 把这个root url放到urlmanager里面
urls.add_new_url(root_url)
# 把结果写到文件里
fout = open("craw_all_pages.txt", "w")
# 这时候 我们已经初始化了urlmanager 我们就可以一直从里面取出我们的url进行爬取 把新的链接放到这个url管理器里
while urls.has_new_url():
    # 有就取出
    curr_url = urls.get_url()
    # 实现这个url的爬取 因为我们要爬取很多的网站 为了防止卡在某一个上 加一个timeout属性
    r = requests.get(curr_url, timeout=3)
    # 如果request失败的话
    if r.status_code != 200:
        print("error, return status_code is not 200", curr_url)
        continue

    # 这时候就说明爬取成功了 我们就可以解析这个网页 得到我们要的数据
    # 传入r.txt
    soup = BeautifulSoup(r.text, "html.parser")
    # soup.title可以得到title这个节点 。string可以得到里面的文字
    title = soup.title.string

    fout.write("%s\t%s\n"%(curr_url, title))
    # 因为写出的时候 经常会缓存一部分数据在内存 最后才批量写出到磁盘 如果想很快看到信息可以用flush 也就是把内存中的数据刷到磁盘里
    fout.flush()
    # 同时 成功爬取的时候 我们可以把url管理器里面的数目打印一下
    print("success:%s, %s, %d"%(curr_url, title, len(urls.new_urls)))
# 这样 我们就实现了这个url的爬取 解析 以及目标数据的获取和写出
# 还有件事 就是不能忘了把这个页面中新的url中提取出来 放到url管理器里 这样 这个管理器才能一直不停的运行
    # 我们使用find all所有的链接来进行
    links = soup.find_all("a")
    for link in links:
        # 因为有些超链接是不标准的 这个href可能取不到 就continue 不管这个url了
        # href = link["href"]
        href = link.get("href")
        if href is None:
            continue

        # 判断是不是我们要的文章的url 就需要用正则表达式来判断
        pattern = r'^http://www.crazyant.net/\d+.html$'
        if re.match(pattern, href):
            # 如果匹配的话 我们再把这个url添加到url管理器里面
            urls.add_new_url(href)

fout.close()

