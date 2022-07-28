import math
from functools import lru_cache
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        """

        :param s:
        :param k:
        :return:
        """
        pass
        if k == 0:
            return self.getAns(s)
        ansM = math.inf
        for (k1,v1) in enumerate(s):
            rest = s[:k1] + s[k1+1:]
            ansM = min(ansM, self.getLengthOfOptimalCompression(rest, k-1) )
        return ansM


    @lru_cache(None)
    def getAns(self, w):
        prev = ''
        cnt = 0
        outl = ''
        for (k, v) in enumerate(w):
            if prev == '':
                prev = v
                cnt = 1
                continue
            if v == prev:
                cnt += 1
                continue
            else:
                if cnt == 1:
                    outl += prev
                else:
                    outl += prev + str(cnt)

                cnt = 1
                prev = v
        if cnt == 1:
            outl += prev
        else:
            outl += prev + str(cnt)
        return len(outl)

a = Solution()
print(a.getLengthOfOptimalCompression(s = "abcdefghijklmnopqrstuvwxyz", k = 16))