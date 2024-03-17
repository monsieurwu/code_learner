"""
第一步 引入模块
"""
from bs4 import BeautifulSoup
"""
接下来把字符串读取出来
使用with语法可以打开html 这样后面不用close 会自动关闭
fin.read可以读取整个文本
这样就实现了把html的文本读取到这个字符串里
"""
with open("./test.html") as fin:
    html_doc = fin.read()

"""
然后就要使用beautifulsoup
1.创建对象
第一个参数传入html_doc 第二个参数"html.parser" 第三个参数这里可以不传 因为这个文件默认编码是utf-8的 所以这里可以不传
"""

soup = BeautifulSoup(html_doc, "html.parser")

"""
2.查找所有节点
可以查找所有的超链接 直接传入一个a
就可以访问节点的名称 节点的属性 节点的文本内容
运行就会发现 名称就是a 属性就是url 内容就是对应的文本
"""


links = soup.find_all("a")
for link in links:
    print(link.name, link["href"], link.get_text())

"""
确认只有一个图片才能这么取 
直接print图片的属性 也就是url
"""
img = soup.find("img")
print(img["src"])

"""
正常我们的网页有很多很多的超链接 也有很多很多的图片
一般会先定位到区域块 比如
<div id="content" class="default">......</div>
先取到这个区域块的内容 
然后在这个区域块的本身里面再寻找超链接和图片
这样就把复杂度降低了
就可以先查找大的区块 再在大的区块里查找目标的数据
"""

print("#"*30)
"""
我们可以先查找div 然后在div的子区块里再查找url
在html中 一个节点如果有id属性的话 那么这个id是全局唯一的 如果有class属性的话 class一般不是全局唯一的
所以id代表某一个 class代表某一类
之后我们查找就可以把soup替换成div_node了
当然如果网页比较简单 直接soup.find_all就可以了
"""
div_node = soup.find("div", id="content")
print(div_node)
print("#"*30)

links = div_node.find_all("a")
for link in links:
    print(link.name, link["href"], link.get_text())

img = div_node.find("img")
print(img["src"])
