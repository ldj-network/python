a = str(input('输入三角形的a边'))
b = str(input('输入三角形的b边'))
c = str(input('输入三角形的c边'))
while a == b or b == c or c == a:
    print("这个三角形为等腰三角形")
    break
else:
    print("这个三角形不为等腰三角形")
#第二种方法，但是还是看自己的选择，不对，还是选择最短的才好！
if a == b:
    print("这个三角形为等腰三角形")
    if c == b:
        print("这个三角形为等腰三角形")
        if a == c:
            print("这个三角形为等腰三角形")
else:
    print("不是等腰三角形")
#第三种方法？
