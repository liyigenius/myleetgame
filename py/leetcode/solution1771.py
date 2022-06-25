from functools import lru_cache


class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        pass
        totalL, l, r= self.getLongest(0, len(word1+word2)-1, word1 + word2, )
        print(totalL, l,r)


    @lru_cache(None)
    def getLongest(self, l, r, w):  # return l,r...

        if len(w) == 0:
            return 0, l, r
        if len(w) == 1:
            return 0, l, r
        if w[0] == w[-1]:
            return 2 + self.getLongest(l+1, r-1, w[1:-1] )[0], l ,r
        v1, l1, r1 = self.getLongest(l+1, r, w[1:])
        v2, l2, lr2 = self.getLongest(l, r-1, w[:-1])
        if v1 >v2:
            return v1, l, r-1
        return v2, l+1, r


"""
"ceebeddc"
"d"
"""
a = Solution()
print(a.longestPalindrome( word1 = "abc", word2 = "ba" ))
