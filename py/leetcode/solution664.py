import math
from functools import lru_cache


class Solution:
    def strangePrinter(self, s: str) -> int:
        """

        :param s:
        :return:
        """
        pass
        cnt = self.getcnt(s, '')
        return cnt

    @lru_cache(None)
    def getcnt(self, s, p):
        if len(s) == 0:
            return 1
        if len(s) == 1:
            return 1
        if s[0] == s[-1]:
            if s[0] != 0:
                return self.getcnt(s[1:-1], s[0]) + 1
            return self.getcnt(s[1:-1], s[0])
        else:
            cnt = math.inf
            for i in range(1, len(s)):
                left = s[:i]
                right = s[i:]
                v1 = self.getcnt(left, )
                v2 = self.getcnt(right, '')
                ans = v1+v2
                cnt = min(cnt, ans)
            return cnt


a = Solution()
print(a.strangePrinter('aaaaaabbbb'))