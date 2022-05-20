import math
from typing import List
from functools import lru_cache

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """
        nums = [7,2,5,10,8], m = 2
        :param nums:
        :param m:
        :return:
        """
        pass
        self.nums = nums
        prevM = {}
        prevM[-1] = 0
        delta = 0
        for (k,v) in enumerate(nums):
            delta += v
            prevM[k] = delta
        self.prevM = prevM
        res = self.getMin(0, len(nums), m)
        return res

    @lru_cache(None)
    def getMin(self,l,r, m):
        if m == 1:
            dt = self.prevM[r-1] - self.prevM[l-1]
            return dt
        if m == 2:
            v1 = math.inf
            for i in range(l,r):
                t1 =  self.prevM[i-1] - self.prevM[l-1]
                t2 = self.prevM[r-1] - self.prevM[i-1]
                vv = max(t1,t2)
                v1 = min(v1, vv)
            return v1
        v1 = math.inf
        for i in range(l,r):
            t1 = self.prevM[i-1] - self.prevM[l-1]
            t2 = self.getMin(i,r, m-1)
            vv = max(t1,t2)
            v1 = min(v1, vv)
        return v1

a = Solution()
print(a.splitArray(nums = [1,4,4], m = 3))