#安装 pip install bs4

import requests
from bs4 import  BeautifulSoup
import  csv
url="https://movie.douban.com/chart"
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
}
resp =requests.get(url,headers=headers)

# print(resp.text)
#解析数据
#1:第一步将页面源代码交给
page =BeautifulSoup(resp.text,"html.parser") #指定html解析器
#2从bs对象中查找数据
#find(标签，属性-值)
#find_all(标签，属性-值)
# a = page.find_all("a", attrs={"class": "nbg"})
div_list = page.find_all("div", class_="pl2")
with open("douban.csv","w",encoding='utf-8_sig' ) as f:
    write = csv.writer(f)
    for i in  div_list:
        title =i.a.span.text
        write.writerow(title)
resp.close()
print("over")