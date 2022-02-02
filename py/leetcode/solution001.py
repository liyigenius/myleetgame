from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m1= {}
        for (k,v) in enumerate(nums):
            m1[v] = k
        for (k,v) in enumerate(nums):
            if target - v in m1 and m1[target - v ] != k:
                return [ k,  m1[target - v ] ]