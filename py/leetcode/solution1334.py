from typing import List
from collections import deque

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        """

        :param n:
        :param edges:
        :param distanceThreshold:
        :return:
        """
        self.d = distanceThreshold
        self.m1 = {}
        for i in edges:
            if i[0] not in self.m1:
                self.m1[i[0]] = [(i[1], i[2])]
            else:
                self.m1[i[0]].append((i[1], i[2]))

            if i[1] not in self.m1:
                self.m1[i[1]] = [(i[0], i[2])]
            else:
                self.m1[i[1]].append((i[0], i[2]))

        m1 = {}
        for i in range(n):
            res = self.findOK(i)
            m1[i] = res
        print(m1)
        ll2 = [(i, m1[i]) for i in m1]
        ll2.sort(key=lambda x:(x[1], -x[0]))
        first = ll2[0]
        return first[0]



    def findOK(self, n, ):
        ll = deque()
        ll.append((n,self.d))
        cnt = 0
        used = {}
        while len(ll) > 0:
            first, rank = ll.popleft()
            if first not in used:
                used[first] = rank
            else:
                if rank > used[first]:
                    used[first] = rank
                else:
                    continue

            ll2 = self.m1.get(first, [])
            for i in ll2:
                rest = rank - i[1]
                if rest >= 0:
                    ll.append((i[0], rest))
        return len(used) - 1


a = Solution()
print(a.findTheCity( n = 6, edges = [[0,1,10],[0,2,1],[2,3,1],[1,3,1],[1,4,1],[4,5,10]], distanceThreshold = 20 ))