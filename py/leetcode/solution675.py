import math
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        """
        forest = [[1,2,3],[0,0,4],[7,6,5]]
        :param forest:
        :return:
        """
        todolist = []
        for (k, v) in enumerate(forest):
            for (k2, v2) in enumerate(v):
                if v2 > 1:
                    todolist.append((v2, (k, k2)))
        todolist.sort(key=lambda x: x[0])
        st = (0, 0)
        total = 0
        while len(todolist) > 0:
            pass
            val, pos = todolist.pop(0)
            res1 = self.getCnt(st, pos,  forest, 0, set())
            if res1 == -1:
                return -1
            total += res1
            st = pos
            forest[pos[0]][pos[1]] = 1
        return total


    def getCnt(self, curPos, targetPos, curMap, step, used):  # return step, newMap...
        if curPos == targetPos:
            return step


        v1 = curPos[0] + 1, curPos[1]
        v2 = curPos[0] - 1, curPos[1]
        v3 = curPos[0], curPos[1] + 1
        v4 = curPos[0], curPos[1] - 1
        step1 = math.inf
        if curPos[0] + 1 <= len(curMap) - 1:
            if curMap[curPos[0] + 1][curPos[1]] != 0:
                if v1 not in used:
                    newV = used.copy()
                    newV.add(v1)
                    step1 = min(step1, self.getCnt((curPos[0] + 1, curPos[1]), targetPos, curMap, step + 1, newV))
        if curPos[0] - 1 >= 0:
            if curMap[curPos[0] - 1][curPos[1]] != 0:
                if v2 not in used:
                    newV = used.copy()
                    newV.add(v1)

                    step1 = min(step1, self.getCnt((curPos[0] - 1, curPos[1]), targetPos, curMap, step + 1, newV ))
        if curPos[1] + 1 <= len(curMap[0]) - 1:
            if curMap[curPos[0]][curPos[1] + 1] != 0:
                if v3 not in used:
                    newV = used.copy()
                    newV.add(v3)
                    step1 = min(step1, self.getCnt((curPos[0], curPos[1] + 1), targetPos, curMap, step + 1, newV ))
        if curPos[1] - 1 >= 0:
            if curMap[curPos[0]][curPos[1] - 1] != 0:
                if v4 not in used:
                    newV = used.copy()
                    newV.add(v4)
                    step1 = min(step1, self.getCnt((curPos[0], curPos[1] - 1), targetPos, curMap, step + 1, newV))
        if step1 == math.inf:
            return math.inf
        return step1


a = Solution()
print(a.cutOffTree( forest = [[1,2,3],[0,0,0],[0,0,4]] ))