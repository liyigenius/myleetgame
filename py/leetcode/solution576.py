from collections import deque
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """
        m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
        :param m:
        :param n:
        :param maxMove:
        :param startRow:
        :param startColumn:
        :return:
        """
        pass
        cnt = 0
        ll = deque()
        ll.append(( (startRow, startColumn), 0)  )

        while len(ll) > 0:
            first, dist = ll.popleft()
            if dist >= maxMove:
                continue
            allplist = self.yieldAll(first)
            for i in allplist:
                if i[0] < 0:
                    cnt += 1
                    continue
                if i[0] > m-1:
                    cnt += 1
                    continue
                if i[1] < 0:
                    cnt += 1
                    continue
                if i[1] > n-1:
                    cnt += 1
                    continue
                ll.append( (i, dist+1) )
        return cnt % (10**9+7)


    def yieldAll(self, st):
        ll = []
        ll.append((st[0]-1, st[1]))
        ll.append((st[0] +1, st[1]))
        ll.append((st[0] , st[1] + 1 ))
        ll.append((st[0] , st[1] - 1))

        return ll