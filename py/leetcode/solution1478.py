import math
from typing import List


class Solution:
    def __init__(self):
        self.m1 = {}
        self.m2 = {}

    def minDistance(self, houses: List[int], k: int) -> int:
        """

        :param houses:
        :param k:
        :return:
        """
        pass
        if k >= len(houses):
            return 0
        houses.sort()
        ans = self.getAns(houses, k)
        return ans

    def getAns(self, house, k):
        ct = tuple(house)
        if (ct, k) in self.m2:
            return self.m2[(ct, k)]

        if k == 1:
            pass
            res = self.getHelper(house)
            self.m2[(ct, k)] = res
            return res
        res1 = math.inf
        for i in range(1, len(house)):
            left = house[:i]
            right = house[i:]
            res = self.getAns(left, 1) + self.getAns(right, k - 1)
            res1 = min(res1, res)
        self.m2[(ct, k)] = res1
        return res1

    def getHelper(self, house):
        ct = tuple(house)
        if ct in self.m1:
            return self.m1[ct]

        cnt = 0
        tag = -1
        if len(house) % 2 != 0:
            mid = len(house) // 2
            tag = house[mid]
        else:
            v1 = len(house) // 2
            tag = house[v1]
        for i in house:
            cnt += abs(i - tag)
        self.m1[ct] = cnt
        return cnt