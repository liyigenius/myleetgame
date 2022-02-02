class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        set1 = set()
        for (k1,v1) in enumerate(nums):
            for j in range(k1+1, len(nums)-2):
                l,r = j+1, len(nums) -1
                while l <r:
                    if v1 + nums[j] + nums[l] + nums[r] == target:
                        set1.add((nums[k1],nums[j], nums[l], nums[r]))
                        l+=1
                        r-=1
                    if v1 + nums[j] + nums[l] + nums[r] < target:
                        l+=1
                    if v1 + nums[j] + nums[l] + nums[r] > target:
                        r -=1
        ll = []
        for i in set1:
            ll.append( list(i)  )
        return ll
