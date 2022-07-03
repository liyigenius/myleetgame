from typing import List


class Solution:


    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        t1 = []
        for (k,v) in enumerate(nums1):
            t1.append(v - nums2[k])
        t2 = []
        for (k,v) in enumerate(nums2):
            t2.append((v - nums1[k]))
        ok1 = sum(nums1) + self.getMax(t2)
        ok2 = sum(nums2) + self.getMax(t1)
        return max(ok1, ok2)


    def getMax(self,ll):
        if len(ll) == 1:
            return max(0, ll[0])
        max1,so_far = max(0, ll[0]), max(0, ll[0])
        for i in range(1, len(ll)):
            so_far = max(so_far+ ll[i], ll[i] )
            max1 = max(max1, so_far)
        return max1

a = Solution()
print(a.maximumsSplicedArray(nums1 = [7,11,13], nums2 = [1,1,1]))