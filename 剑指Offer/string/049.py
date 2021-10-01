# -*- coding: utf-8 -*-

def aa(data):
    s = data.strip() # 去除字符串首尾空格
    
    n, flag = 0, 1
    # 符号位判断和字符串去除首位
    if s[0] == '-':
        s = s[1:]
        flag = -1
    elif s[0] == '+':
        s = s[1:]

    # 遍历字符串, 若字符串属于数字, 进行拼接( 10 * n + c), 非数字直接返回0
    for c in s:
        if c >= '0' and c <= '9':
            n = 10 * n + int(c)
        else:
            return 0
    return n * flag 

if __name__ == "__main__":
    data = "1a33"
    print aa(data)
    print aa("+2147483647")
