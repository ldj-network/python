a = input("请输入字典")
b = eval(a)
print(b)
max(b.values())
for key,value in b.items():
    if(value == max(b.values())):
        print(key,value)