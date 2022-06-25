class Solution:
    def totalNQueens(self, n: int) -> int:
        """

        :param n:
        :return:
        """
        if n == 1:
            return 0
        if n == 2:
            return 0
        self.n = n
        res = self.getAns(1, [])
        return res

    def checkOK1(self, cur, prevlist):
        #print(cur, prevlist)
        if abs(cur - prevlist[-1]) <= 1:
            return False
        if cur in prevlist:
            return False

        for i in range(len(prevlist)):
            step = i + 1
            tag1 = cur - step
            tag2 = cur + step
            tocheckV = prevlist[len(prevlist)- i - 1]
            if tocheckV == tag2 or tocheckV == tag1:
                return False

        return True

    def getAns(self, cur, reslist):
        cnt = 0
        # if cur == self.n:
        #     #check ..
        #     if self.checkOK1(cur, reslist):
        #         return 1
        #     return 0
        if cur > self.n:
            return 1

        for i in range(self.n):
            # pre-check
            if len(reslist) == 0:

                p1 = reslist.copy()
                p1.append(i+1)
                cnt += self.getAns(cur + 1, p1)
            else:

                if self.checkOK1(i+1, reslist) is False:
                    continue

                p1 = reslist.copy()
                p1.append(i+1)
                cnt += self.getAns(cur + 1, p1)

        return cnt


a = Solution()
print(a.totalNQueens(5))

#print(a.checkOK1(1,[2,4]))
