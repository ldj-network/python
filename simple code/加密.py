def encryption(word):
    wordList = list(word)
    temp = []
    for i in wordList:
        temp.append(str((eval(i) +7)%10))
    temp[0],temp[2] = temp[2],temp[0]
    temp[1], temp[3] = temp[3], temp[1]
    newWord = ''.join(temp)
    return newWord
word = input("请输入需要加密的四位数字")
print('你输入的数字为：{},加密后的数字为：{}' .format(word,encryption(word)))