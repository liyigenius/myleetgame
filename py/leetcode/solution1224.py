from typing import List
from sortedcontainers import SortedDict

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        """

        :param nums:
        :return:
        """
        sd = SortedDict()