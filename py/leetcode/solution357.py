class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        """

        :param n:
        :return:
        """
        pass
        if n == 0:
            return 1
        if n == 1:
            return 9
        res = 0
        for i in range(n+1):
            if n == 0:
                res += 1
                continue
            if n == 1:
                res += 10
                continue
            s1 = set()
            q1 = self.getAns(i, s1)
            print(q1)
            res += q1
        return res


    def getAns(self, n, used):
        if n == 0:
            return 1
        if n == 1:
            cnt = 0
            for i in range(0,10):
                if i not in used:
                    cnt += 1
            return cnt
        res = 0
        if len(used) == 0:
            for i in range(1, 10):
                if i in used:
                    continue
                newC = used.copy()
                newC.add(i)
                res += self.getAns(n - 1, newC)
        else:
            for i in range(0, 10):
                if i in used:
                    continue
                newC = used.copy()
                newC.add(i)
                res += self.getAns(n - 1, newC)

        return res

a = Solution()
print(a.countNumbersWithUniqueDigits(2))