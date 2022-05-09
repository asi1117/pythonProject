import  requests # get方法获取
query = input("请输入要搜索的明星名字")
url='https://zh.m.wikipedia.org/zh-hans/%E4%BA%94%E6%9D%A1%E4%BA%BA'
headers= {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
}
resp= requests.get(url,headers=headers)
print(resp)
print(resp.text)