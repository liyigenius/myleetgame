from typing import List
from copy import deepcopy

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        """

        :param mat:
        :return:
        """
        pass
        start1 = self.getStr1(mat)
        ll = []
        ll.append((start1, 0))
        used = {}
        self.h = len(mat)
        self.w = len(mat[0])
        while len(ll) > 0:
            first, step = ll.pop(0)
            if self.checkZero(first):
                return step
            if first not in used:
                used[first] = step
            else:
                if step >= used[first]:
                    continue
                else:
                    used[first] = step
            oriMat = self.conver2Mat(first)
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    val1 = (i, j)
                    #converting..
                    t1 = deepcopy(oriMat)
                    if t1[i][j] == '1':
                        t1[i][j] = '0'
                    else:
                        t1[i][j] = '1'
                    if i - 1 >= 0:
                        if t1[i-1][j] == '1':
                            t1[i-1][j] = '0'
                        else:
                            t1[i-1][j] = '1'

                    if j-1 >= 0:
                        if t1[i][j-1] == '1':
                            t1[i][j-1]  = '0'
                        else:
                            t1[i][j-1]  = '1'

                    if i + 1 <= self.h -1:
                        if t1[i+1][j] == '1':
                            t1[i+1][j] = '0'
                        else:
                            t1[i+1][j] = '1'

                    if j+1 <= self.w - 1:
                        if t1[i][j+1] == '1':
                            t1[i][j+1] = '0'
                        else:
                            t1[i][j+1] = '1'
                    str2 = self.getStr1(t1)
                    ll.append((str2, step+1))

        return -1



    def conver2Mat(self, str1):
        outl = []
        cnt = 0
        tmpl = []
        for i in str1:
            tmpl.append(i)
            if (cnt+1) % self.w == 0:
                outl.append(tmpl)
                tmpl = []
            cnt += 1
        return outl



    def checkZero(self,ll):
        for i in ll:
            if i == '1':
                return False
        return True

    def getStr1(self, ll):
        outl = ''
        for i in ll:
            for j in i:
                if str(j) == '1':
                    outl += '1'
                else:
                    outl += '0'
        return outl

a = Solution()
print(a.minFlips(mat = [[0,0],[0,1]]))