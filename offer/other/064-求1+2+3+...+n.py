# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        self.res = 0

    def sum(self, n):
        n > 1 and self.sum(n-1)
        self.res += n
        return self.res


if __name__ == "__main__":
    n = 3
    aa = Solution()
    print aa.sum(n)
