from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = sorted(nums)
        a1 = len(a)//2 + 1
        ll1,ll2= a[:a1],a[a1:]
        print(ll1,ll2)
        ll1.reverse()
        ll2.reverse()
        print(ll1, ll2)
        if len(ll1) == len(ll2):
            outl = []
            for (k ,v) in enumerate(ll1):
                outl.append(v)
                outl.append(ll2[k])
            return outl
        else:
            outl = []
            for (k, v) in enumerate(ll1):
                if k != len(ll1) -1:
                    outl.append(v)
                    outl.append(ll2[k])
                else:
                    outl.append(v)
            return outl


a = Solution()
print(a.wiggleSort([1,1,2,1,2,2]))