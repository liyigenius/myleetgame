from typing import List


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        """

        :param nums:
        :return:
        """
        ll =  [ bin(i)[2:].zfill(16) for i in nums]
        print(ll)


a = Solution()
print(a.countTriplets([2,1,3]))
