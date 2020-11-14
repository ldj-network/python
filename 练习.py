import re
my_enter=input("请输入字典（每一对键值之间用“|”分开）：")
my_dict={}		#定义一个空字典
my_enter=str(str(my_enter.split("|")).split(":"))		#先分离键值对，再分离键和值
my_enter=re.sub(" ",'',my_enter)
my_enter=re.sub("\[",'',my_enter)
my_enter=re.sub("\]",'',my_enter)
my_enter=re.sub("\"",'',my_enter)
my_enter=re.sub("\'",'',my_enter)		#把字符中其余元素去掉
my_enter=my_enter.split(",")		#最后把字符串转换成列表样式
for i in range(0,len(my_enter),2):
    my_dict[str(my_enter[i])] = my_enter[i+1]
#print(my_dict)
max(my_dict.values())
for key,value in my_dict.items():
    if(value == max(my_dict.values())):
        print(key,value)