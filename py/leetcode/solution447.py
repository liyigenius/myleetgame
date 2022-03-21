from typing import List
from math import sqrt

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        """

        :param points:
        :return:
        """
        pass
        m1 = {}
        for (k,v) in enumerate(points):
            for i in range(k+1, len(points)):
                m1[(k,i)] = self.getDist(v, points[i])
        cnt = 0
        for i in range(len(points)):
            m2 = {}
            for j in range(len(points)):
                if i == j:
                    continue
                res = 0
                if i < j:
                    res = m1.get((i,j))
                else:
                    res = m1.get((j,i))
                if res not in m2:
                    m2[res] = 1
                else:
                    m2[res] += 1
            for i in m2:
                vv = m2[i]
                if vv > 1:
                    cnt += vv

        return cnt



    def getDist(self,a,b):
        dist = (a[0] - b[0] ) **2 + (a[1] - b[1] ) **2
        res = sqrt(dist)
        return res

a = Solution()
print(a.numberOfBoomerangs([[0,0],[1,0],[2,0]]))