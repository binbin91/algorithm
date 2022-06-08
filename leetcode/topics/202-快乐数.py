# -*- coding: utf-8 -*-

def aa(n):
    s = set()
    while n not in s:
        s.add(n)
        tmp = sum((map(lambda x: int(x) ** 2, str(n))))
        if tmp == 1: return True
        n = tmp
    return False 


def bb(n):
    def calculate(num):
        sum = 0
        while num:
            sum += (num % 10) ** 2
            num = num // 10
        return sum
 
    record = set()
    while True:
        n = calculate(n)
        if n == 1: return True
        if n in record:
            return False
        else:
            record.add(n)

if __name__ == "__main__":
    print aa(19)
