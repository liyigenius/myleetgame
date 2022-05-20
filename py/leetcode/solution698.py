from typing import List
from functools import lru_cache

class Solution:
    def __init__(self):
        pass

    def canPartition(self, nums: List[int]) -> bool:
        pass

        sum1 = sum(nums)
        if sum1 %2 != 0:
            return False
        target = sum1 // 2
        for i in nums:
            if i > target:
                return False
        self.tar = target
        self.nums = nums
        return self.checkOK(0, 0)

    @lru_cache(None)
    def checkOK(self, idx, prev):
        if len(idx) == len(self.nums):
            if prev == self.tar:
                return True
            return False
        if prev > self.tar:
            return False
        v1 = self.checkOK(idx+1, prev)
        v2 = self.checkOK(idx+1, prev+self.nums[idx])
        return v1 or v2

