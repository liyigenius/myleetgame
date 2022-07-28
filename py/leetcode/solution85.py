from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """

        :param matrix:
        :return:
        """
        cnt1 = 0
        dp = {}
        for (k, v) in enumerate(matrix):
            for (k2, v2) in enumerate(v):
                if v2 == '0':
                    dp[k, k2, k, k2] = False
                    continue
                if v2 == '1':
                    cnt1 = max(cnt1, 1)
                    dp[k, k2, k, k2] = True
                    for j in range(k + 1):
                        for j2 in range(k2 + 1):
                            if j == k and j2 == k2:
                                continue
                            flag = matrix[j][j2]
                            if flag == '0':
                                continue
                            else:
                                if k2 == 0:
                                    ans1 = True
                                else:
                                    ans1 = dp.get((j, j2, k, k2 - 1), False)
                                if k == 0:
                                    ans2 = True
                                else:
                                    ans2 = dp.get((j, j2, k - 1, k2), False)
                                if ans1 is False or ans2 is False:
                                    dp[j, j2, k, k2] = False
                                else:
                                    dp[j, j2, k, k2] = True
                                    cnt1 = max(cnt1, (k2-j2+1) * (k-j+1) )
        print(dp)
        return cnt1

a = Solution()
print(a.maximalRectangle( [["1","0","1","0","0"],["1","0","1","1","1"]  ]



))

