#对字符串中敏感词进行替换。要求：根据需要定义一个敏感词库，例如：words=(‘暴力’，‘非法’，‘攻击’)，
# 然后用户输入一个字符串，如果该字符串中有words中的敏感词汇，将对该字符串进行敏感词汇的替换（用***代替敏感词汇），
# 最后把替换后的字符串打印出来，并写入“test.txt”文件。
def display(mgc):
    words = ('暴力','非法','攻击')
    for i in words:
        mgc = mgc.replace(i,'***')
    return mgc

a = '‘暴力’，‘非法’，‘攻击’,you ? qqkkk攻击'
print(display(a))