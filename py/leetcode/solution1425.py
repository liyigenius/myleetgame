import math
from typing import List
import math
from sortedcontainers import SortedList

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k2: int) -> int:
        """
        nums = [10,2,-10,5,20], k = 2
        :param nums:
        :param k:
        :return:
        """
        dp = {}
        sd = SortedList()

        if k2 >= len(nums):
            cnt = 0
            for i in nums:
                if i >=0:
                    cnt += i
            if cnt == 0:
                return max(nums)
            return cnt
        for (k,v ) in enumerate(nums):
            if k == 0:
                dp[k] = v
                sd.add(v)
                continue
            else:
                cur = v
                maxone = sd[-1]
                cur = max(cur, maxone + v )
                dp[k] = cur
                if len(sd) < k2:
                    sd.add(cur)
                    continue
                else:
                    first = dp[k-k2]
                    sd.remove(first)
                    sd.add(cur)


                # for j in range(k-k2, k):
                #     if j <0:
                #         continue
                #     prev1 = dp[j]
                #     cur = max(cur, prev1 + v )

        rest = list(dp.values())
        ans = max(rest)
        return ans


a = Solution()
print(a.constrainedSubsetSum(nums = [10,-2,-10,-5,20], k2 = 2))
