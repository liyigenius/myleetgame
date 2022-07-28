from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        """

        :param mat:
        :return:
        """
        dp = {}
        cnt = 0
        for (k,v) in enumerate(mat):
            for (k2, v2) in enumerate(v):
                if v2 == 0:
                    continue
                else:
                    print(k,k2,'!')
                    for a in range(k+1):
                        for b in range(k2+1):
                            if mat[a][b] == 1:
                                print((a,b))

a = Solution()
print(a.numSubmat(mat = [[1,0,1],[1,1,0],[1,1,0]]))