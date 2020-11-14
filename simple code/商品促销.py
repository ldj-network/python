#错误的py。还是不知道，自己要在了解清楚吧！！！！,了解！！！now ok。
m = float(input('输入你的购物金额'))
s = 0
if m > float(3000):
    s = m * float(0.7)
    print('优惠价为：',str(s),)
elif m > float(2000):
    s = m * float(0.8)
    print('优惠价为：', str(s), )
elif m >= float(1000):
    s = m * float(0.9)
    print('优惠价为：', str(s), )