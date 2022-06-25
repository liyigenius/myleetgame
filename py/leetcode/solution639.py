from functools import  lru_cache

class Solution:
    @lru_cache(None)
    def numDecodings(self, s: str) -> int:
        """

        :param s:
        :return:
        """

        if len(s) == 0:
            return 1
        if len(s) == 1:
            if s == '0':
                return 0
            if s == '*':
                return 9
            return 1

        if s[0] == '*':
            v1 = self.numDecodings(s[2:])
            v2 = 9*self.numDecodings(s[1:])
            return v1 + v2
        intV = int(s[0])
        if intV == 0:
            return 0
        if intV > 2:
            return self.numDecodings(s[1:])
        if intV ==  1:
            v1 = self.numDecodings(s[2:])
            v2 = self.numDecodings(s[1:])
            return v1 + v2
        if intV == 2:
            intV2 = int(s[1])
            if intV2 <= 6:
                v1 = self.numDecodings(s[2:])
                v2 = self.numDecodings(s[1:])
                return v1 + v2
            return self.numDecodings(s[1:])


a = Solution()
print(a.numDecodings('99999'))