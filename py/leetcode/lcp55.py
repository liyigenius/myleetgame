from typing import List


class Solution:
    def getMinimumTime(self, time: List[int], fruits: List[List[int]], limit: int) -> int:
        """

        :param time:
        :param fruits:
        :param limit:
        :return:
        """
        m1 = {}
        for i in fruits:
            if i[0] not in m1:
                m1[i[0]] = [i[1]]
            else:
                m1[i[0]].append(i[1])
        ans = 0
        for i in range(len(time)):
            t1 = m1[i]
            for j in t1:
                if j % limit == 0:
                    ans += j //limit * time[i]
                else:
                    ans += (j // limit + 1) * time[i]
        return ans
