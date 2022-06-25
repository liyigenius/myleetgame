from typing import List
from functools import lru_cache

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """

        :param words:
        :return:
        """
        s1 = set()

        for i in words:
            s1.add(i)
        self.s1 = s1
        ll = []
        for i in words:
            if self.checkMade(i):
                ll.append(i)
        return ll


    @lru_cache(None)
    def checkMade(self, w):
        for j in range(1, len(w)):
            l, r = w[:j], w[j:]
            if (self.checkMade(l) or l in self.s1) and (self.checkMade(r)  or r in self.s1 ):
                return True
        return False

a = Solution()
print(a.findAllConcatenatedWordsInADict(words = ["cat","dog","catdog"]))