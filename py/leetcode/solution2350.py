from typing import List


class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        """

        :param rolls:
        :param k:
        :return:
        """
        s1 = set()
        ans = 0
        for i in rolls:
            s1.add(i)
            if len(s1) == k:
                s1.clear()
                ans += 1

        return ans + 1
