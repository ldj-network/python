temp=('one','two','four','five','six')
temp = temp[:2] + ("three",) + temp[2:]
print(temp)
print(temp[:2])