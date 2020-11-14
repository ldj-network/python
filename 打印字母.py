from collections import OrderedDict
import random
lst1 = [chr(i) for i in range(ord('a'),ord('z')+1)]
length = len(lst1)
n = 2
lst2 = []
od = OrderedDict()
for i in range(10):
    str1 = ''
    for i in range(n):
        index = random.randrange(length)
        str1 += lst1[index]
    else:
        lst2.append(str1)
lst2 = sorted(lst2,reverse=True)
print(lst2,end='\n\n')

for k in lst2:
    od.setdefault(k,0)
    od[k] += 1
else:
    print(od)
