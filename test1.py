import csv
import json
import codecs

'''
将json文件格式转为csv文件格式并保存。
'''
class Json_Csv():

	#初始化方法，创建csv文件。
    def __init__(self):
        self.save_csv = open('output.csv', 'w', encoding='utf-8', newline='')
        self.write_csv = csv.writer(self.save_csv, delimiter=',')  #以，为分隔符

    def trans(self,filename):
        with codecs.open(filename,'r',encoding='utf-8') as f:
            read=f.readlines()
            flag=True
            for index,info in enumerate(read):
                data=json.loads(info)
                if index <10000000: #读取json文件的前1千万行写入csv文件 。要是想写入全部，则去掉判断。
                    if flag: #截断第一行当做head
                        keys=list(data.keys())  #将得到的keys用列表的形式封装好，才能写入csv
                        self.write_csv.writerow(keys)
                        flag=False  #释放
                    value=list(data.values())   #写入values，也要是列表形式
                    self.write_csv.writerow(value)
            self.save_csv.close()  #写完就关闭


if __name__=='__main__':
    json_csv=Json_Csv()
    path='../Data/part-00000.json'
    json_csv.trans(path)