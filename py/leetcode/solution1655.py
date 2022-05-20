from typing import List


class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        """
        nums = [1,2,3,3], quantity = [2]
        :param nums:
        :param quantity:
        :return:
        """
        m1 = {}
        for i in nums:
            if i not in m1:
                m1[i] = 1
            else:
                m1[i] += 1
        ll = list(m1.values())
        self.ll = ll
        res = self.iter(ll, quantity)
        return res

    def iter(self, m1, idx):
        if idx == len(self.ll):
            return True
        for i in m1:
            if i

