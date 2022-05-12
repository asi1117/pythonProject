#服务器加载的页面 1:直接拿页面源代码  request2:通过re来提取有效信息 re
import  requests
import  re

url="https://movie.douban.com/chart"
heders ={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
}
resp = requests.get(url,headers=heders)
page_content = resp.text
# print(page_content)
# 解析数据
obj = re.compile(r'.*<div class="">.*?<tr class="item">.*?<a class="nbg" href=".*?"  title="(?P<name>.*?)">.*',re.S)
res=obj.finditer(page_content)
for i in res:
    print(i.group("name"))