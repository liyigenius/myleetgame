from typing import List
from functools import lru_cache


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        """

        :param bombs:
        :return:
        """
        pass
        self.bombs = bombs
        cnt = 0
        for (k,v) in enumerate(bombs):
            cnt = max(cnt, self.iter(k, set() ) )
        return cnt

    #@lru_cache(None)
    def iter(self, idx , used):
        val = self.bombs[idx]
        cnt = 1
        used.add(tuple(val))
        for (k,v) in enumerate(self.bombs):
            if tuple(v) in used:
                continue
            delta = self.getDist(v, val)
            if delta <= val[2]**2:
                if delta == 0:
                    cnt += 1
                else:
                    newV = used.copy()
                    #newV.add(tuple(val))
                    cnt += self.iter(k, newV)
        return cnt

    def getDist(self,a,b):
        rest = (a[0]-b[0])**2 + (a[1]-b[1])**2
        return rest

a = Solution()
print(a.maximumDetonation(bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]] ))