from functools import lru_cache
class Solution:
    @lru_cache(None)
    def numDistinct(self, s: str, t: str) -> int:
        """
        s = "babgbag", t = "bag"
        s = "rabbbit", t = "rabbit"
        :param s:
        :param t:
        :return:
        """
        if len(s) == 0 and len(t) == 0:
            return 1
        if len(t) == 0 and len(s) > 0:
            return 1
        if len(s) < len(t):
            return 0
        if len(s) == len(t):
            if s == t:
                return 1
            return 0
        if s[0] != t[0]:
            return self.numDistinct(s[1:], t)
        v1 = self.numDistinct(s[1:], t[1:])
        v2 = self.numDistinct(s[1:], t)
        return v1 + v2


