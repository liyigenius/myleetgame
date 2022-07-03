import math
from typing import List
from functools import lru_cache

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        """
        nums = [1,-1,-2,4,-7,3], k = 2
        :param nums:
        :param k:
        :return:
        """
        pass
        self.l = nums
        self.end = len(nums) - 1
        self.k = k
        if k >= len(nums):
            cnt = 0
            for i in nums:
                if i > 0:
                    cnt += i
            return cnt

        ans = self.getAns(self.end)
        return ans

    @lru_cache(None)
    def getAns(self, cur):
        if cur == 0:
            return self.l[cur]
        ok = -math.inf
        for i in range(max(0, cur- self.k), cur):
            ok = max(ok, self.getAns(i))
        res = self.l[cur] + ok
        return res

a = Solution()
print(a.maxResult(nums = [1,-1,-2,4,-7,3], k = 2))