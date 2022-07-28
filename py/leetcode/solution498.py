from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """

        :param mat:
        :return:
        """
        cnt = 0
        total = len(mat) * len(mat[0])
        ll = []
        st = (0,0)
        dirt = 1
        while True:
            if cnt == total:
                break
            if dirt == 1:
                nextX = st[0] -1
                nextY = st[1] + 1
                if nextX < 0 or nextY > len(mat[0]) - 1:
                    dirt = 0



        return ll