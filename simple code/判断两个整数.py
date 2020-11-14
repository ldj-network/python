a = input("输入你要判断整数")
b = input("输入你要判断的整数")
if a > b :
    print(str(a),str(b))
else:
    print(str(b),str(a))
#编写程序,倒是无妨/，但是还是要自己与之相同！
def number(m,n):
    if m > n :
        print(str(m),str(n))
        if n > m:
            print(str(n), str(m))
            return

m = float(input("输入你要判断整数"))
n = float(input("输入你要判断的整数"))
number(m,n)
