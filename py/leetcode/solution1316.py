from functools import lru_cache


class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        """

        :param text:
        :return:
        """
        cnt = 0
        set1 = set()
        self.ss = text
        for (k, v) in enumerate(text):
            for j in range(k + 1, len(text) + 1):
                #substr = text[k:j]
                if self.getOK(k, j):
                    set1.add(text[k:j])

        return len(set1)

    #@lru_cache(None)
    def getOK(self, k ,j):
        if j-k <2:
            return False
        if (j-k) %2 != 0:
            return False
        #tag = len(str1)//2
        mid = (j-k) //2 + k
        if self.ss[k:mid] != self.ss[mid:j]:
            return False
        return True

a = Solution()
print(a.distinctEchoSubstrings("abcabcabc"))