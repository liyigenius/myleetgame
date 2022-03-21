from typing import List


class Solution:
    def __init__(self):
        self.m1 = {}

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """

        :param nums:
        :param k:
        :return:
        """
        sum1 = sum(nums)
        if sum1 % k != 0:
            return False
        tar = sum1 // k
        todec = 0
        n2 = []
        for i in nums:
            if i == tar:
                todec +=  1
                continue
            if i > tar:
                return False
            n2.append(i)
        k -= todec
        ll = k * [tar]
        n2.sort()
        res = self.checkOK(n2, ll)
        return res

    def checkOK(self, numlist, klist):
        t1,t2 = tuple(numlist), tuple(klist)
        if (t1,t2) in self.m1:
            return self.m1[(t1,t2)]

        if len(numlist) == 1:
            if len(klist) != 1:
                self.m1[(t1, t2)] = False
                return False
            if klist[0] == numlist[0]:
                self.m1[(t1, t2)] = True
                return True
            else:
                self.m1[(t1, t2)] = False
                return False
        ok = False
        for i in numlist:
            for (k,v) in enumerate(klist):
                if v >= i:
                    restV = v -i
                    if restV == 0:
                        res1 = self.checkOK(numlist[1:],  klist[:k]+klist[k+1:] )
                        if res1:
                            self.m1[(t1, t2)] = True
                            return True
                    else:
                        res1 = self.checkOK(numlist[1:],  klist[:k]+ [restV]+ klist[k+1:] )
                        if res1:
                            self.m1[(t1, t2)] = True

                            return True
        self.m1[(t1, t2)] = False
        return False



a = Solution()
print(a.canPartitionKSubsets([3522,181,521,515,304,123,2512,312,922,407,146,1932,4037,2646,3871,269] ,  5 ))


