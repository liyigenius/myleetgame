from typing import List
import math
from functools import lru_cache


class Solution:

    @lru_cache(None)
    def checkOK(self, a, b):
        res = math.gcd(a, b)
        return res != 1

    def __init__(self):
        self.ll = []

    def compresss(self, nn):
        ll = []
        prev = None
        for (k,v) in enumerate(nn):
            if k == 0:
                prev = v
                ll.append(v)
            else:
                if v == prev:
                    continue
                else:
                    prev = v
                    ll.append(prev)
        return ll

    def splitArray(self, nums: List[int]) -> int:
        """

        :param nums:
        :return:
        """
        res1 = self.compresss(nums)
        self.ll = res1
        res = self.iterAll(0)
        return res

    @lru_cache(None)
    def iterAll(self, idx):
        if idx == len(self.ll):
            return 0

        if self.checkOK(self.ll[idx], self.ll[-1]):
            return 1

        cnt = math.inf
        first = self.ll[idx]
        for k in range(idx , len(self.ll)):
            if self.checkOK(self.ll[k], first):
                ans = 1 + self.iterAll(k + 1)
                cnt = min(cnt, ans)
        return cnt


a = Solution()
print(a.splitArray(
[2,3,5,7]))
