from typing import List
from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """
        grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
        :param grid:
        :param k:
        :return:
        """
        ll = deque()
        ll.append(((0, 0), 0, 0))  # step, kicked
        target = (len(grid) - 1, len(grid[0]) - 1)
        usedMap = {}
        while len(ll) > 0:
            idx, step, ked = ll.popleft()
            # search ..
            if idx == target:
                return step

            if idx not in usedMap:
                usedMap[idx] = (step, ked)
            else:
                prev,prev2 = usedMap[idx]
                if step < prev or ked < prev2:
                    pass
                    usedMap[idx] = (step, ked)

                else:
                    continue

            v1 = idx[0] - 1, idx[1]
            v2 = idx[0] + 1, idx[1]
            v3 = idx[0], idx[1] + 1
            v4 = idx[0], idx[1] - 1
            if v1[0] >= 0:
                if grid[v1[0]][v1[1]] == 1:
                    if ked + 1 <= k:
                        ll.append((v1, step + 1, ked + 1))
                else:
                    ll.append((v1, step + 1, ked))

            if v4[1] >= 0:
                if grid[v4[0]][v4[1]] == 1:
                    if ked + 1 <= k:
                        ll.append((v4, step + 1, ked + 1))
                else:
                    ll.append((v4, step + 1, ked))

            if v2[0] <= target[0]:
                if grid[v2[0]][v2[1]] == 1:
                    if ked + 1 <= k:
                        ll.append((v2, step + 1, ked + 1))
                else:
                    ll.append((v2, step + 1, ked))

            if v3[1] <= target[1]:
                if grid[v3[0]][v3[1]] == 1:
                    if ked + 1 <= k:
                        ll.append((v3, step + 1, ked + 1))
                else:
                    ll.append((v3, step + 1, ked))

        return -1

a = Solution()
print(a.shortestPath(grid = [[0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,1,1,1,1,0,0,0],[0,1,0,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,0,1,0],[0,0,0,0,0,0,0,0,1,0]], k = 1))