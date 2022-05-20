import math
from typing import List
from functools import lru_cache

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        """

        :param jobs:
        :param k:
        :return:
        """
        if k == 1:
            return sum(jobs)
        if k >= len(jobs):
            return max(jobs)

        st_list = '0' * len(jobs)
        self.nn = jobs
        ll = []
        for i in range(k):
            ll.append(0)
        res = self.iter(st_list, tuple(ll))
        return res

    @lru_cache(None)
    def checkALL(self, ll):
        for i in ll:
            if i == '0':
                return False
        return True


    @lru_cache(None)
    def iter(self, st, ll):
        if self.checkALL(st):
            return max(ll)
        res = math.inf

        for (k,v) in enumerate(st):
            if v == '0':

                for (k2,v2) in enumerate(ll):
                    newStr = st[:k]+'1'+st[k+1:]
                    nn = list(ll).copy()
                    nn[k2]+=self.nn[k]
                    res1 = self.iter(newStr, tuple(nn))
                    res = min(res, res1)
        return res

a = Solution()
print(a.minimumTimeRequired(jobs = [9899456,8291115,9477657,9288480,5146275,7697968,8573153,3582365,3758448,9881935 ,]
, k = 9))