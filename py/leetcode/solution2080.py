from typing import List
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        """
        :param arr:
        """
        self.ary = arr


    def query(self, left: int, right: int, value: int) -> int:
        """

        :param left:
        :param right:
        :param value:
        :return:
        """
        cnt = 0
        for i in range(left, right+1):
            if self.ary[i] == value:
                cnt += 1
        return cnt



# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)