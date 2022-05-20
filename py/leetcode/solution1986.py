import math
from typing import List
from functools import lru_cache

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        """

        :param tasks:
        :param sessionTime:
        :return:
        """
        pass

        self.tt = tasks
        self.origin = [str(sessionTime)] * len(tasks)
        ll2 = ','.join(self.origin)
        self.str1 = sessionTime
        bm = '0' * len(tasks)
        res = self.getCnt(bm, ll2)
        return res

    @lru_cache(None)
    def checkOK(self, bm):
        for i in bm:
            if i == '0':
                return False
        return True
    #
    @lru_cache(None)
    def checkCnt(self, ll):
        ll = ll.split(',')
        cnt = 0
        for i in ll:
            if int(i) != self.str1:
                cnt += 1
        return cnt

    @lru_cache(None)
    def getCnt(self, bm, stlist):
        pass

        if self.checkOK(bm):
            cnt =  self.checkCnt(stlist)
            return cnt
        stlist = stlist.split(',')
        res1 = math.inf
        for (k,v) in enumerate(bm):
            if v == '1':
                continue
            newbm = bm[:k] + '1' + bm[k+1:]
            for (k2, v2) in enumerate(stlist):
                if int(v2) - self.tt[k] >= 0:
                    newll = str(int(v2) - self.tt[k])
                    newst = stlist[:k2] + [str(newll)] + stlist[k2+1:]
                    newst = ','.join(newst)
                    res2 = self.getCnt(newbm,  newst)
            res1 = min(res1, res2)


        return res1


a = Solution()
print(a.minSessions( [5,9,7,4,4,7,7,9],
9 ))
