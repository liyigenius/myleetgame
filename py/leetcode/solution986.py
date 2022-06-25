from typing import List
from sortedcontainers import SortedList

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
        输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

        :param firstList:
        :param secondList:
        :return:
        """
        firstList.sort(key=lambda x:x[0])
        sd1 = SortedList(key=lambda x:x[0])
        for i in secondList:
            sd1.add((i))

        ll = []
        for i in firstList:
            for j in secondList:
                if j[0] > i[1]:
                    break
                if i[0] > j[1]:
                    continue
                if j[1] >= i[1] and i[1] >= j[0]:
                    ll.append((max(j[0],i[0]), i[1]))
                elif j[1] < i[1]:
                    ll.append((max(i[0],j[0]), j[1]))
        return ll


a = Solution()
print(a.intervalIntersection( [[5,10]],
[[3,10]] ))
