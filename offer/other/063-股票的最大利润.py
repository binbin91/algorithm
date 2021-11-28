# -*- coding: utf-8 -*-

def aa(prices):
    cost, profit = float("inf"), 0
    for p in prices:
        cost = min(cost, p)
        profit = max(profit, p-cost)
    return profit


if __name__ == "__main__":
    print aa([7,1,5,3,6,4])
    print aa([7,6,4,3,1])
