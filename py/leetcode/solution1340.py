from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        """

        :param arr:
        :param d:
        :return:
        """
        accessSeq = []
        for (k, v) in enumerate(arr):
            accessSeq.append((v, k))
        accessSeq.sort(key=lambda x: x[0])
        dp = {}
        for (k, v) in enumerate(accessSeq):
            v1, idx = v
            if k == 0:
                dp[idx] = 1
            else:
                ok = 1
                l, r = True, True
                for j in range(1, d + 1):
                    if l is False and r is False:
                        break
                    t1 = idx + j
                    t2 = idx - j
                    if t1 > len(arr) - 1 or arr[t1] >= v1:
                        l = False
                    if t2 < 0 or arr[t2] >= v1:
                        r = False
                    if l is True:
                        ok = max(ok, 1 + dp.get(t1, 0))
                    #print(r)
                    if r is True:
                        ok = max(ok, 1 + dp.get(t2, 0))

                dp[idx] = ok
        max1 = max(dp.values())
        for i in sorted(dp.keys()):
            print(i, dp[i])
        return max1


a = Solution()
"""
[22,29,52,97,29,75,78,2,92,70,90,12,43,17,97,18,58,100,41,32]
17
"""
print(a.maxJumps(arr=[22,29,52,97,29,75,78,2,92,70,90,12,43,17,97,18,58,100,41,32], d=17))
