url = "http://www.crazyant.net"
"""
第一步 去获取这个url的文本
"""
import requests
r = requests.get(url)
"""
如果不等于200 就会直接退出这个程序
raise Exception 就是程序出现问题 不往下执行了
"""
if r.status_code != 200:
    raise Exception
"""
提取文档内容
"""
html_doc = r.text


"""
第二步 对取到的数据进行解析
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, "html.parser")
"""
正如分析 我们可以先查找h2的列表
"""
h2_nodes = soup.find_all("h2", class_ = "entry-title")
"""
h2_node就是一个超链接
所以可以继续进行查找
"""
for h2_node in h2_nodes:
    link = h2_node.find("a")
    print(link["href"], link.get_text())


"""
这样我们就查到了所有的h2 class限定为entry-title
然后对每个h2 我们查到了里面的超链接
最后打印每个超链接里面的url 以及它的文本内容
"""




