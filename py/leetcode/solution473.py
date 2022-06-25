from  typing import List
from functools import lru_cache
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """
        matchsticks = [3,3,3,3,4]
        :param matchsticks:
        :return:
        """

        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        if total == 0:
            return False
        self.target = total//4
        pass
        if len(matchsticks) < 4:
            return False
        self.matchsticks = matchsticks
        matchsticks.sort()
        self.ll = [0,0,0,0]
        res = self.checkOK(0,  )
        return res


    def checkOK(self, idx, ):

        #print(ll)

        if idx == len(self.matchsticks):

            for i in self.ll:
                if i != self.target:
                    return False
            return True
        for i in range(4):
            if self.ll[i] + self.matchsticks[idx] <= self.target:
                #ll1 = ll
                self.ll[i] += self.matchsticks[idx]
                ok1 = self.checkOK(idx+1, )
                if ok1:
                    return True
                self.ll[i] -= self.matchsticks[idx]
        return False

a = Solution()
print(a.makesquare(matchsticks =[5,5,5,5,4,4,4,4,3,3,3,3]))
