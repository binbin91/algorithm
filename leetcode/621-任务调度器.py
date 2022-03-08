# -*- coding: utf-8 -*-


# 思路: 完成所有任务的最短时间取决于出现次数最多的任务数量
# 解体步骤:
# 1. 计算任务次数
# 2. 找到出现次数最多的任务
# 3. 计算至少需要时间
# 4. 计算出现次数最多的任务总数
def aa(tasks, n):
    lg = len(tasks)
    if lg <= 1: return lg

    # 记录每个任务出现的次数
    tm = dict()
    for t in tasks: tm[t] = tm.get(t, 0) + 1

    # 按任务出现次数从大到小排序
    ts = sorted(tm.items(), key=lambda x: x[1], reverse=True)

    max_ts = ts[0][1]
    # 至少需要的最短时间
    res = (max_ts - 1) * (n + 1)
    
    for i in ts:
        if i[1] == max_ts: res += 1
    # 若结果比任务数量少, 则返回总任务数
    return res if res >= lg else lg 


if __name__ == "__main__":
    print aa(["A", "A", "A", "B", "B", "B"], 2)
    print aa(["A", "A", "A", "B", "B", "B"], 0)
    print aa(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2)
