import math
from functools import lru_cache


class Solution:
    def strangePrinter(self, s: str) -> int:
        """

        :param s:
        :return:
        """
        pass
        res = self.getAns(s)
        return res

    @lru_cache(None)
    def getAns(self, ss):
        if len(ss) == 0:
            return 0
        if len(ss) == 1:
            return 1
        t1, ok = self.getOverDub(ss)
        ans = math.inf
        if ok:

                v1 = 1 + self.getAns(t1)
                ans = min(ans, v1)
        else:
            for i in range(1, len(ss)):
                l,r = ss[:i], ss[i:]
                cnt = self.getAns(l) + self.getAns(r)
                ans = min(ans, cnt)
        return ans


    @lru_cache(None)
    def getLmin(self, s):
        tag = s[0]
        l = -1
        for (k,v) in enumerate(s):
            if v != tag:
                l = k-1
                break
        return s[l+1:]

    @lru_cache(None)
    def getRmin(self, s):
        tag = s[-1]
        r = -1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == tag:
                continue
            else:
                r = i + 1
                break
        return s[:r]

    @lru_cache(None)
    def getOverDub(self, s):
        if s[0] == s[-1]:
            tag = s[0]
            l,r = -1 ,-1
            for (k,v) in enumerate(s):
                if v == tag:

                    continue
                else:
                    l = k-1
                    break
            for i in range(len(s)-1, -1,-1):
                if s[i] == tag:
                    continue
                else:
                    r = i + 1
                    break
            if l == -1 or r == -1:
                return '', True
            return s[l+1:r], True
        return '', False

a = Solution()
print(a.strangePrinter("baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa"))

