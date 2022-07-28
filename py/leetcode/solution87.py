from functools import   lru_cache
class Solution:
    @lru_cache(None)
    def getM(self, str1):
        m1 = {}
        for i in str1:
            if i not in m1:
                m1[i] = 1
            else:
                m1[i] += 1
        return m1

    def checkOK(self, m1, m2):
        for i in m1:
            if m1[i] != m2.get(i, 0):
                return False
        for i in m2:
            if m2[i] != m1.get(i,0):
                return False
        return True

    @lru_cache(None)
    def isScramble(self, s1: str, s2: str) -> bool:
        """

        :param s1:
        :param s2:
        :return:
        """
        if s1 == s2:
            return True
        if len(s1) == 2:
            if s1[0] == s2[1] and s1[1] == s2[0]:
                return True
            else:
                return False

        for (k,v) in enumerate(s1):
            if k == 0:
                continue
            if v == s2[k]:
                left1 = s1[:k]
                left2 = s2[:k]
                right1 = s1[k:]
                right2 = s2[k:]
                lem1 = self.getM(left1)
                lem2 = self.getM(left2)
                rim1 = self.getM(right1)
                rim2 = self.getM(right2)
                if self.checkOK(lem1, lem2) and self.checkOK(rim1, rim2):
                    if self.isScramble(left1, left2) and self.isScramble(right1, right2):
                        return True
        return False

a = Solution()
print(a.isScramble("abcd",
"bdac"))