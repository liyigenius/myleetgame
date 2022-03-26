import math
from typing import List


class Solution:
    def __init__(self):
        self.m1 = {}
        self.cnt = {}

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        """
        7
        [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
        :param n:
        :param roads:
        :return:
        """
        pass
        for i in range(n):
            self.m1[i] = []
        for i in roads:
            a, b, c = i[0], i[1], i[2]
            self.m1[a].append((b, c))
            self.m1[b].append((a, c))
        self.getRes(n - 1, set())
        ok1 = self.cnt[n-1]
        print(self.cnt)
        return ok1[1]

    def getRes(self, n, used):
        if n == 0:
            return 0
        ans = math.inf

        for i in self.m1[n]:
            if i[0] in used:
                continue
            new1 = used.copy()
            new1.add(n)
            res = i[1] + self.getRes(i[0], new1)
            if n not in self.cnt:
                self.cnt[n] = (res, 1)
            else:
                tar = self.cnt[n][0]
                if res > tar:
                    pass
                if res == tar:
                    self.cnt[n] = (tar, self.cnt[n][1] + 1)
                else:
                    self.cnt[n] = (res, 1)
            ans = min(ans, res)


        return ans


a = Solution()
print(a.countPaths(n=7, roads=[[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5],
                      [4, 6, 2]]
               ))
