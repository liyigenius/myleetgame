from typing import List
from sortedcontainers import SortedList


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        nums1 = [1,7,11], nums2 = [2,4,6], k = 3
        :param nums1:
        :param nums2:
        :param k:
        :return:
        """
        sd1 = SortedList(key=lambda x: x[0])
        for i in range(min(k, nums1)):
            for j in range(min(k, nums2)):
                res = nums1[i] + nums2[j]
                sd1.append((res, i, j))

        res2 = []
        for i in range(min(k, len(sd1))):
            res2.append((i[1], i[2]))
        return res2
