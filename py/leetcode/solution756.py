from typing import List
from functools import lru_cache
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        """

        :param bottom:
        :param allowed:
        :return:
        """
        pass
        self.allowed = allowed
        res = self.getAns(bottom)
        return res

    @lru_cache(None)
    def getAns(self, words):
        if len(words) == 1:
            return False
        if len(words) == 2:
            for i in self.allowed:
                if i[:2] == words:
                    return True
            return False

        plist = []
        for i in range(len((words))-1):
            ww1 = words[i:i+2]
            found = False
            tl = []
            for j in self.allowed:
                if j[:2] == ww1:
                    found = True
                    tl.append(j[2])
            if len(plist) == 0:
                plist = tl
            else:
                tt = []
                for k1 in plist:
                    for k2 in tl:
                        tt.append(k1+k2)
                plist = tt
            if found is False:
                return False

        for i in plist:
            if self.getAns(i) is True:
                return True
        return False

a  = Solution()
print(a.pyramidTransition( bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"] ))



