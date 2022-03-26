from typing import List
from functools import lru_cache

class Solution:
    def __init__(self):
        self.m1 = {}
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """

        :param n:
        :param edges:
        :return:
        """
        m1 = {}
        for i in range(n):
            m1[i] = []
        for i in edges:
            a,b = i[0],i[1]
            m1[a].append(b)
            m1[b].append(a)
        ll2 = []
        self.m1 = m1
        for i in m1:
            ll2.append((i, len(m1[i])))
        ll2.sort(key=lambda x:x[1], reverse=True)
        ll3 = []
        cnt = 0
        vv1 = []
        for i in ll2:
            if i[1] not in vv1:
                vv1.append(i[1])
            if len(ll2) < 1000:
                pass
            else:
                if len(vv1) == 2:
                    break
        for i in ll2:
            if i[1] < min(vv1):
                break
            cnt += 1
            ll3.append((i[0], self.getHeight(i[0])))
        ll3.sort(key=lambda x:x[1])
        min1 = ll3[0][1]
        outl = []
        for i in ll3:
            if i[1] == min1:
                outl.append(i[0])
            else:
                break
        return outl

    @lru_cache(None)
    def getHeight(self, curN, prev=None):
        restlist = self.m1[curN]
        if len(restlist) == 1 and restlist[0] == prev:
            return 1
        ok1 = 0
        for i in self.m1[curN]:
            if i == prev:
                continue
            res1 = self.getHeight(i, curN )
            ok1  = max(ok1, 1 + res1)
        return ok1


a=  Solution()
print(a.findMinHeightTrees( n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]] ))