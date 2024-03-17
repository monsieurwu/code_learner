class UrlManager():
    """
    url管理器
    可以使用两个python set来定义待爬行的url和爬取过的url的集合 
    old的是来自new的 当爬取完一个url就可以把这个url从new放到old的set里
    同时也需要把这个url从new中去除掉
    """
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
    
    """
    首先初始化 对自己进行初始化
    """
    """
    1.新增url 2.取出待爬取的url 
    """
    """
    首先判断这个url是否合格 不合格就不让它添加了
    接下来需要判断这个url是不是已经在容器里面了 只要在这里面 就不添加了
    """
    def add_new_url(self, url):
        if url is None or len(url) == 0:
            return
        if url in self.new_urls or url in self.old_urls:
            return
        self.new_urls.add(url)


    """
    一般取出来的url是很多个 这是新增url的两个方法 因为网页中解析出来的可能会是很多个 就加一个urls的
    这样就是批量添加url的方法
    """
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    """
    也需要得到爬取到待爬取的url的方法
    pop可以从集合里移除一个元素 并且返回
    取完这个url之后 把这个url标记为已爬取
    否则 如果容器里没有url了的话 return None
    """
    def get_url(self):
        if self.has_new_url():
            url = self.new_urls.pop()
            self.old_urls.add(url)
            return url
        else: 
            return None

    """
    判断get_url中得到的新增的url在管理器里有没有
    """
    def has_new_url(self):
        return len(self.new_urls) > 0

    """
    这样就定义完了这个类要向外提供的所有方法
    """
    
    
    
    
    """
    这样可以写一段测试代码
    下面if __name__ == "__main__": 加上这个判断的作用是 如果别的模块引用这个模块 就不会引入和执行下面的代码
    """

if __name__ == "__main__":
    """
    首先创建对象
    """
    url_manager = UrlManager()

    url_manager.add_new_url("url1")
    url_manager.add_new_urls(["url1", "url2"])
    print(url_manager.new_urls, url_manager.old_urls)
    
    print("#"*30)
    """
    测试从中取一个url
    """
    new_url = url_manager.get_url()
    print(url_manager.new_urls, url_manager.old_urls)
    print(url_manager.has_new_url())
    
    print("#"*30)
    """
    再从中取一个url
    """
    new_url = url_manager.get_url()
    print(url_manager.new_urls, url_manager.old_urls)
    print(url_manager.has_new_url())
    
    print("#"*30)

    print(url_manager.has_new_url())