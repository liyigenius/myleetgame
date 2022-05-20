import math
from typing import List


class Solution:
    def __int__(self):
        self.m = 0

    def mctFromLeafValues(self, arr: List[int]) -> int:
        """

        :param arr:
        :return:
        """
        pass

        res = self.iterValue(arr, 0)
        return res

    # 0 cur, 1 submax
    def iterValue(self, arr, prev ):
        if len(arr) == 1:
            return prev + arr[0]
        if len(arr) == 0:
            return prev
        cnt = math.inf
        for (k,v) in enumerate(arr):
            if k == len(arr) -1:
                continue
            for j in range(k+1, len(arr)):
                newval = v * arr[j]
                rest2 = arr.copy()
                rest2.remove(v)
                rest2.remove(arr[j])
                cnt = min(cnt, self.iterValue(rest2, newval))

        return cnt


a = Solution()
print(a.mctFromLeafValues([2,4,6]))