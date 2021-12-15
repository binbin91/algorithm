# -*- coding: utf-8 -*-

# 分割字符串(split), 再倒序拼接字符串([::-1])

def aa(data):
    s = data.split(' ')
    res = []
    for i in s:
        if i != '':
            res.append(i)
    return ' '.join(res[::-1])

def bb(data):
    return ' '.join(data.strip().split()[::-1])

# 面试请用此解法
def cc(s):
    s = s.strip()   # 去除首尾空格
    i = j = len(s)-1
    res = []
    while i >= 0:
        while i >= 0 and s[i] != ' ':  # 搜索首个空格
            i -= 1
        res.append(s[i+1:j+1])  # 添加单词 
        while s[i] == ' ': # 跳过单词间空格
            i -= 1
        j = i  # 指向下个单词尾字符
    return ' '.join(res)  # 拼接
 

if __name__ == "__main__":
    data = "blue is the sky"
    print aa(data)
    print bb('student. a am I')
    print cc("mac book pro")
