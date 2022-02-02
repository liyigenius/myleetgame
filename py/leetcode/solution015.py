class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        pass
        nums = sorted(nums, )
        res= []
        for (k,v) in enumerate(nums):
            pass
            l,r = k+1, len(nums)-1
            while l < r:
                sig = v + nums[l] + nums[r]
                if sig == 0:
                    res.append([k,l,r] )
                    l+=1
                    r -=1
                if sig <0 :
                    l += 1
                if sig > 0 :
                    r -=1
        ll = set()
        for i in res:
            ll.add(  (nums[i[0]],nums[i[1]],nums[i[2]]  ) )
        return list(ll)