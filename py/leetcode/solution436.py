from typing import List

from sortedcontainers import SortedList


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        """
        intervals = [[3,4],[2,3],[1,2]]
        :param intervals:
        :return:
        """
        sd1 = SortedList(key=lambda x: x[0])
        for (k, v) in enumerate(intervals):
            sd1.add((v[0], k))
        ll = []
        for (k,v) in enumerate(intervals):
            v1 = v[1]
            idx1 = sd1.bisect_left((v1, 0))
            if idx1 == len(sd1):
                ll.append(-1)
            else:
                vv = sd1[idx1]
                ll.append(vv[1])
        return ll