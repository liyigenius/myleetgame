from functools import lru_cache
class Solution:
    @lru_cache(None)
    def longestDecomposition(self, text: str) -> int:
        """

        :param text:
        :return:
        """
        if len(text) == 0:
            return 0
        if len(text) == 1:
            return 1

        v1 = 1
        for i in range(1, len(text)//2 + 1):
            left = text[:i]
            tag = len(text)-i
            right = text[tag:]
            if left == right:
                v2 = self.longestDecomposition(text[i:tag])
                v1 = max(v1, v2 + 2)
        return v1

a = Solution()
print(a.longestDecomposition('ghiabcdefhelloadamhelloabcdefghi'))