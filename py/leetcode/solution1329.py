from typing import List
from copy import deepcopy

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """

        :param mat:
        :return:
        """
        pass
        ret = deepcopy(mat)
        todo = []
        for i in range(len(mat[0])):
            todo.append((0, i))
        for i in range(len(mat)):
            if i != 0:
                todo.append((i,0))
        #print(todo)
        for i in todo:
            res1 = self.getLL(i[0], i[1], len(mat), len(mat[0]))
            #print(res1)
            v1 = [ mat[i[0]][i[1]] for i in res1]
            v1.sort()
            for (k,v) in enumerate(res1):
                ret[v[0]][v[1]]  = v1[k]


        return ret

    def getLL(self,h,w,maxH, maxW):
        ll = []
        ll.append((h,w))
        while True:
            t1 = ll[-1]
            new1 = t1[0]+1, t1[1]+1
            if new1[0] > maxH - 1 or new1[1] > maxW -1:
                break
            ll.append(new1)
        return ll

a = Solution()
print(a.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))