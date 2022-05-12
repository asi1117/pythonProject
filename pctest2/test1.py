# #re模块 z
import  re
# # findall ：匹配字符串中的所有的符合正则的内容
# lis= re.findall(r"\d+", "我的电话15199669534")
# print(lis)
#
# #findter :匹配字符串中所有的内容【返回的是迭代器】
# it =re.finditer(r"\d+", "我的电话15199669534,10080")
# for i in  it:
#     print(i.group())
# #search 全文匹配，返回的结果是match对象，拿数据需要.group（）

# s = re.search(r"\d+", "我的电话15199669534,女朋友的电话是：10080")
# print(s.group())
#match 从头开始匹配
# 从头开始匹配s =re.match(r"\d+", "我的电话15199669534,女朋友的电话是：10080")
# print(s.group())
# 预加载正则表达式
# obj =re.compile(r"\d+")
# ret= obj.finditer("我的电话15199669534,女朋友的电话是：10080")
# for i in ret:
#     print(i.group())
# 想从正则里面提取一点内容
s='''
<div class='jacau'><span id='1'>郭麒麟</span></div>
<div class='jacau'><span id='2'>郭gagh</span></div>
<div class='jacau'><span id='3'>鸡鸡</span></div>
'''
#提取网页代码的方法 (?P<分组名字>正则) 可以单独从正则匹配的内容中进一步提取内容
obj =re.compile(r"div class='.*?'><span id='(?P<id>\d+)'>(?P<waha>.*?)</span></div>",re.S)#re.S:让.能匹配到换行
res=obj.finditer(s)
for i in res:
    print(i.group("waha"))
    print(i.group("id"))