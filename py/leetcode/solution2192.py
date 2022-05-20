class Solution:
    def sumScores(self, s: str) -> int:
        """

        :param s:
        :return:
        """
        # m1 = set()
        # for (k,v) in enumerate(s):
        #     subs = s[:k+1]
        #     m1.add(subs)

        cnt = 0
        for i in range(len(s)):
            newVal = len(s)  - 1- i
            subll = s[newVal:]
            for j in range(len(subll)):
                newVal2 = len(subll) - 1 - j
                ss = subll[newVal2:]
                if s.startswith(ss):
                    cnt += len(ss)
                    break
        return cnt


a = Solution()
print(a.sumScores('babab'))