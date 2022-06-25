from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """

        :param arr:
        :return:
        """
        if len(arr) < 3:
            return 0
        