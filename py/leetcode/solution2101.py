from typing import List
from math import sqrt
from functools import lru_cache
from collections import deque

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        """

        :param bombs:
        :return:
        """
        pass
        self.ll = bombs
        ok = 0
        mm1 = {}
        for i in self.ll:
            if tuple(i) not in mm1:
                mm1[tuple(i)] = 1
            else:
                mm1[tuple(i)] += 1

        for i in mm1.keys():
            res1 = self.getAns(tuple(i))
            cnt2 = mm1.get(tuple(i))
            res1 = res1 + cnt2 - 1
            ok = max(ok, res1)


        return ok

    @lru_cache(None)
    def getAns(self, cur):
        used = set()
        ll = deque()
        ll.append((cur))
        while len(ll ) > 0:
            x,y, range1 = ll.popleft()
            if (x,y) in used:
                continue
            used.add((x,y))
            for i in self.ll:
                res1 = self.getDis((i[0],i[1]), (x,y) )
                if res1 <= range1:
                    ll.append(i)
        return len(used)


    @lru_cache(None)
    def getDis(self,a,b):
        v1 = a[0] - b[0]
        v2 = a[1] - b[1]
        res= v1 ** 2+ v2**2
        return sqrt(res)

a = Solution()
print(a.maximumDetonation([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))