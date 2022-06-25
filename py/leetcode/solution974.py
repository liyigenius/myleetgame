from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        nums = [4,5,0,-2,-3,1], k = 5
        :param nums:
        :param k:
        :return:
        """
        dp = {}
        dp[0] = 1
        cache = 0
        cnt = 0
        for (k2,v) in enumerate(nums):
            cache += v
            toFind = cache % k
            res1 = dp.get(toFind, 0)
            cnt += res1
            dp[toFind] = res1 + 1
        return cnt

a = Solution()
print(a.subarraysDivByK(nums = [4,5,0,-2,-3,1], k = 5))

