# 首先把请求的网址放到一个变量里
url = "https://tianqi.2345.com/Pc/GetHistory"
# 加上参数 复制payload的内容并改成字典的格式 加上”xxx“和逗号
# params = {
#     "areaInfo[areaId]": 54511,
#     "areaInfo[areaType]": 2,
#     "date[year]": 2014,
#     "date[month]": 6
# }
# 然后我们再设一个headers 里面方法user-agent
# 因为里面有可能有双引号 导致冲突 直接使用三引号就好了
headers = {
    "User-Agent" : """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36""",
    "Referer": "https://tianqi.2345.com/wea_history/54511.htm"
    # Referer这个HTTP请求头部用于指示一个请求是从哪个页面发起的。
    # 在网络爬虫或者API请求中，设置Referer头部可以模拟浏览器行为，因为正常用户浏览网页时，浏览器会自动添加这个头部。
    # 如果一个网站只允许从特定页面发起的请求访问某些资源，没有正确的Referer头部，请求可能会被拒绝。

}
# 准备完毕 开始爬取

import requests
import pandas as pd
# 定义一个函数 传入年份 月份 
# 把参数放进来
def craw_table(year, month):
    params = {
    "areaInfo[areaId]": 54511,
    "areaInfo[areaType]": 2,
    # 把年和月替换成我们的参数 爬取对应的表格数据
    "date[year]": year,
    "date[month]": month
}

    resp = requests.get(url, headers=headers, params=params)
    # 如果是200 说明请求成功
    # print(resp.status_code)
    # 然后就可以打印一下request到的内容
    # print(resp.text)
    data = resp.json()["data"]
    # print(data)

    # 提取一个字符串里的表格数据
    # import pandas as pd
    # 它直接就可以解析html 传入data字段 它可以解析这个网页中所有的表格 因为一个网页中会有很多个表格 我们取0 就是第一个表格
    # pandas的核心概念叫做data frame（df）
    # up主有专门的pandas的课程 后续可以学下
    df = pd.read_html(data)[0]
    # print(df.head())
    # 这个打印可以看到表格的前几行
    # 最后return一下df
    return df

# 设一个df_list的列表
df_list = []
for year in range(2020, 2024):
    for month in range(1, 13):
        # 我们来用一下这个方法
        df = craw_table(year, month)
        # print(df.head())
        # 想要合并打印出来
        df_list.append(df)
        # 到这步 这个df_list是很多年份的数据 然后就要把它合并已经保存到excel里
        # 加个print追踪下进度
        print("爬取：", year, month)
# 然后就要把它合并已经保存到excel里 pandas有现成的方法
pd.concat(df_list).to_excel("北京10年天气数据.xlsx", index=False)

