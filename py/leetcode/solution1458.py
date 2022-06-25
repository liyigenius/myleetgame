import math
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        """
        nums1 = [2,1,-2,5], nums2 = [3,0,-6]
        :param nums1:
        :param nums2:
        :return:
        """
        dp = {}
        dp[(0,0)] = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                v1 = nums1[i] * nums2[j]
                v2 = dp.get((i-1,j-1), -math.inf)
                v3 = dp.get((i-1,j), -math.inf)
                v4 = dp.get((i,j-1), -math.inf)
                dp[(i,j)] = max( v1, v2, v1 + v2, v3, v4, )
        last = (len(nums1)-1, len(nums2)-1)
        res = dp[last]
        return res


a = Solution()
print(a.maxDotProduct([5,-4,-3],
[-4,-3,0,-4,2]))