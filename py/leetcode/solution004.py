from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ll = []
        for i in nums1:
            ll.append(i)
        for i in nums2:
            ll.append(i)
        ll.sort()
        if len(ll) %2 == 0:
            l = len(ll) // 2
            r = l-1
            return (ll[l] +ll[r]) / 2
        else:
            l = len(ll) //2
            return ll[l]