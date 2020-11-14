from collections import OrderedDict
import random
lst = sorted([(random.randint(-1000,1000))for i in range(10)])
print(lst,end='\n\n')
od = OrderedDict()
for k in lst:
    od.setdefault(k,0)
    od[k] += 1
print(od)