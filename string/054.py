# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        self.s = ''
        self.data = set()

    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            if self.data[i] == 1:
                return i
        return '#'

    def Insert(self, char):
        # write code here
        self.s = self.s+char
        if char in self.data:
            self.data[char] = self.data[char] + 1
        else:
            self.data[char] = 1

if __name__ == "__main__":
    data = "google"
    print aa(data)
