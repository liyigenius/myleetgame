from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        """
        nums = [1,4,6,8,10]
        :param nums:
        :return:
        """
        dp = {}
        dp[-1] = 0
        cache = 0
        cnt = 0
        for i in nums:
            cache += i
            dp[cnt] = cache
            cnt += 1
        ret = []
        for (k,v) in enumerate(nums):

            v1V = abs(dp[k] - dp[-1]  - nums[k]*(k+1)  )
            v2V = abs(dp[len(nums)-1] - dp[k]  - nums[k] * (len(nums)-1 - k)  )
            res = v1V + v2V
            ret.append(res)

        return ret

a = Solution()
print(a.getSumAbsoluteDifferences(nums = [1,4,6,8,10]))