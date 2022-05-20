from typing import List


class Solution:
    def __init__(self):
        self.n = 0

    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        """
        batchSize = 3, groups = [1,2,3,4,5,6]
        :param batchSize:
        :param groups:
        :return:
        """
        self.n = batchSize
        if len(groups) == 0:
            return 0
        res = self.getAns(0 , groups)
        return res


    def getAns(self, rest: int, groups: List[int]) -> int:
        """
        batchSize = 3, groups = [1,2,3,4,5,6]
        :param rest:
        :param groups:
        :return:
        """
        if len(groups) == 0:
            return 0
        toadd = 0
        if rest == 0:
            toadd += 1
        max1 = 0
        for (k, v) in enumerate(groups):
            # cp1 = groups.copy()
            if rest == 0:
                if v < self.n + rest:  #
                    rest1 = self.n + rest - v
                    max1 = max(max1, self.getAns(rest1, groups[:k] + groups[k + 1:]))

                if v == self.n + rest:
                    max1 = max(max1, self.getAns(0, groups[:k] + groups[k + 1:]))

                if v > self.n + rest:
                    rr = v - (self.n + rest)
                    max1 = max(max1, self.getAns(0, groups[:k] + [rr] + groups[k + 1:]))
            else:
                if rest > v:
                    rest2 = rest  - v
                    max1 = max(max1, self.getAns(rest2, groups[:k] + groups[k + 1:]))
                if rest == v:
                    max1 = max(max1, self.getAns(0, groups[:k] + groups[k + 1:]))

                if rest < v:
                    newV = v - rest
                    max1 = max(max1, self.getAns(0, groups[:k] + [newV] + groups[k + 1:]))


        if len(groups) == 1:
            return 0
        #if  max1 > 0:
        return max1 + 1
        #return max1

a = Solution()
print(a.maxHappyGroups(batchSize = 3, groups = [1,2,3,4,5,6]))