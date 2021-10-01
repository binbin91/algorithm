# -*- coding: utf-8 -*-

# 递归 + 递归
# 字符串的全排列，对字符串中的每个元素都当作起始位置, 把其他元素当作以后的位置
# 然后再同样的进行操作，最终就会得到全排列

def aa(s):
    if not s:
        return []

    res = list()
    perm(s, res, '')
    return sorted(list(set(res)))


def perm(ss, res, path):
    if not ss:
        res.append(path)
        print 'res1=', res
        print '结束一轮'
    else:
        for i in range(len(ss)):
            print 'ss=', ss
            print 'res=', res
            print (ss[:i]+ss[i+1:], path+ss[i])
            perm(ss[:i]+ss[i+1:], res, path+ss[i])
         

if __name__ == "__main__":
    data = "abc" 
    print aa(data)
    #print aa("ab")
    #print aa("aab")
