num = int(input('请输入计算的数字'))
if num%2 == 0:
    if num%3 == 0:
        print("这个数可以被2and3 整除")
    else:
        print('不能被三整除，可以被2整除')
elif num%3 == 0:
    print('可以被三整除')
else:
    print("不能被三和二整除")

#while 循环
sum = 0
i = 1
while i <=200:
    sum = sum +i
    i += 1
print("1 到200 之间的和为：%d" %(sum))
#看清程序的本质！
