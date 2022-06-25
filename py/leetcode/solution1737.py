import math


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        """

        :param a:
        :param b:
        :return:
        """
        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        ok = math.inf
        for (k, v) in enumerate(a):
            if k > len(b) -1:
                break
            if v != b[k]:
                cnt1 += 1
        cnt2 = self.getCmp(a, b)
        cnt3 = self.getCmp(b, a)

        ok = min(cnt1, cnt2, cnt3)
        return ok


    def getCmp(self,a,b):
        """
        a = "aba", b = "caa"
        :param a:
        :param b:
        :return:
        """
        cnt1 = 0
        for (k,v) in enumerate(a):
            if k > len(b) -1:
                break
            if b[k] > v:
                continue
            if b[k] <= v:
                if b[k] == 'z':
                    return math.inf
                else:
                    cnt1 += 1
        return cnt1

a = Solution()
print(a.minCharacters(a = "dabadd", b = "cda"))





a = Solution()
print(a.minCharacters( a = "aba", b = "caa" ))
