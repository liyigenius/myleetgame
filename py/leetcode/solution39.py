from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        candidates = [2,3,6,7], target = 7
        :param candidates:
        :param target:
        :return:
        """
        pass
        self.candi = candidates
        self.t = target
        res = self.getAns(target)
        return res


    def getAns(self, target ):
        oklist = []
        if target in self.candi:
            oklist.append((target))

        for i in self.candi:
            tt1 = []
            rest = target - i
            if rest > 0:
                ok1 = self.getAns(rest)
                if ok1:
                    for a in ok1:
                        tt1.append(a)
            for j in tt1:
                t1 = j
                print(tt1)
                #t1.insert(0, i)
                print(t1)
                print('..')
                oklist.append(t1)

        return oklist

a = Solution()
print(a.combinationSum( candidates = [2,3,6,7], target = 7  ))