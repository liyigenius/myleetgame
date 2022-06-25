import math
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """

        :param points:
        :return:
        """
        m1 = {}
        for (k,v) in enumerate(points):
            for (k2,v2) in enumerate(v):
                if k == 0:
                    m1[(k,k2)] = v2
                else:
                    curVal = v2
                    curM = -math.inf
                    for j in range(len(points[0])):
                        curM = max(curM, curVal+ m1.get((k-1,j)) - abs(j-k2) )

                    for j in range(-curVal, curVal+1):



                    m1[(k,k2)] = curM
        lastone = ( len(points)-1, len(points[0])-1)
        res = m1.get(lastone)
        maxV = max(m1.values())
        return maxV