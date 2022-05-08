#需求 用程序模拟器，输入一个网址，从该网址中获取资源
from urllib.request import urlopen
url='https://translate.google.com/'
resp=urlopen(url)


with open("google.html" ,mode="w") as  f:
    f.write(resp.read().decode("utf-8"))#读取网页的页面源代码
print("over")