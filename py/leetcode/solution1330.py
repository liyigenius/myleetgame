from typing import List


class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        """

        :param nums:
        :return:
        """
        cnt1 = 0
        for (k,v) in enumerate(nums):
            if k == 0:
                continue
            cnt1 += abs(v - nums[k-1])

        for (k,v) in enumerate(nums):
            if k == 0:
                continue

