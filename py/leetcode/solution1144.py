from typing import List


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        """
        nums = [9,6,1,6,2]
        :param nums:
        :return:
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if nums[0] == nums[1]:
                return 1
            return 0
        v1 = self.getV1(nums)
        v2 = self.getV2(nums)
        print(v1, v2)
        return min(v1, v2)

    def getV1(self, nums):
        cnt = 0
        for (k, v) in enumerate(nums):
            if k % 2 == 0:
                if k == 0:
                    pass
                    if nums[k + 1] <= v:
                        cnt += v - nums[k + 1]  + 1
                elif k == len(nums) - 1:
                    if nums[k - 1] >= v:
                        cnt += v - nums[k - 1]  + 1
                else:
                    tag1 = max(v - nums[k + 1] + 1, v - nums[k - 1] + 1)
                    tag1 = max(0, tag1)
                    cnt += tag1
        return cnt

    def getV2(self, nums):
        cnt = 0
        for (k, v) in enumerate(nums):
            if k % 2 == 1:
                if k == 0:
                    pass
                    if nums[k + 1] >= v:
                        cnt +=  nums[k + 1] - v + 1
                elif k == len(nums) - 1:
                    if nums[k - 1] >= v:
                        cnt +=  nums[k - 1] -v  + 1
                else:
                    tag1 = max( nums[k + 1] - v + 1 ,  nums[k - 1] -v  + 1 )
                    tag1 = max(0, tag1)
                    cnt += tag1
        return cnt


a  = Solution()
print(a.movesToMakeZigzag(nums = [2,1,2]))