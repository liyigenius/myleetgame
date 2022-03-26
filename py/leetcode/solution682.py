from sortedcontainers import SortedList
from functools import lru_cache
m = dict()
class Solution:
    def __init__(self):
        pass

    def monotoneIncreasingDigits(self, n: int) -> int:
        """

        :param n:
        :return:
        """
        pass
        oklist = SortedList()
        stop = False
        for i in range(1, 11):
            if stop is True:
                break
            res = self.yieldPost(i)

            for j in res:
                if j > n:
                    stop = True
                    break
                oklist.add(j)

        resIdx = oklist.bisect_left(n)
        resIdx = min(len(oklist) - 1, resIdx)
        res1 = oklist[resIdx]
        return res1

    @lru_cache(None)
    def yieldPost(self, n,prev = 0):
        global m
        if (n,prev) in m:
            return m[(n,prev)]

        if n == 1:
            outl = []
            for i in range(prev,10):
                outl.append(i)
            return outl
        outl = []
        for i in range(prev,10):
            first = str(i)
            rest = self.yieldPost(n-1, i)
            for j in rest:
                outl.append( first+ str(j) )
        res = [int(i) for i in outl]
        m[(n,prev)] = res
        return res

a = Solution()
print(a.monotoneIncreasingDigits(677339157))
