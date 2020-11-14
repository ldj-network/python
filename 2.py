n = input("请输入数字")
dic = {}
for i in range(len(n)):
    if n[i] not in dic:
        dic[n[i]] = 1
    else:
        dic[n[i]] += 1
print(dic)

#第二种方法
from collections import OrderedDict
num = input('输入数字')
od = OrderedDict()

for k in num:
    od.setdefault(k,0)
    od[k] += 1
print(od)
