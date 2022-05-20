from typing import List


class Solution:
    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
        """
        gem = [3,1,2], operations = [[0,2],[2,1],[2,0]]
        :param gem:
        :param operations:
        :return:
        """
        for i in operations:
            v1 = gem[i[0]]
            res = v1 // 2
            gem[i[0]] -= res
            gem[i[1]] += res
        v1 = max(gem)
        v2 = min(gem)
        return v1 -v2

a = Solution()
print(a.giveGem(gem = [3,1,2], operations = [[0,2],[2,1],[2,0]]))