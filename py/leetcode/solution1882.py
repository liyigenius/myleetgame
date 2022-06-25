from typing import List
from sortedcontainers import SortedList
from collections import deque


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        """
        servers = [3,3,2], tasks = [1,2,3,2,1,2]
        :param servers:
        :param tasks:
        :return:
        """
        qq1 = deque()
        for i in tasks:
            qq1.append(i)
        tasks = qq1
        m1 = {}
        for (k, v) in enumerate(servers):
            m1[k] = v
        q1 = SortedList(key=lambda x: (x[0], x[1]))  # duetime, idx
        q2 = SortedList(key=lambda x: (x[0], x[1]))  # weight, idx
        outl = []
        used = 0
        timecnt = 0
        for (k, v) in enumerate(servers):
            q2.add((v, k))
        while True:
            if len(tasks) == 0:
                break
            timecnt += 1
            
            while q1 and q1[0][0] <= timecnt:
                #res = q1.pop(0)
                res = q1[0]
                del q1[0]
                q2.add((m1[res[1]], res[1]))
            while len(q2) > 0 and len(tasks) > 0:
                if used >= timecnt:
                    break
                #mid = q2.pop(0)
                mid = q2[0]
                del q2[0]
                outl.append(mid[1])

                first = tasks.popleft()
                used += 1

                tt1 = timecnt + first
                q1.add((tt1, mid[1]))

        return outl


a = Solution()
print(a.assignTasks(servers=[3, 3, 2], tasks=[1, 2, 3, 2, 1, 2]))
