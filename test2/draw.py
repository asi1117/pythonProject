import  matplotlib.pyplot as  plt
import  csv
ydata = []
xdata = []
j = 0
with open('data/participant01-Aircar.csv','r') as  f:
    data = csv.reader(f)
    readerdata =list(data)
    print(readerdata)
    for i in readerdata:
        ydata.append(i[0])
        xdata.append(j)
        j += 1
    print(ydata)
    print(xdata)
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.title('heart dump', fontsize=24)
plt.xlabel('s', fontsize=16)
plt.ylabel('heart_vlaue', fontsize=16)
plt.plot(xdata, ydata)
plt.savefig('data/test1.jpg')#一定要写到show前面 不然会出现存空图的情况
plt.show()