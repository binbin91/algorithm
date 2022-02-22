# -*- coding: utf-8 -*-

# 排序 + 贪心
def aa(intervals):
    intervals.sort(key=lambda x: x[0]) # 按照左区间从小到大
    res = [intervals[0]]
    for i in range(1, len(intervals)):
        last = res[-1]
        if last[1] >= intervals[i][0]:
            res[-1] = [last[0], max(last[1], intervals[i][1])]
        else:
            res.append(intervals[i])
    return res


if __name__ == "__main__":
    print aa([[1,3], [2,6], [8,10], [15,18]])
    print aa([[1,4], [4,5]])
