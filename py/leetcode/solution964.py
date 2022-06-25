class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        """
        x = 3, target = 19
        :param x:
        :param target:
        :return:
        """
        if target == x:
            return 1
        v1 = target + x
        v2 = target - x
        v3 = target // x
        v4 = target * x
        ans = min(self.leastOpsExpressTarget(x, v1), self.leastOpsExpressTarget(x, v2),
                  self.leastOpsExpressTarget(x, v3),self.leastOpsExpressTarget(x, v4) )
        return ans

a = Solution()
print(a.leastOpsExpressTarget(3, 19))