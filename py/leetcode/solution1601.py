from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        """
        n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
        :param n:
        :param requests:
        :return:
        """
        pass
        ll2 = []
        ok = 0

        while len(requests) > 0:
            first = requests.pop(0)
            if [first[1], first[0]] in requests:
                ok += 2
                requests.remove([first[1], first[0]])
                continue
            else:
                ll2.append(first)
        print(ll2)


    def addM(self, map1, tt):
        if tt[0] not in map1:
            map1[tt[0]] = 1
        else:
            map1[tt[0]] += 1

        if tt[1] not in map1:
            map1[tt[1]] = 1
        else:
            map1[tt[1]] += 1

    def checkOK(self, m1):

        for i in m1:
            if m1[i] %2 != 0:
                return False
        tt1 = list(m1.values())
        tt1.sort()
        return tt1[0] == tt1[-1]


    def getAns(self, todo, prevM, last):
        if len(todo) == 0:
            return 0
        if len(todo) == 1:
            if todo[0] != last:
                return 0
            resM = self.addM(prevM, last)
            res = self.checkOK(resM)
            if res:
                return len(resM)
            return 0













a = Solution()
print(a.maximumRequests(5, [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]))

