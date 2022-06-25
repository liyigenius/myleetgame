import math
from functools import lru_cache
class Solution:

    def minMovesToMakePalindrome(self, s: str) -> int:
        """
        leteltx
        :param s:
        :return:
        """
        pass
        len1 = len(s)
        if len1 %2 == 0:
            pass
            res = self.getAns(s)
            return res
        else:
            pass
            m1 = {}
            for i in s:
                if i not in m1:
                    m1[i] =1
                else:
                    m1[i] += 1
            idxA = ''
            for i in m1:
                if m1[i] %2  == 1:
                    idxA = i
                    break
            idxll = []
            for (k,v) in enumerate(s):
                if v == idxA:
                    idxll.append(k)

            cnt1 = (len(s) -1) //2
            # cnt3 = -1
            # for i in idxll:
            #     if abs(i - cnt1) < cnt2:
            #         cnt2 = abs(i - cnt1)
            #         cnt3 = i
            last1 = idxll[-2]
            cnt2 = abs(last1 - cnt1)

            news = s[:last1] + s[last1+1:]
            return cnt2 + self.getAns(news)



    def getAns(self,s1):
        if len(s1) == 0:
            return 0
        if s1[0] == s1[-1]:
            return self.getAns(s1[1:-1])
        xx = s1.rfind(s1[0])
        newword = s1[1:xx]+s1[xx+1:]
        cnt = len(s1)- 1- xx
        return cnt + self.getAns(newword)


a = Solution()
print(a.minMovesToMakePalindrome("scpcyxprxxsjyjrww"))
